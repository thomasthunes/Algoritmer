# INF234 — Algorithms
**Compulsory Assignment 1, due October 2nd, 20:00**

## Set Theory:

### b) ∪ and ∩
- ∪ is the union operator, while ∩ is the intersection operator.
- The union of a collection of sets is an operation that combines all the distinct elements from those sets to create a new set. The intersection of a collection of sets is an operator that combines all elements of a set that also belongs to all other sets in that collection.
- **Correct:**
    - ¬(A ∪ B) = ¬A ∩ ¬B
    - A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∩ C)
- **Incorrect:**
    - (A ∪ B) = A ∩ B
    - A ∪ B = B ∩ A

### c) ⊆ and ⊇
- ⊆ is the subset operator, while ⊇ is the superset operator.
- If all elements of set A also exist in set B, then set A is a subset of B, denoted A ⊆ B. Then B is called the superset of A, denoted B ⊇ A.
- **Correct:**
    - {1, 2, 3} ⊆ {1, 2, 3, 4, 5, 6}
    - {1, 2, 3, 4, 5, 6} ⊇ {1, 2, 3}
    - A ⊆ B ⇔ A ∪ B = B
    - B ⊇ A ⇔ A ∪ B = B
- **Incorrect:**
    - {1, 2, 3} ⊆ {4, 5, 6} ⊇ {7, 8, 9}
    - A ⊆ B ⇔ A ∪ B = A
    - B ⊇ A ⇔ A ∪ B = A

### d) ⊂ and ⊃
- ⊂ is the «is a proper subset of» symbol, while ⊃ is the “”is a proper superset of” symbol.
- If set A is a proper subset/superset of another set B, then A and B cannot be equal.
- **Correct:**
    - {1, 2, 3} ⊂ {1, 2, 3, 4, 5, 6}
    - {1, 2, 3, 4, 5, 6} ⊃ {1, 2, 3}
- **Incorrect:**
    - {1, 2, 3} ⊂ {1, 2, 3}
    - {1, 2, 3} ⊃ {1, 2, 3}

### e) ∈ and ∈/
- ∈ is the symbol for «is an element of» and ∈/ is the symbol for ”is not an element of”.
- If some element is present in a set, then this element is an element of that set. E.g., an integer 1 is an element of the set of all integers. While a string “hello” is not an element of the set of all Integers.
- **Correct:**
    - 1 ∈ {0, 1}, 100 ∈/ {0, 1}
    - ¬x ∈ Z, y ∈/ Z
- **Incorrect:**
    - 1 ∈ {0, 3}, 100 ∈/ {0, 100}
    - 1 ∈ 2

### f) \
- The symbol for relative complement
- A\B denotes the set of elements in A that is not in B.
- **Correct:**
    - {1, 2, 3, 4}\{1, 2, 3} = {4}
    - (B \ A) U C = (B U C) \ (A \ C)
- **Incorrect:**
    - {1, 2, 3, 4}\{1, 2, 3} = {1, 2, 3}
    - {1, 2, 3, 4}\{1, 2, 3} = {1, 2, 3, 1, 2, 3, 4}

### g) ||
- Cardinality
- Denotes the number of elements in a set.
- **Correct:**
    - |{1, 2, 3, 6}| = 4
    - |∅| = 0
- **Incorrect:**
    - |{1, 2, 3, 6}| = 6
    - |days_in_a_week| = 1

