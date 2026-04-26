"""
FC Global Group — MarkItDown Document Processing Demo
------------------------------------------------------
Demonstrates how markitdown can be used to convert supplier documents
(PDFs, Excel price lists, Word catalogs, CSVs) into Markdown for
downstream LLM analysis, compliance review, or archiving.

Installation:
    pip install 'markitdown[all]'

Optional (for AI image descriptions):
    pip install openai
    export OPENAI_API_KEY=your-key-here
"""

import os
import sys
from pathlib import Path


def convert_document(filepath: str) -> str:
    """Convert a supplier document to Markdown using markitdown."""
    from markitdown import MarkItDown

    md = MarkItDown(enable_plugins=False)
    result = md.convert(filepath)
    return result.text_content


def convert_with_llm_descriptions(filepath: str, model: str = "claude-opus-4-7") -> str:
    """
    Convert a document and use an LLM to generate descriptions for
    any embedded images (e.g. product photos in catalogs).
    Supports OpenAI-compatible clients.
    """
    from markitdown import MarkItDown
    from openai import OpenAI

    client = OpenAI()
    md = MarkItDown(llm_client=client, llm_model=model, enable_plugins=False)
    result = md.convert(filepath)
    return result.text_content


def batch_convert(directory: str, extensions: list[str] | None = None) -> dict[str, str]:
    """
    Convert all matching documents in a directory.

    Args:
        directory: Folder containing supplier documents.
        extensions: File types to process. Defaults to common business formats.

    Returns:
        Dict mapping file name → markdown text.
    """
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
# Demo scenarios relevant to FC Global Group's workflow
# ---------------------------------------------------------------------------

def demo_single_file(filepath: str) -> None:
    """Convert and print one supplier document."""
    print(f"\n--- Converting: {filepath} ---")
    markdown = convert_document(filepath)
    print(markdown[:2000])  # Preview first 2000 chars
    print("..." if len(markdown) > 2000 else "")


def demo_price_list_analysis(filepath: str) -> None:
    """
    Convert a supplier Excel/CSV price list and print a preview.
    In production this output would be fed to an LLM for margin analysis.
    """
    print(f"\n--- Price List Analysis: {filepath} ---")
    markdown = convert_document(filepath)

    # In a real pipeline you would send `markdown` to a Claude API call, e.g.:
    #
    #   import anthropic
    #   client = anthropic.Anthropic()
    #   response = client.messages.create(
    #       model="claude-opus-4-7",
    #       max_tokens=1024,
    #       messages=[{
    #           "role": "user",
    #           "content": (
    #               "Analyze this supplier price list and identify the top 10 products "
    #               "with the best Amazon FBA margin potential:\n\n" + markdown
    #           ),
    #       }],
    #   )
    #   print(response.content[0].text)

    print(markdown[:3000])


def demo_batch_supplier_docs(docs_dir: str, output_dir: str) -> None:
    """
    Batch-convert a folder of supplier documents and save each as a .md file.
    Useful for archiving or feeding into a vector store for retrieval.
    """
    print(f"\n--- Batch Converting Documents in: {docs_dir} ---")
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    results = batch_convert(docs_dir)

    for filename, content in results.items():
        stem = Path(filename).stem
        out_path = str(Path(output_dir) / f"{stem}.md")
        save_markdown(content, out_path)

    print(f"\nConverted {len(results)} document(s) → {output_dir}/")


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

USAGE = """
Usage:
  python markitdown_demo.py <command> [args]

Commands:
  convert <file>              Convert a single document to Markdown (stdout)
  save <file> <output.md>     Convert a document and save to file
  batch <docs_dir> <out_dir>  Batch-convert a folder of documents
  price-list <file>           Convert an Excel/CSV price list (analysis preview)

Examples:
  python markitdown_demo.py convert supplier_catalog.pdf
  python markitdown_demo.py save price_list.xlsx price_list.md
  python markitdown_demo.py batch ./supplier_docs ./markdown_docs
  python markitdown_demo.py price-list wholesale_prices.xlsx
"""


def main() -> None:
    args = sys.argv[1:]

    if not args or args[0] in ("-h", "--help"):
        print(USAGE)
        return

    command = args[0]

    if command == "convert" and len(args) == 2:
        demo_single_file(args[1])

    elif command == "save" and len(args) == 3:
        content = convert_document(args[1])
        save_markdown(content, args[2])

    elif command == "batch" and len(args) == 3:
        demo_batch_supplier_docs(args[1], args[2])

    elif command == "price-list" and len(args) == 2:
        demo_price_list_analysis(args[1])

    else:
        print("Unrecognized command or wrong number of arguments.")
        print(USAGE)
        sys.exit(1)


if __name__ == "__main__":
    main()
