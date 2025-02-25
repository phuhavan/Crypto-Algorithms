SHAKE256_RATE = 136  # Block size for SHAKE256

class KeccakState:
    def __init__(self):
        self.s = [0] * 25  # Keccak state of 25 uint64_t words
        self.pos = 0        # Position tracking

NROUNDS = 24

# Keccak round constants
KeccakF_RoundConstants = [
    0x0000000000000001,
    0x0000000000008082,
    0x800000000000808a,
    0x8000000080008000,
    0x000000000000808b,
    0x0000000080000001,
    0x8000000080008081,
    0x8000000000008009,
    0x000000000000008a,
    0x0000000000000088,
    0x0000000080008009,
    0x000000008000000a,
    0x000000008000808b,
    0x800000000000008b,
    0x8000000000008089,
    0x8000000000008003,
    0x8000000000008002,
    0x8000000000000080,
    0x000000000000800a,
    0x800000008000000a,
    0x8000000080008081,
    0x8000000000008080,
    0x0000000080000001,
    0x8000000080008008]

MASK64 = 0xFFFFFFFFFFFFFFFF

def ROL(a, offset):
    b = a & MASK64
    return ((b << offset) ^ (b >> (64-offset))) & MASK64

def KeccakF1600_StatePermute(state):
    """The Keccak F1600 Permutation."""

    # copyFromState(A, state)
    Aba = state[ 0]
    Abe = state[ 1]
    Abi = state[ 2]
    Abo = state[ 3]
    Abu = state[ 4]
    Aga = state[ 5]
    Age = state[ 6]
    Agi = state[ 7]
    Ago = state[ 8]
    Agu = state[ 9]
    Aka = state[10]
    Ake = state[11]
    Aki = state[12]
    Ako = state[13]
    Aku = state[14]
    Ama = state[15]
    Ame = state[16]
    Ami = state[17]
    Amo = state[18]
    Amu = state[19]
    Asa = state[20]
    Ase = state[21]
    Asi = state[22]
    Aso = state[23]
    Asu = state[24]

    for round in range(0, NROUNDS, 2):
        # prepareTheta
        BCa = Aba^Aga^Aka^Ama^Asa
        BCe = Abe^Age^Ake^Ame^Ase
        BCi = Abi^Agi^Aki^Ami^Asi
        BCo = Abo^Ago^Ako^Amo^Aso
        BCu = Abu^Agu^Aku^Amu^Asu

        # thetaRhoPiChiIotaPrepareTheta(round, A, E)
        Da = BCu^ROL(BCe, 1)
        De = BCa^ROL(BCi, 1)
        Di = BCe^ROL(BCo, 1)
        Do = BCi^ROL(BCu, 1)
        Du = BCo^ROL(BCa, 1)

        Aba ^= Da
        BCa = Aba
        Age ^= De
        BCe = ROL(Age, 44)
        Aki ^= Di
        BCi = ROL(Aki, 43)
        Amo ^= Do
        BCo = ROL(Amo, 21)
        Asu ^= Du
        BCu = ROL(Asu, 14)
        Eba =   BCa ^((~BCe)&  BCi )
        Eba ^= (KeccakF_RoundConstants[round] & MASK64)
        Ebe =   BCe ^((~BCi)&  BCo )
        Ebi =   BCi ^((~BCo)&  BCu )
        Ebo =   BCo ^((~BCu)&  BCa )
        Ebu =   BCu ^((~BCa)&  BCe )

        Abo ^= Do
        BCa = ROL(Abo, 28)
        Agu ^= Du
        BCe = ROL(Agu, 20)
        Aka ^= Da
        BCi = ROL(Aka,  3)
        Ame ^= De
        BCo = ROL(Ame, 45)
        Asi ^= Di
        BCu = ROL(Asi, 61)
        Ega =   BCa ^((~BCe)&  BCi )
        Ege =   BCe ^((~BCi)&  BCo )
        Egi =   BCi ^((~BCo)&  BCu )
        Ego =   BCo ^((~BCu)&  BCa )
        Egu =   BCu ^((~BCa)&  BCe )

        Abe ^= De
        BCa = ROL(Abe,  1)
        Agi ^= Di
        BCe = ROL(Agi,  6)
        Ako ^= Do
        BCi = ROL(Ako, 25)
        Amu ^= Du
        BCo = ROL(Amu,  8)
        Asa ^= Da
        BCu = ROL(Asa, 18)
        Eka =   BCa ^((~BCe)&  BCi )
        Eke =   BCe ^((~BCi)&  BCo )
        Eki =   BCi ^((~BCo)&  BCu )
        Eko =   BCo ^((~BCu)&  BCa )
        Eku =   BCu ^((~BCa)&  BCe )

        Abu ^= Du
        BCa = ROL(Abu, 27)
        Aga ^= Da
        BCe = ROL(Aga, 36)
        Ake ^= De
        BCi = ROL(Ake, 10)
        Ami ^= Di
        BCo = ROL(Ami, 15)
        Aso ^= Do
        BCu = ROL(Aso, 56)
        Ema =   BCa ^((~BCe)&  BCi )
        Eme =   BCe ^((~BCi)&  BCo )
        Emi =   BCi ^((~BCo)&  BCu )
        Emo =   BCo ^((~BCu)&  BCa )
        Emu =   BCu ^((~BCa)&  BCe )

        Abi ^= Di
        BCa = ROL(Abi, 62)
        Ago ^= Do
        BCe = ROL(Ago, 55)
        Aku ^= Du
        BCi = ROL(Aku, 39)
        Ama ^= Da
        BCo = ROL(Ama, 41)
        Ase ^= De
        BCu = ROL(Ase,  2)
        Esa =   BCa ^((~BCe)&  BCi )
        Ese =   BCe ^((~BCi)&  BCo )
        Esi =   BCi ^((~BCo)&  BCu )
        Eso =   BCo ^((~BCu)&  BCa )
        Esu =   BCu ^((~BCa)&  BCe )

        # prepareTheta
        BCa = Eba^Ega^Eka^Ema^Esa
        BCe = Ebe^Ege^Eke^Eme^Ese
        BCi = Ebi^Egi^Eki^Emi^Esi
        BCo = Ebo^Ego^Eko^Emo^Eso
        BCu = Ebu^Egu^Eku^Emu^Esu

        # thetaRhoPiChiIotaPrepareTheta(round+1, E, A)
        Da = BCu^ROL(BCe, 1)
        De = BCa^ROL(BCi, 1)
        Di = BCe^ROL(BCo, 1)
        Do = BCi^ROL(BCu, 1)
        Du = BCo^ROL(BCa, 1)

        Eba ^= Da
        BCa = Eba
        Ege ^= De
        BCe = ROL(Ege, 44)
        Eki ^= Di
        BCi = ROL(Eki, 43)
        Emo ^= Do
        BCo = ROL(Emo, 21)
        Esu ^= Du
        BCu = ROL(Esu, 14)
        Aba =   BCa ^((~BCe)&  BCi )
        Aba ^= (KeccakF_RoundConstants[round+1] & MASK64)
        Abe =   BCe ^((~BCi)&  BCo )
        Abi =   BCi ^((~BCo)&  BCu )
        Abo =   BCo ^((~BCu)&  BCa )
        Abu =   BCu ^((~BCa)&  BCe )

        Ebo ^= Do
        BCa = ROL(Ebo, 28)
        Egu ^= Du
        BCe = ROL(Egu, 20)
        Eka ^= Da
        BCi = ROL(Eka, 3)
        Eme ^= De
        BCo = ROL(Eme, 45)
        Esi ^= Di
        BCu = ROL(Esi, 61)
        Aga =   BCa ^((~BCe)&  BCi )
        Age =   BCe ^((~BCi)&  BCo )
        Agi =   BCi ^((~BCo)&  BCu )
        Ago =   BCo ^((~BCu)&  BCa )
        Agu =   BCu ^((~BCa)&  BCe )

        Ebe ^= De
        BCa = ROL(Ebe, 1)
        Egi ^= Di
        BCe = ROL(Egi, 6)
        Eko ^= Do
        BCi = ROL(Eko, 25)
        Emu ^= Du
        BCo = ROL(Emu, 8)
        Esa ^= Da
        BCu = ROL(Esa, 18)
        Aka =   BCa ^((~BCe)&  BCi )
        Ake =   BCe ^((~BCi)&  BCo )
        Aki =   BCi ^((~BCo)&  BCu )
        Ako =   BCo ^((~BCu)&  BCa )
        Aku =   BCu ^((~BCa)&  BCe )

        Ebu ^= Du
        BCa = ROL(Ebu, 27)
        Ega ^= Da
        BCe = ROL(Ega, 36)
        Eke ^= De
        BCi = ROL(Eke, 10)
        Emi ^= Di
        BCo = ROL(Emi, 15)
        Eso ^= Do
        BCu = ROL(Eso, 56)
        Ama =   BCa ^((~BCe)&  BCi )
        Ame =   BCe ^((~BCi)&  BCo )
        Ami =   BCi ^((~BCo)&  BCu )
        Amo =   BCo ^((~BCu)&  BCa )
        Amu =   BCu ^((~BCa)&  BCe )

        Ebi ^= Di
        BCa = ROL(Ebi, 62)
        Ego ^= Do
        BCe = ROL(Ego, 55)
        Eku ^= Du
        BCi = ROL(Eku, 39)
        Ema ^= Da
        BCo = ROL(Ema, 41)
        Ese ^= De
        BCu = ROL(Ese, 2)
        Asa =   BCa ^((~BCe)&  BCi )
        Ase =   BCe ^((~BCi)&  BCo )
        Asi =   BCi ^((~BCo)&  BCu )
        Aso =   BCo ^((~BCu)&  BCa )
        Asu =   BCu ^((~BCa)&  BCe )

    # copyToState(state, A)
    state[ 0] = Aba
    state[ 1] = Abe
    state[ 2] = Abi
    state[ 3] = Abo
    state[ 4] = Abu
    state[ 5] = Aga
    state[ 6] = Age
    state[ 7] = Agi
    state[ 8] = Ago
    state[ 9] = Agu
    state[10] = Aka
    state[11] = Ake
    state[12] = Aki
    state[13] = Ako
    state[14] = Aku
    state[15] = Ama
    state[16] = Ame
    state[17] = Ami
    state[18] = Amo
    state[19] = Amu
    state[20] = Asa
    state[21] = Ase
    state[22] = Asi
    state[23] = Aso
    state[24] = Asu

    return state

def keccak_absorb(s, pos, r, input, inlen):
    i = 0
    index = 0

    while(pos+inlen >= r):
        for i in range(pos, r):
            s[i // 8] ^= int(input[index]) << (8 * (i % 8))
            index += 1
        inlen -= r-pos
        KeccakF1600_StatePermute(s)
        pos = 0

    for i in range(pos, pos+inlen):
        s[i // 8] ^= int(input[index]) << (8 * (i % 8))
        index += 1

    return i


def store64(x: bytearray, u: int):
    """Stores a 64-bit integer into an 8-byte array (little-endian).

    Args:
        x (bytearray): The output array (must be at least 8 bytes).
        u (int): The 64-bit integer to store.
    """
    for i in range(8):
        x[i] = (u >> (8 * i)) & 0xFF

def shake256_absorb(state: KeccakState, data: bytes):
    """Absorbs input data into the SHAKE256 state.

    Args:
        state (KeccakState): The Keccak state.
        data (bytes): The input data to absorb.
    """
    state.pos = keccak_absorb(state.s, state.pos, SHAKE256_RATE, data)

def keccak_absorb_once(s: list, r: int, data: bytes, p: int):
    """Absorbs input into the Keccak state with padding.

    Args:
        s (list): Keccak state (list of 25 uint64 values).
        r (int): Rate (block size in bytes).
        data (bytes): Input data.
        p (int): Padding byte.
    """
    # Initialize state to zero
    for i in range(25):
        s[i] = 0

    inlen = len(data)
    offset = 0

    # Absorb full blocks
    while inlen >= r:
        for i in range(r // 8):
            s[i] ^= int.from_bytes(data[offset + 8 * i : offset + 8 * (i + 1)], 'little')
        offset += r
        inlen -= r
        KeccakF1600_StatePermute(s)

    # Absorb remaining bytes
    for i in range(inlen):
        s[i // 8] ^= data[offset + i] << (8 * (i % 8))

    # Apply padding
    s[inlen // 8] ^= p << (8 * (inlen % 8))
    s[(r - 1) // 8] ^= 1 << 63

def shake256_absorb_once(state: KeccakState, data: bytes):
    """Absorbs input into the Keccak state for SHAKE256 with one-time initialization.

    Args:
        state (KeccakState): Keccak state object.
        data (bytes): Input data.
    """
    SHAKE256_RATE = 136  # Rate for SHAKE256
    keccak_absorb_once(state.s, SHAKE256_RATE, data, 0x1F)
    state.pos = SHAKE256_RATE

def keccak_squeezeblocks(nblocks, s, r):
    """Squeezes `nblocks` blocks from the state `s` with rate `r`."""
    out = bytearray(nblocks * r)  # Allocate correct buffer size

    while nblocks:
        KeccakF1600_StatePermute(s)
        for i in range(r // 8):
            store64(out[8*i:8*(i+1)], s[i])  # Fix slice error
        nblocks -= 1
    
    return bytes(out)  # Convert back to immutable bytes

def shake256_squeezeblocks(nblocks: int, state: KeccakState) -> bytes:
    """Squeezes full blocks from the SHAKE256 state.

    Args:
        nblocks (int): Number of blocks to squeeze.
        state (KeccakState): Keccak state object.

    Returns:
        bytes: Squeezed output.
    """
    return keccak_squeezeblocks(nblocks, state.s, SHAKE256_RATE)


def keccak_squeeze(outlen: int, s: list, pos: int, r: int) -> tuple:
    """Squeezes Keccak output from the state.

    Args:
        outlen (int): Number of bytes to squeeze.
        s (list): Keccak state (list of 25 uint64 values).
        pos (int): Current position in the state.
        r (int): Rate (block size in bytes).

    Returns:
        tuple: (squeezed output bytes, updated pos)
    """
    out = bytearray()

    while outlen:
        if pos == r:
            KeccakF1600_StatePermute(s)
            pos = 0

        i = pos
        while i < r and i - pos < outlen:
            out.append((s[i // 8] >> (8 * (i % 8))) & 0xFF)
            i += 1

        outlen -= i - pos
        pos = i

    return bytes(out), pos

def shake256_squeeze(state: KeccakState, outlen: int) -> bytes:
    """Squeezes output data from the SHAKE256 state.

    Args:
        state (KeccakState): The Keccak state.
        outlen (int): Number of bytes to squeeze.

    Returns:
        bytes: The squeezed output.
    """
    out, state.pos = keccak_squeeze(outlen, state.s, state.pos, SHAKE256_RATE)
    return out


def shake256(outlen: int, data: bytes) -> bytes:
    """Computes the SHAKE256 hash of the input data.

    Args:
        outlen (int): Desired output length in bytes.
        data (bytes): Input data to be hashed.

    Returns:
        bytes: The SHAKE256 hash output.
    """
    state = KeccakState()

    # Absorb input data
    shake256_absorb_once(state, data)

    # Compute number of full blocks to squeeze
    nblocks = outlen // SHAKE256_RATE
    output = bytearray(shake256_squeezeblocks(nblocks, state))

    # Squeeze remaining bytes
    remaining_bytes, state.pos = keccak_squeeze(outlen - nblocks * SHAKE256_RATE, state.s, state.pos, SHAKE256_RATE)
    output.extend(remaining_bytes)

    return bytes(output)


message = b"\x12\x34"
digest = shake256(64, message)
print(digest.hex())