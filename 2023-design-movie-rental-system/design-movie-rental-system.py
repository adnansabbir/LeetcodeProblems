from sortedcontainers import SortedList
from collections import defaultdict

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.search_optimized = defaultdict(SortedList)
        self.rented_sorted = SortedList(key= lambda e: (e[2], e[0], e[1]))
        self.rented_movies = set()
        self.movie_shop_price_map = {}

        for s, m, p in entries:
            if m not in self.search_optimized:
                self.search_optimized[m] = SortedList(key=lambda e: (e[0], e[1]))            
            self.search_optimized[m].add((p, s))
            self.movie_shop_price_map[(m, s)] = p
        
        # print(self.search_optimized)


    def search(self, movie: int) -> List[int]:
        # print(f'\n Searching\nMovie: {movie}\nShops: {self.search_optimized[movie]}\nReturned: {[s for p, s in self.search_optimized[movie][:5]]}')
        return [s for p, s in self.search_optimized[movie][:5]]
        

    def rent(self, shop: int, movie: int) -> None:
        # print(f'\n Renting\nMovie: {movie}\nShop: {shop}')
        p = self.movie_shop_price_map[(movie, shop)]
        self.search_optimized[movie].discard((p, shop))

        key = (shop, movie, p)
        if key not in self.rented_movies:
            self.rented_sorted.add(key)
            self.rented_movies.add(key)
        # print(f'Rented: {self.rented_sorted}\n Uniq: {self.rented_movies}')
        # print(f'Update: {self.search_optimized[movie]}')
        

    def drop(self, shop: int, movie: int) -> None:
        # print(f'\n Dropping\nMovie: {movie}\nShop: {shop}')
        p = self.movie_shop_price_map[(movie, shop)]
        self.search_optimized[movie].add((p, shop))

        key = (shop, movie, p)
        if key in self.rented_movies:
            self.rented_sorted.discard(key)
            self.rented_movies.remove(key)
        # print(f'Update: {self.search_optimized[movie]}')
        

    def report(self) -> List[List[int]]:
        return [[s, m] for s, m, p in self.rented_sorted[:5]]
        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()