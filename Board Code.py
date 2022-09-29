#
# board.py
#
# A Board class for the Eight Puzzle
#
# name: Yoshiki Hoshinaga   
# email: yoshiki.hoshinaga@salve.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name: None
# partner's email: None
#

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)
        self.tiles = [[0] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1
        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for r in range(0,3):
            for c in range(0,3):
                self.tiles[r][c]=int(digitstr[3*r+c])
                if(self.tiles[r][c]==0):
                    self.blank_r=r
                    self.blank_c=c
    ### Add your other method definitions below. ###
    def __repr__(self):
        """returns a string representation of a Board object."""
        s=""
        s="" 
        for lst in self.tiles:
            for digit in lst:
                if digit != 0:
                    s += str(digit)
                    s += " "
                else:
                    s += "_"
                    s += " "
            s += "\n"
        return s

    def move_blank(self,direction):
        """takes as input a string direction that specifies the direction in which the blank should move,
            and that attempts to modify the contents of the called Board object accordingly. 
            Not all moves are possible on a given Board; for example, it isnâ€™t possible to move the blank 
            down if it is already in the bottom row. The method should return True or False to indicate 
            whether the requested move was possible.
        """
        nr=0
        nc=0
        if direction not in ["up", "down", "left", "right"]:
            print("unknown direction:" + " " + direction)
            return False
        if(direction=='up'):
            nr=self.blank_r-1
            nc=self.blank_c
            if(nr<0 or nr>2):
                return False
        elif(direction=='down'):
            nr=self.blank_r+1
            nc=self.blank_c
            if(nr<0 or nr>2):
                return False
        elif(direction=='left'):
            nr=self.blank_r
            nc=self.blank_c-1
            if(nc<0 or nc>2):
                return False
        elif(direction=='right'):
            nr=self.blank_r
            nc=self.blank_c+1
            if(nc<0 or nc>2):
                return False
        if nr >= 0 and nr <= 2 and nc >= 0 and nc <= 2:
            self.tiles[self.blank_r][self.blank_c] = self.tiles[nr][nc]
            self.tiles[nr][nc] = 0
            self.blank_r = nr
            self.blank_c = nc
            return True
        else:
            return False

    def digit_string(self):
        """creates and returns a string of digits that corresponds to 
            the current contents of the called Board objectâ€™s tiles attribute.
        """
        s=''
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[row])):
                s+=str(self.tiles[row][col])
        return s

    def copy(self):
        """returns a newly-constructed Board object that is a deep copy of the called object"""
        new_board=Board(self.digit_string())
        return new_board

    def num_misplaced(self):
        """counts and returns the number of tiles in the called Board object
            that are not where they should be in the goal state.
        """
        count = 0
        for idx in range(9):
            tmpRow = int(idx / 3)
            tmpCol = int(idx % 3)
            if self.tiles[tmpRow][tmpCol] != 0 and self.tiles[tmpRow][tmpCol] != idx:
                count += 1
        return count

    def num_manhattanDistance(self):
        """calculate the manhattan distance"""
        distance = 0
        for idx in range(9):
            idxRow = int(idx / 3)
            idxCol = int(idx % 3)
            if self.tiles[idxRow][idxCol] != 0 and self.tiles[idxRow][idxCol] != idx:
                curDigit = self.tiles[idxRow][idxCol]
                gr = int(curDigit / 3)
                gc = int(curDigit % 3)
                distance += abs(idxRow - gr)
                distance += abs(idxCol - gc)
        return distance

    def num_permutationInversions(self):
        """calculate the permutation inversions"""
        permutationInversions = 0
        for i in range(8):
            idxRowI = int(i / 3)
            idxColI = int(i % 3)
            if self.tiles[idxRowI][idxColI] != 0:
                for j in range(i + 1, 9):
                    idxRowJ = int(j / 3)
                    idxColJ = int(j % 3)

                    if self.tiles[idxRowI][idxColI] > self.tiles[idxRowJ][idxColJ] and self.tiles[idxRowJ][idxColJ] != 0:
                        permutationInversions += 1
            else:
                continue

        return permutationInversions

    def __eq__(self, other):
        """ overloads the == operator â€“ creating a version of the
            operator that works for Board objects. return True if
            the called object (self) and the
            argument (other) have the same
            values for the tiles attribute and False otherwise.
        """
        if self.digit_string() == other.digit_string():
            return True
        else:
            return False

if __name__=='__main__':
    #test
    #par1
    print('board_part1')
    b = Board('142358607')
    print(b.tiles)
    print(b.blank_r)
    print(b.blank_c)
    b2 = Board('631074852')
    print(b2.tiles)
    print(b2.blank_r)
    print(b2.blank_c)
    print()
    #part2
    print('borad_part2')
    b = Board('142358607')
    print(b)
    str(b)
    b = Board('142358607')
    print(b.tiles)
    print(b)
    b.tiles
    print()
    #part3
    print('board_part3')
    b = Board('142358607')
    print(b)
    print(b.move_blank('up'))
    print(b)
    print(b.tiles)
    print(b.blank_r)
    print(b.blank_c)
    print(b.move_blank('left'))
    print(b.blank_r)
    print(b.blank_c)
    print(b.move_blank('left'))
    print(b)
    print(b.move_blank('down'))
    print(b)
    print(b.move_blank('right'))
    print(b)
    print(b.move_blank('RIGHT'))
    print(b)
    print(b.blank_r)
    print(b.blank_c)
    print()
    #part4
    print('board_part4')
    b = Board('142358607')
    print(b.digit_string())
    print(b.move_blank('right'))
    print(b.move_blank('up'))
    print(b.digit_string())
    print()
    #part5
    print('board_part5')
    b = Board('142358607')
    print(b)
    b2 = b.copy()
    print(b2)
    print(b2.move_blank('up'))
    print(b2)
    print(b)
    print()
    #part6
    print('board_part6')
    b = Board('142358607')
    print(b)
    print(b.num_misplaced())
    print(b.move_blank('right'))
    print(b.num_misplaced())
    print()
    #part7
    print('board_part7')
    b1 = Board('012345678')
    b2 = Board('012345678')
    print(b1 == b2)
    print(b2.move_blank('right'))
    print(b1 == b2)
    print()
