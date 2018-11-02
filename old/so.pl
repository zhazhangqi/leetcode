edge(john, isa, cdpatient).
edge(cdpatient, shouldAvoid, gluten).
edge(noodle, contains, gluten).
edge(soba, ako, noodle).

value(Node, Slot, Value):- edge(Node, Slot, Value).
value(Node, Slot, Value):- 
edge(Node, isa, Node1),
value(Node1, Slot, Value).
value(Node, Slot, Value):-
edge(Node, ako, Node1),
value(Node1, Slot, Value).
value(Node, shouldAvoid, Node1):-
value(Node1, contains, Stuff),
value(Node, shouldAvoid, Stuff).