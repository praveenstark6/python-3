"""
    The message is "there's no place like home on a snowy night".
                        t o i o y
                        h p k n n    -> reversed
                        e l e a i
                        r a h s g    -> reversed
                        e c o n h
                        s e m o t    -> reversed
                        n l e w x
    And joined as "toioynnkpheleaigshareconhtomesnlewx" (encrypted message) , here the x is padded to form the rectangle

    Inputs : columns(int) and encrypted message.
    Output : the original message(decrypted message) without spaces and x(padded letter).
"""

columns = 5
encrypted_message = 'toioynnkpheleaigshareconhtomesnlewx'


def decrypt(message: str, col: int):
    result = []
    new = [message[i-col:i] for i in range(0, len(message)+1, col)][1:]
    for index in range(1, len(new), 2):
        new[index] = new[index].replace(new[index], new[index][::-1])
    for i in range(0, col):
        for j in range(0, len(new)):
            result.append(new[j][i])

    return "".join(result).rstrip("x")


print(decrypt(encrypted_message, columns))

# the code by Praveenkumar M.