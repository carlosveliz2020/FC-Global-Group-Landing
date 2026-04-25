import React from 'react';
import { Composition } from 'remotion';
import { FcGlobalIntro } from './FcGlobalIntro';

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="FcGlobalIntro"
        component={FcGlobalIntro}
        durationInFrames={240}
        fps={30}
        width={1280}
        height={720}
      />
    </>
  );
};
