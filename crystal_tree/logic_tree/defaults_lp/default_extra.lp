gt(P, F, T) :- holds(P, F, V), V>T, thres(T).
le(P, F, T) :- holds(P, F, V), V<=T, thres(T).
between(P, F, Min, Max) :- holds(P, F, V), V>Min, thres(Min), V<=Max, thres(Max).

%!trace_rule {"Predicted class % for instance %", C, P}
prediction(P) :- class(C,P).

%!show_trace prediction(P).
