from joke import Joke
from dao_jokes import DaoJokes

if __name__ == "__main__":
    connection_string = "mongodb://localhost:27017/"
    dao_jokes = DaoJokes(connection_string)

    joke = Joke("der witz", "baum", "John Doe")

    dao_jokes.insert(joke)

    retrieved_joke = dao_jokes.get_category("baum")
    print("Abgerufene Witze:")
    print(f"Joke: {retrieved_joke.text}, Author: {retrieved_joke.author}")

    deleted_count1 = dao_jokes.delete(retrieved_joke)
    print(dao_jokes.get_category("baum"))

