from config import *
import analytics
import logging


# bot_token = "УДАЛЕНО"
# chat_id = 1662609079
# research.send_telegram(bot_token, "Тестовое сообщение")


logging.basicConfig(filename='analytics.log', level=logging.INFO, format='%(asctime)s %(message)s')

def main():
    research = analytics.Research(file)
    try:
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

        try:
            from config import bot_token
            research.send_telegram(bot_token, "The report has been successfully created")
        except ImportError:
            pass
        except Exception as e:
            logging.error('Telegram send error: %s', str(e))
    except Exception as e:
        logging.error('Error in main: %s', str(e))
        print("Error:", e)
        try:
            from config import bot_token
            research.send_telegram(bot_token, "The report hasn't been created due to an error")
        except ImportError:
            pass
        except Exception as e:
            logging.error('Telegram send error: %s', str(e))

if __name__ == '__main__':
    main()
