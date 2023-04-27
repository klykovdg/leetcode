"""
In order to stop the Mad Coder evil genius you need to decipher the encrypted message
he sent to his minions. The message contains several numbers that,
when typed into a supercomputer, will launch a missile into the sky blocking out the sun,
and making all the people on Earth grumpy and sad.
You figured out that some numbers have a modified single digit in their binary representation.
More specifically, in the given number n the kth bit from the right was initially set to 0,
but its current value might be different.
It's now up to you to write a function that will change the kth bit of n back to 0.

Example
For n = 37 and k = 3, the output should be
solution(n, k) = 33.
37 = 100101 ~> 100001 = 3310.

For n = 37 and k = 4, the output should be
solution(n, k) = 37.
The 4th bit is 0 already (looks like the Mad Coder forgot to encrypt this number), so the answer is still 37.
"""


def solution(n: int, k: int) -> int:
    """
    start time: 00:32
    end time: 00:41
    """
    if n == 0:
        return 0
    reversed_k = -k
    bits = list(bin(n))
    bits[reversed_k] = '0'

    return int(''.join(bits), 2)


if __name__ == '__main__':
    n = 123
    ks = [7, 3, 6, 1]
    result = [59, 123, 91, 122]
    for k, r in zip(ks, result):
        print('actual {} expected {}'.format(solution(n, k), r))
    print('actual {} expected {}'.format(solution(0, 4), 0))
