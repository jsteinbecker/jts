%%%%%%%%%%%%%%%
%CHORD SQUASH MODE
%%%%%%%%%%%%%%%
\score {
  \header {
    piece = "CHORD SQUASH MODE"
    opus = "BWV 846" }
<<
  \new ChordNames {
    \chordmode {

	  \time 3/4

    % CHORD NAMES GO HERE
      g2. g4 c2 f4. c8 f4 g2.

    }

  }
  \new Voice \with {
    \consists "Pitch_squash_engraver"
  } \relative c'' {
    \improvisationOn
    \set repeatCountVisibility = #(every-nth-repeat-count-visible 1)
    \repeat percent 4 {


      %% BEAMED RYTHYM GOES HERE
      g8_"Each refrain consists of the progression repeated 4 times in total" 8 4 4 
      8 8 4 4
      4 8 8 4
      8 8 4 4 \break


      }
  }
>>
}
%%%%%%%%%%%%%%%%
%NORMAL REPEATS
%%%%%%%%%%%%%%%%
\score{
  \header {
    piece = "NORMAL REPEATS"
    opus = "\repeat volta 2 { c''4 d e f }" }
\relative {
  \repeat volta 2 { c''4 d e f }
  c2 d
  \repeat volta 2 { d4 e f g }

%%%%%%%%%%%%%%%%
%PERCENT REPEATS
%%%%%%%%%%%%%%%%
\relative {
  \repeat percent 2 { c''4^"PERCENT REPEATS" d e f }
  c2 d
  \repeat percent 7 { d4_"\repeat percent 7 { d4 e f g }" e f g }
}
}
}