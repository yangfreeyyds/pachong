import requests
from bs4 import BeautifulSoup
import csv
import time
from concurrent.futures import ThreadPoolExecutor

def fetch_movie_data(session, url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = session.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        movies_list = []
        movies = soup.find_all('div', class_='item')

        for movie in movies:
            movie_data = {}
            movie_data['movie_detail_url'] = movie.find('a')['href']
            movie_data['image_url'] = movie.find('img')['src']
            title = movie.find('span', class_='title').contents
            movie_data['chinese_title'] = title[0].strip()
            movie_data['foreign_title'] = title[1].get_text().strip() if len(title) > 1 else ''
            movie_data['rating'] = float(movie.find('span', class_='rating_num').get_text())
            rating_num = movie.find('div', class_='star').findAll('span')[-1].contents[0]
            movie_data['rating_num'] = int(rating_num.strip('人评价'))
            summary = movie.find('span', class_='inq')
            movie_data['summary'] = summary.contents[0] if summary else ''
            info = movie.find('div', class_='bd').find('p').get_text().strip()
            movie_data['info'] = " ".join(info.split())

            movies_list.append(movie_data)

        return movies_list
    except requests.RequestException as e:
        print(f'Request failed: {e}')
    except Exception as e:
        print(f'Error scraping movie data: {e}')

def save_to_csv(movies, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=movies[0].keys())
        writer.writeheader()
        for movie in movies:
            writer.writerow(movie)

def main(start, session):
    url = f'https://movie.douban.com/top250?start={start}&filter='
    movies = fetch_movie_data(session, url)
    if movies:
        return movies
    else:
        return []

if __name__ == '__main__':
    start_time = time.time()

    # 使用线程池处理网络请求
    with requests.Session() as session, ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(main, start, session) for start in range(0, 250, 25)]
        results = [f.result() for f in futures]

    top250_movies = [movie for sublist in results for movie in sublist]  # Flatten the list of lists

    if top250_movies:
        save_to_csv(top250_movies, 'Top250Movies.csv')

    end_time = time.time()
    print(f'Time taken: {end_time - start_time} seconds')