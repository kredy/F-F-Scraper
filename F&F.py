'''

Performs cosine similarity and prints the appropriate headlines

'''

from core import f1_news, football_news
from core.process import TextProcess


def main():

    # Get football headlines
    print('Fetching football headlines... ')
    try:
        news_football = football_news.GetNews()
        fo_guardian_news = news_football.get_guardian_news()
        fo_independent_news = news_football.get_independent_news()
        fo_metro_news = news_football.get_metro_news()
        print('Done!')
    except:
        print('Cannot connect to the source.')
        print('\tMake sure that there is a working internet connection.')
        print('\tEnsure that the website is not down.')
        print('\tCheck whether the url to be connected is valid.')

    # Get F1 headlines
    print('Fetching Formula 1 headlines... ')
    try:
        news_f1 = f1_news.GetNews()
        f1_guardian_news = news_f1.get_guardian_news()
        f1_independent_news = news_f1.get_independent_news()
        f1_bbc_news = news_f1.get_bbc_news()
        print('Done!')
    except:
        print('Cannot connect to the source.')
        print('\tMake sure that there is a working internet connection.')
        print('\tEnsure that the website is not down.')
        print('\tCheck whether the url to be connected is valid.')

    text_process = TextProcess()

    # Final football news
    print('Finding the ideal mix... ')
    fo_final_news = {}
    for gu_x, gu_y in fo_guardian_news.items():
        gu_string = text_process.lemma(gu_y)
        fo_final_news[gu_x] = gu_y
        for id_x, id_y in fo_independent_news.items():
            id_string = text_process.lemma(id_y)
            if id_string.similarity(gu_string) < 0.7:
                fo_final_news[id_x] = id_y
            for mt_x, mt_y in fo_metro_news.items():
                mt_string = text_process.lemma(mt_y)
                if mt_string.similarity(gu_string) < 0.7 and mt_string.similarity(id_string) < 0.7:
                    fo_final_news[mt_x] = mt_y

    # Final Formula 1 news
    f1_final_news = {}
    for gu_x, gu_y in f1_guardian_news.items():
        gu_string = text_process.lemma(gu_y)
        f1_final_news[gu_x] = gu_y
        for id_x, id_y in f1_independent_news.items():
            id_string = text_process.lemma(id_y)
            if id_string.similarity(gu_string) < 0.7:
                    f1_final_news[id_x] = id_y
            for bbc_x, bbc_y in f1_bbc_news.items():
                bbc_string = text_process.lemma(bbc_y)
                if bbc_string.similarity(gu_string) < 0.7 and bbc_string.similarity(id_string) < 0.7:
                    f1_final_news[bbc_x] = bbc_y
    print('Done!\n\n')

    # Print a maximum of 10 football headlines
    print('*'*50)
    print('Football:\n')
    count = 0
    for x, y in fo_final_news.items():
        print(y)
        print(x)
        print('\n')
        count += 1
        if count == 10:
            break
    print('*'*50)
    print()

    # Print a maximum of 10 Formula 1 headlines
    count = 0
    print('Formula 1:\n')
    for x, y in f1_final_news.items():
        print(y)
        print(x)
        print('\n')
        count += 1
        if count == 10:
            break


if __name__ == '__main__':
    try:
        main()
    except:
        print('Error in code. Please inspect the code if it is modified.')
