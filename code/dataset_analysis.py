import pathlib
import music21

def analyze():
    chords = []
    measures = []
    for i in range(372)[1:]:
        if i < 10:
            ind = "00%s" % i
        elif i < 100:
            ind = "0%s" % i
        else:
            ind = "%s" %i
        if i % 10 == 0:
            print('Analyzing Chorale %s' % ind)

        analysis_file = (pathlib.Path(__file__).parent / ('../data/analysis/riemenschneider%s.txt' % ind)).resolve()
        rna = music21.converter.parse(analysis_file, format="romantext")
        for element in rna.recurse():
            if (type(element).__name__ == 'Measure'):
                measures.append(element)
            if (type(element).__name__ == 'RomanNumeral'):
                chords.append(element)
    print('Num Measures: %s' % len(measures))
    print('Num Numerals: %s' % len(chords))

analyze()