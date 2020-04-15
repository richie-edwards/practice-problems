# Time: O(n), where n is the movie lengths
# Space: O(n)


def is_flight_movies_sum(flight_length, movie_lengths):
    seen = set()
    for movie_length in movie_lengths:
        target = flight_length - movie_length
        if target in seen:
            print(
                f"Movie Length: {movie_length}, Target: {target}, Movie Lengths: {movie_lengths}")
            return True
        else:
            seen.add(movie_length)
    print(seen)
    return False


flight_length = 10
movie_lengths = [5, 3, 4, 2, 1, 9]
print(is_flight_movies_sum(flight_length, movie_lengths))
