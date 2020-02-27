# Strings, Integers, and Bytes
---


Computers do not recognize strings. Strings are represented as numbers, and then numbers are represented
as binary digits.


ASCII and Unicode define the rules of how to map characters to numbers. UTF-8, UTF-16 and UTF-32 define how to store the numbers in bytes, in the aspect of how many bytes to use.

# ASCII

In ASCII, every letter, digits, and symbols that mattered (a-z, A-Z, 0–9, +, -, /, “, ! etc.) were represented as a number between 32 and 127. Most computers used 8-bits bytes then. This meant each byte could store 2⁸-1= 255 numbers.

**In ASCII, every character can be represented by an integer in [0, 255], and this integer can be converted to a byte.**

# Unicode

ASCII use a single byte to represent characters, which can only represent 255 characters.

The Unicode standard describes how characters are represented by **code points**. A **code point value is an integer in 
the range 0 to 0x10FFFF** (about 1.1 million values, with some 110 thousand assigned so far). 

![Example image](/static/images/unicode-table-example.png)


**In unicode system, every character can be represented by a hex number or a decimal number. Decimal numbers can be converted bytes.**

# Conversions between symbol, number and byte

**Every single character can have a number representation as well as a byte representation. Numbers can then be converted to bytes.**

## ASCII conversions

- Find the number representation of ASCII character `A`

    ```
    ord('A') # get number representation
    ```

    65

- Find the byte representation of ASCII character `A`

    ```    
    bin(ord('A')) # get byte representation
    ```

    '0b1000001'

- Convert a number back to character

	```
    chr(65)
    ```


    'A'

## Unicode conversions

- Find the number representation of unicode character `华`

	```
    ord('华')
    ```

    21326

- Find the **hex representation (code-point)** of unicode character `华`

    ```
    hex(ord('华'))
    ```

    '0x534e'

- Find the byte representation of unicode character `华`

    ```    
    bin(ord('华'))
    ```


    '0b101001101001110'


# UTF-8, UTF-16, and UTF-32

## UTF-8

UTF-8 uses 1 ~ 4 bytes

```
1 byte:       0 -     7F     (ASCII)
2 bytes:     80 -    7FF     (all European plus some Middle Eastern)
3 bytes:    800 -   FFFF     (multilingual plane incl. the top 1792 and private-use)
4 bytes:  10000 - 10FFFF
```

## UTF-16

UTF-16 uses 2 or 4 bytes

```
2 bytes:      0 -   D7FF     (multilingual plane except the top 1792 and private-use )
4 bytes:   D800 - 10FFFF
```

## UTF-32

UTF-32 uses 4 bytes


```
4 bytes:      0 - 10FFFF
```

