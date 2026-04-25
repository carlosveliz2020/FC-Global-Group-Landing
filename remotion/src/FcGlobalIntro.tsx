import React from 'react';
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';

const GOLD = '#C4A255';
const GOLD_LIGHT = '#D4B76A';
const OBSIDIAN = '#050507';
const WHITE = '#FFFFFF';
const SILVER = '#9B9BAB';

function GridOverlay() {
  return (
    <AbsoluteFill
      style={{
        backgroundImage: `
          linear-gradient(rgba(255,255,255,0.015) 1px, transparent 1px),
          linear-gradient(90deg, rgba(255,255,255,0.015) 1px, transparent 1px)
        `,
        backgroundSize: '80px 80px',
        maskImage: 'radial-gradient(ellipse 70% 60% at 50% 50%, black 30%, transparent 100%)',
        WebkitMaskImage: 'radial-gradient(ellipse 70% 60% at 50% 50%, black 30%, transparent 100%)',
        pointerEvents: 'none',
      }}
    />
  );
}

function GoldLine({ frame, fps }: { frame: number; fps: number }) {
  const progress = spring({ frame, fps, config: { damping: 40, stiffness: 80 } });
  const width = interpolate(progress, [0, 1], [0, 320]);

  return (
    <div
      style={{
        width,
        height: 2,
        background: `linear-gradient(90deg, ${GOLD_LIGHT}, ${GOLD})`,
        borderRadius: 1,
        overflow: 'hidden',
      }}
    />
  );
}

function Logo({ frame, fps }: { frame: number; fps: number }) {
  const progress = spring({ frame, fps, config: { damping: 30, stiffness: 60 } });
  const opacity = interpolate(progress, [0, 1], [0, 1]);
  const translateY = interpolate(progress, [0, 1], [30, 0]);

  return (
    <div
      style={{
        display: 'flex',
        alignItems: 'center',
        gap: 3,
        fontFamily: 'Georgia, serif',
        fontSize: 52,
        fontWeight: 800,
        color: WHITE,
        letterSpacing: -2,
        opacity,
        transform: `translateY(${translateY}px)`,
      }}
    >
      <span>F</span>
      <div
        style={{
          width: 3,
          height: 36,
          background: GOLD,
          margin: '0 4px',
          transform: 'skewX(-8deg)',
        }}
      />
      <span>C</span>
      <span
        style={{
          fontSize: 11,
          fontWeight: 500,
          letterSpacing: 5,
          color: '#6B6B7B',
          marginLeft: 12,
          alignSelf: 'center',
          fontFamily: 'Arial, sans-serif',
        }}
      >
        GLOBAL GROUP
      </span>
    </div>
  );
}

function TagLine({ frame, fps }: { frame: number; fps: number }) {
  const progress = spring({ frame, fps, config: { damping: 30, stiffness: 50 } });
  const opacity = interpolate(progress, [0, 1], [0, 1]);
  const translateY = interpolate(progress, [0, 1], [20, 0]);

  return (
    <div
      style={{
        fontFamily: 'Arial, sans-serif',
        fontSize: 28,
        fontWeight: 300,
        color: WHITE,
        letterSpacing: -0.5,
        lineHeight: 1.2,
        textAlign: 'center',
        opacity,
        transform: `translateY(${translateY}px)`,
      }}
    >
      Strategic Wholesale{' '}
      <span
        style={{
          background: `linear-gradient(135deg, ${GOLD} 0%, ${GOLD_LIGHT} 100%)`,
          WebkitBackgroundClip: 'text',
          WebkitTextFillColor: 'transparent',
          fontWeight: 700,
        }}
      >
        Distribution
      </span>{' '}
      at Scale
    </div>
  );
}

function Stat({
  frame,
  fps,
  delay,
  value,
  label,
}: {
  frame: number;
  fps: number;
  delay: number;
  value: string;
  label: string;
}) {
  const localFrame = Math.max(0, frame - delay);
  const progress = spring({ frame: localFrame, fps, config: { damping: 30, stiffness: 60 } });
  const opacity = interpolate(progress, [0, 1], [0, 1]);
  const translateY = interpolate(progress, [0, 1], [24, 0]);

  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        gap: 6,
        padding: '28px 40px',
        background: 'rgba(11, 11, 15, 0.8)',
        border: '1px solid rgba(255,255,255,0.06)',
        borderRadius: 16,
        opacity,
        transform: `translateY(${translateY}px)`,
        backdropFilter: 'blur(10px)',
      }}
    >
      <div
        style={{
          fontFamily: 'Georgia, serif',
          fontSize: 32,
          fontWeight: 700,
          color: WHITE,
        }}
      >
        {value}
      </div>
      <div
        style={{
          fontFamily: 'Arial, sans-serif',
          fontSize: 11,
          color: SILVER,
          letterSpacing: 2,
          textTransform: 'uppercase',
        }}
      >
        {label}
      </div>
    </div>
  );
}

function EyebrowBadge({ frame, fps }: { frame: number; fps: number }) {
  const progress = spring({ frame, fps, config: { damping: 40, stiffness: 60 } });
  const opacity = interpolate(progress, [0, 1], [0, 1]);
  const scale = interpolate(progress, [0, 1], [0.92, 1]);

  return (
    <div
      style={{
        display: 'inline-flex',
        alignItems: 'center',
        gap: 8,
        padding: '8px 18px',
        background: 'rgba(196, 162, 85, 0.08)',
        border: `1px solid rgba(196, 162, 85, 0.2)`,
        borderRadius: 100,
        fontFamily: 'Arial, sans-serif',
        fontSize: 11,
        fontWeight: 600,
        color: GOLD,
        letterSpacing: 3,
        textTransform: 'uppercase' as const,
        opacity,
        transform: `scale(${scale})`,
      }}
    >
      <div
        style={{
          width: 7,
          height: 7,
          borderRadius: '50%',
          background: GOLD,
        }}
      />
      Amazon FBA Wholesale Partner
    </div>
  );
}

export const FcGlobalIntro: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const overallOpacity = interpolate(frame, [220, 240], [1, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });

  return (
    <AbsoluteFill
      style={{
        background: OBSIDIAN,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        gap: 40,
        opacity: overallOpacity,
      }}
    >
      <GridOverlay />

      {/* Ambient glow */}
      <div
        style={{
          position: 'absolute',
          width: 600,
          height: 600,
          borderRadius: '50%',
          background: `radial-gradient(circle, rgba(196,162,85,0.06) 0%, transparent 70%)`,
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          pointerEvents: 'none',
        }}
      />

      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 28 }}>
        {/* Eyebrow badge */}
        {frame >= 10 && <EyebrowBadge frame={Math.max(0, frame - 10)} fps={fps} />}

        {/* Gold line */}
        {frame >= 0 && (
          <GoldLine frame={frame} fps={fps} />
        )}

        {/* Logo */}
        {frame >= 20 && <Logo frame={Math.max(0, frame - 20)} fps={fps} />}

        {/* Gold line */}
        {frame >= 0 && (
          <div style={{ width: interpolate(spring({ frame, fps, config: { damping: 40, stiffness: 80 } }), [0, 1], [0, 320]), height: 1, background: 'rgba(196,162,85,0.2)', borderRadius: 1 }} />
        )}

        {/* Tagline */}
        {frame >= 50 && <TagLine frame={Math.max(0, frame - 50)} fps={fps} />}
      </div>

      {/* Stats */}
      {frame >= 100 && (
        <div
          style={{
            display: 'flex',
            gap: 20,
            marginTop: 10,
          }}
        >
          <Stat frame={Math.max(0, frame - 100)} fps={fps} delay={0} value="FBA" label="Fulfillment Model" />
          <Stat frame={Math.max(0, frame - 100)} fps={fps} delay={8} value="U.S." label="Knoxville, TN" />
          <Stat frame={Math.max(0, frame - 100)} fps={fps} delay={16} value="100%" label="Authorized Products" />
        </div>
      )}
    </AbsoluteFill>
  );
};
