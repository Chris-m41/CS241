from collections import deque


class Song:
    def __init__(self):
        self.title = "No title"
        self.artist = "No artist"

    def prompt(self):
        self.title = input("Enter title name: ")
        self.artist = input("Enter artist name: ")

    def display(self):
        print("Playing song: ")
        print("{} by {}".format(self.title, self.artist))


def main():
    playlist = deque()

    # Call Song class
    s = Song()

    # Initialize option to enter loop
    option = 0

    while option != 4:
        print("Options: ")
        print("1. Add a new song to the end of the playlist")
        print("2. Insert a new song to the beginning of the playlist")
        print("3. Play the next song")
        print("4. Quit")
        option = int(input("Enter selection: "))

        # Add song to beginning of playlist
        if option == 1:
            s.prompt()
            playlist.append(s)

        # Add song to end of playlist
        elif option == 2:
            s.prompt()
            playlist.appendleft(s)

        elif option == 3:
            if len(playlist) == 0:
                print("The playlist is currently empty")
            else:
                s = playlist.popleft()
                s.display()
        print("\n")

    print("Goodbye")


if __name__ == "__main__":
    main()
