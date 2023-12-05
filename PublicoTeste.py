from PublicoWebScraper import PublicoWebScraper


def menu():
    urls = [
        'https://www.publico.pt/opiniao',
        'https://www.publico.pt/politica',
        'https://www.publico.pt/sociedade',
        'https://www.publico.pt/local',
        'https://www.publico.pt/mundo',
        'https://www.publico.pt/economia',
        'https://www.publico.pt/ciencia',
        'https://www.publico.pt/cultura',
        'https://www.publico.pt/desporto',
        'https://www.publico.pt/tecnologia',
        'https://www.publico.pt/multimedia',
        'https://www.publico.pt/jornalismo-de-dados'
    ]

    scraper = PublicoWebScraper(urls)
    scraper.fetch_data()

    if scraper.data:
        print("Dados extraidos")
        scraper.save_to_file('publico_output.txt')
    else:
        print("Nenhum dado extraido. Verificar HTML.")


menu()
