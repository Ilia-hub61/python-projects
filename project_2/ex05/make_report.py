from config import *
import analytics

def main():
    research = analytics.Research(file)
    data = research.file_reader()
    count = research.calc.counts()
    x, y = count
    fract = research.calc.fractions(x, y)
    predict_r = research.analyt.predict_random(num_of_steps)
    predict_l = research.analyt.predict_lastself()
    tails = sum(1 for p in predict_r if p == [0, 1])
    heads = sum(1 for p in predict_r if p == [1, 0])
    report = template.format(
        len(data), x, y, round(fract[0], 2), round(fract[1], 2), num_of_steps, tails, heads
    )
    print(report)
    research.analyt.save_file(output, report)

if __name__ == '__main__':
    main()
