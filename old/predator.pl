edge(bucky, isa, deer).
edge(deer, shouldAvoids, predator).
edge(lion, ako, predator).
edge(simba, isa, lion).

value(Node, Slot, Value):- edge(Node, Slot, Value).
value(Node, Slot, Value):- 
	edge(Node, isa, Node1),
	value(Node1, Slot, Value).
value(Node, Slot, Value):-
	edge(Node, ako, Node1),
	value(Node1, Slot, Value).
value(Node, shouldAvoid, Node1):-
	value(Node1, ako, Stuff),
	value(Node, shouldAvoid, Stuff).