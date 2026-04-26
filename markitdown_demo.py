"""
FC Global Group — MarkItDown + Claude Document Processing
----------------------------------------------------------
Converts supplier documents (PDFs, Excel price lists, Word catalogs, CSVs)
into Markdown with markitdown, then sends them to Claude for intelligent
analysis: FBA margin scoring, compliance review, and catalog summarization.

Installation:
    pip install 'markitdown[all]' anthropic

Environment:
    export ANTHROPIC_API_KEY=your-key-here
"""

import os
import sys
from pathlib import Path

import anthropic

# ---------------------------------------------------------------------------
# System prompt — shared across all analysis calls (cached by the API)
# ---------------------------------------------------------------------------

_SYSTEM_PROMPT = """\
You are a wholesale distribution analyst for FC Global Group LLC, a U.S.-based
Amazon FBA company headquartered in Knoxville, Tennessee.

Your job is to analyze supplier documents and provide actionable intelligence:
- Identify products with strong Amazon FBA margin potential
- Flag compliance, authorization, or brand-integrity risks
- Summarize key terms, minimums, and payment conditions
- Recommend next steps for the purchasing team

Be concise, specific, and data-driven. Use bullet points and tables where helpful.\
"""

# ---------------------------------------------------------------------------
# Document conversion (markitdown)
# ---------------------------------------------------------------------------

def convert_document(filepath: str) -> str:
    """Convert a supplier document to Markdown using markitdown."""
    from markitdown import MarkItDown

    md = MarkItDown(enable_plugins=False)
    result = md.convert(filepath)
    return result.text_content


def batch_convert(directory: str, extensions: list[str] | None = None) -> dict[str, str]:
    """Convert all matching documents in a directory. Returns {filename: markdown}."""
    if extensions is None:
        extensions = [".pdf", ".docx", ".xlsx", ".xls", ".csv", ".pptx", ".html"]

    from markitdown import MarkItDown

    md = MarkItDown(enable_plugins=False)
    results: dict[str, str] = {}

    for path in Path(directory).iterdir():
        if path.suffix.lower() in extensions:
            try:
                result = md.convert(str(path))
                results[path.name] = result.text_content
                print(f"  ✓  {path.name}")
            except Exception as exc:
                print(f"  ✗  {path.name}: {exc}")

    return results


def save_markdown(content: str, output_path: str) -> None:
    """Write converted markdown to a file."""
    Path(output_path).write_text(content, encoding="utf-8")
    print(f"Saved → {output_path}")


# ---------------------------------------------------------------------------
# Claude analysis functions
# ---------------------------------------------------------------------------

def _stream_claude(prompt: str, label: str) -> str:
    """Send a prompt to Claude (streaming) and return the full response text."""
    client = anthropic.Anthropic()

    print(f"\n{'─' * 60}")
    print(f"Claude analysis — {label}")
    print('─' * 60)

    full_text = ""
    with client.messages.stream(
        model="claude-opus-4-7",
        max_tokens=4096,
        thinking={"type": "adaptive"},
        system=[
            {
                "type": "text",
                "text": _SYSTEM_PROMPT,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
            full_text += text

    print(f"\n{'─' * 60}\n")
    return full_text


def analyze_price_list(filepath: str) -> str:
    """
    Convert a supplier price list (Excel/CSV) and ask Claude to score
    each product for Amazon FBA margin potential.
    """
    print(f"Converting: {filepath}...")
    markdown = convert_document(filepath)

    prompt = (
        "Below is a supplier price list converted to Markdown.\n\n"
        "Tasks:\n"
        "1. Identify the **top 10 products** with the best Amazon FBA margin potential "
        "(consider typical FBA fees, category competitiveness, and price point).\n"
        "2. For each, estimate a rough **margin tier**: High (>30%), Medium (15-30%), Low (<15%).\n"
        "3. Flag any products to **avoid** (MAP violations, restricted categories, oversized).\n"
        "4. Recommend a **first purchase order** mix (units and SKUs) for a $5,000–$10,000 budget.\n\n"
        f"--- PRICE LIST ---\n{markdown}"
    )

    return _stream_claude(prompt, label=Path(filepath).name)


def compliance_review(filepath: str) -> str:
    """
    Convert a supplier agreement, authorization letter, or compliance doc
    and ask Claude to flag risks and missing requirements.
    """
    print(f"Converting: {filepath}...")
    markdown = convert_document(filepath)

    prompt = (
        "Below is a supplier document (authorization letter, reseller agreement, or compliance doc).\n\n"
        "Tasks:\n"
        "1. Summarize the **key terms**: authorized territory, product categories, duration.\n"
        "2. List any **restrictions** on resale channels (e.g. Amazon marketplace limitations).\n"
        "3. Identify **missing elements** we should request before proceeding "
        "(e.g. brand authorization letter, MAP policy, minimum purchase, payment terms).\n"
        "4. Rate the **risk level** (Low / Medium / High) with a one-line justification.\n\n"
        f"--- DOCUMENT ---\n{markdown}"
    )

    return _stream_claude(prompt, label=Path(filepath).name)


def catalog_summary(filepath: str) -> str:
    """
    Convert a product catalog and ask Claude for a strategic summary
    of the best opportunities for FC Global Group.
    """
    print(f"Converting: {filepath}...")
    markdown = convert_document(filepath)

    prompt = (
        "Below is a supplier product catalog converted to Markdown.\n\n"
        "Tasks:\n"
        "1. **Categorize** the product lines and count SKUs per category.\n"
        "2. Highlight **3–5 product lines** most suited for Amazon FBA wholesale distribution.\n"
        "3. Note any **brand recognition** signals (well-known vs. private label).\n"
        "4. Suggest **follow-up questions** for the supplier discovery call.\n\n"
        f"--- CATALOG ---\n{markdown}"
    )

    return _stream_claude(prompt, label=Path(filepath).name)


def batch_analyze(docs_dir: str, output_dir: str) -> None:
    """
    Convert every document in a folder, run a catalog_summary analysis
    on each, and save both the .md conversion and the .analysis.txt.
    """
    print(f"\nBatch analyzing: {docs_dir}")
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    results = batch_convert(docs_dir)

    for filename, markdown in results.items():
        stem = Path(filename).stem

        # Save raw markdown conversion
        md_path = str(Path(output_dir) / f"{stem}.md")
        save_markdown(markdown, md_path)

        # Run Claude analysis
        prompt = (
            "Below is a supplier document converted to Markdown. "
            "Provide a concise 3-paragraph summary covering: (1) what this supplier offers, "
            "(2) the best opportunities for an Amazon FBA wholesale buyer, "
            "(3) any risks or red flags.\n\n"
            f"--- DOCUMENT: {filename} ---\n{markdown}"
        )

        analysis = _stream_claude(prompt, label=filename)

        analysis_path = str(Path(output_dir) / f"{stem}.analysis.txt")
        Path(analysis_path).write_text(analysis, encoding="utf-8")
        print(f"Analysis saved → {analysis_path}")

    print(f"\nDone. {len(results)} document(s) processed → {output_dir}/")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

USAGE = """
Usage:
  python markitdown_demo.py <command> [args]

Commands:
  convert <file>                  Convert a document to Markdown (stdout)
  save <file> <output.md>         Convert and save to .md file
  batch <docs_dir> <out_dir>      Batch-convert a folder (no Claude analysis)
  price-list <file>               FBA margin analysis of a price list (Claude)
  compliance <file>               Compliance review of a supplier document (Claude)
  catalog <file>                  Strategic catalog summary (Claude)
  batch-analyze <docs_dir> <out>  Batch-convert + Claude summary for each doc

Environment:
  ANTHROPIC_API_KEY   Required for Claude commands (price-list, compliance,
                      catalog, batch-analyze)

Examples:
  python markitdown_demo.py convert supplier_catalog.pdf
  python markitdown_demo.py price-list wholesale_prices.xlsx
  python markitdown_demo.py compliance brand_auth_letter.pdf
  python markitdown_demo.py catalog full_product_line.pdf
  python markitdown_demo.py batch-analyze ./supplier_docs ./analyzed
"""


def main() -> None:
    args = sys.argv[1:]

    if not args or args[0] in ("-h", "--help"):
        print(USAGE)
        return

    command = args[0]

    if command == "convert" and len(args) == 2:
        print(convert_document(args[1]))

    elif command == "save" and len(args) == 3:
        save_markdown(convert_document(args[1]), args[2])

    elif command == "batch" and len(args) == 3:
        results = batch_convert(args[1])
        Path(args[2]).mkdir(parents=True, exist_ok=True)
        for filename, content in results.items():
            out = str(Path(args[2]) / f"{Path(filename).stem}.md")
            save_markdown(content, out)
        print(f"\n{len(results)} document(s) converted → {args[2]}/")

    elif command == "price-list" and len(args) == 2:
        analyze_price_list(args[1])

    elif command == "compliance" and len(args) == 2:
        compliance_review(args[1])

    elif command == "catalog" and len(args) == 2:
        catalog_summary(args[1])

    elif command == "batch-analyze" and len(args) == 3:
        batch_analyze(args[1], args[2])

    else:
        print("Unrecognized command or wrong number of arguments.")
        print(USAGE)
        sys.exit(1)


if __name__ == "__main__":
    main()
