from Trie import Trie
class Boggle:
    def __init__(self, dictionary_file, input_file):
        """
        Boggle board class constructor

        :param dictionary_file: Dictionary of valid words
        :param input_file: input file formatted
        :return: None
        """
        self.trie = Trie()
        self.load_dictionary(dictionary_file)
        self.size, self.board = self.load_input(input_file)
        self.return_words = set()


    def __repr__(self):
        """
        Prints the Boggle board

        :return: A string representation of the board
        """
        return '\n'.join([' '.join(row) for row in self.board])


    def load_dictionary(self, dictionary_file):
        """
        Loads a dictionary_file into trie

        :param name: Path to the dictionary file
        :return: None
        """
        with open(dictionary_file, 'r') as f:
            for line in f:
                word = line.rstrip()
                if len(word) >= 3:
                    self.trie.insert(word)


    def load_input(self, input_file):
        """
        Loads a input_file into trie

        :param input_file: Path to the input file
        :return: a 2D board
        """
        f = open(input_file, 'r')
        size = int(f.readline())
        board = [line.strip().split(" ") for line in f]
        return size, board


    def search(self):
        """
        Call the dfs recursively and record the visited nodes. 

        :return: None
        """
        for x in range(self.size):
            for y in range(self.size):
                visited = set()
                self.dfs(self.trie.root, x, y, [], visited)
        self.return_words


    def dfs(self, trieNode, x, y, result, visited):
        """
        Depth-first search

        :param trieNode: current trieNode
        :param x: x cordenate on the board
        :param y: y cordenate on the board
        :param result: y cordenate on the board
        :return: None
        """
        # base case
        visited.add((x, y))
        current_letter = self.board[x][y]
        #print (current_letter)
        if current_letter not in trieNode.children:
            visited.remove((x, y))
            return

        if len(result) >= 3 and trieNode.isEnd:
            self.return_words.add("".join(result))

        result.append(current_letter)
        for nx, ny in [(x+1, y), (x-1, y), (x, y-1), (x, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]:
            if 0<=nx<=self.size-1 and 0<=ny<=self.size-1 and (nx, ny) not in visited:
                self.dfs(trieNode.children[current_letter], nx, ny, result, visited)
        result.pop()


if __name__ == '__main__':
    b = Boggle('words_alpha.txt', 'input_file.txt')
    print(b.size)
    print(b.board)
    b.search()
    print(b.return_words)