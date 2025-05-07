package main

type TrieNode struct {
	child map[rune]*TrieNode
	end   bool
}

type Trie struct {
	root *TrieNode
}

func (t *Trie) Insert(word string) {
	pointer := t.root

	for _, v := range word {
		_, ok := pointer.child[v]
		if !ok {
			pointer.child[v] = &TrieNode{
				child: make(map[rune]*TrieNode),
				end:   false,
			}
		}
		pointer = pointer.child[v]
	}
	pointer.end = true
}

func (t *Trie) Search(word string) bool {
	pointer := t.root
	for _, v := range word {
		_, ok := pointer.child[v]
		if !ok {
			return false
		}
		pointer = pointer.child[v]
	}

	return pointer.end
}

func (t *Trie) StartsWith(prefix string) bool {
	pointer := t.root
	for _, v := range prefix {
		_, ok := pointer.child[v]
		if !ok {
			return false
		}
		pointer = pointer.child[v]
	}

	return true
}
