# playfair-cipher

Playfair cipher is another cipher where the individual letters are substituted with their respective cipher letter as obtained using the key matrix.
The key matrix is made using the key and the remaining alphabets. if the letters are repeated in the key then they are added to the key matrix only once. the letters are added from left to right, row wise. the letters i and j are entered in a single cell, i.e. it is pre determined if the letter i or j is to be used, as a 5x5 matrix cant hold 26 characters this takes place.

# encryption
After the key matrix is formed the cipher text is to be generated, but there are certain rules that needs to be followed.
  1. Make pairs of characters in the plain text.
  2. Follow the rules to find the corresponding cipher text
    i.  If both the letters are in the same column: Take the letter below each one (going back to the top if at the bottom).
    ii. If both the letters are in the same row: Take the letter to the right of each one (going back to the leftmost if at the rightmost position).
    iii.If neither of the above rules is true: Form a rectangle with the two letters and take the letters on the horizontal opposite corner of the rectangle.
  3. In this way find the adjacent characters.
 
