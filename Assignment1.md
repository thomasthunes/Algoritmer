# INF234 — Algorithms 
## Compulsory Assignment 1, due October 2nd, 20:00
## Set Theory:
 
 $a /notin b$ 
### b) ∪ and ∩

1. **∪** is the union operator, while **∩** is the intersection operator.
2. The union of a collection of sets is an operation that combines all the distinct elements from those sets to create a new set. The intersection of a collection of sets is an operator that combines all elements of a set that also belongs to all other sets in that collection.
3. **Correct:**
   - ¬(A U B) = ¬A ∩ ¬B
   - A U (B ∩ C) = (A U B) ∩ (A ∩ C)
4. **Incorrect:**
   - (A U B) = A ∩ B
   - A U B = B ∩ A

### c) ⊆ and ⊇

1. **⊆** is the subset operator, while **⊇** is the superset operator.
2. If all elements of set A also exist in set B, then set A is a subset of B, denoted A ⊆ B. Then B is called the superset of A, denoted B ⊇ A.
3. **Correct:**
   - {1, 2, 3} ⊆ {1, 2, 3, 4, 5, 6}
   - {1, 2, 3, 4, 5, 6} ⊇ {1, 2, 3}
   - A ⊆ B ⇔ A U B = B
   - B ⊇ A ⇔ A U B = B
4. **Incorrect:**
   - {1, 2, 3} ⊆ {4, 5, 6} ⊇ {7, 8, 9}
   - A ⊆ B ⇔ A U B = A
   - B ⊇ A ⇔ A U B = A

### d) ⊂ and ⊃

1. **⊂** is the «is a proper subset of» symbol, while **⊃** is the “is a proper superset of” symbol.
2. If set A is a proper subset/superset of another set B, then A and B cannot be equal.
3. **Correct:**
   - {1, 2, 3} ⊂ {1, 2, 3, 4, 5, 6}
   - {1, 2, 3, 4, 5, 6} ⊃ {1, 2, 3}
4. **Incorrect:**
   - {1, 2, 3} ⊂ {1, 2, 3}
   - {1, 2, 3} ⊃ {1, 2, 3}

### e) $\in$ and $\notin$

1. **∈** is the symbol for «is an element of» and **∈/** is the symbol for ”is not an element of”.
2. If some element is present in a set, then this element is an element of that set. E.g., an integer 1 is an element of the set of all integers, while a string “hello” is not an element of the set of all integers.
3. **Correct:**
   - 1 $\in$ {0, 1}
   - $100 \notin {0, 1}$
   - $ \forall \, x \in (1,2) $
   - 

