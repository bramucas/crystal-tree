gt(I, F, T) :- value(I, F, V), V>T, thres(T).
le(I, F, T) :- value(I, F, V), V<=T, thres(T).
between(I, F, Min, Max) :- value(I, F, V), V>Min, thres(Min), V<=Max, thres(Max).

%!trace_rule {"Predicted class % for instance %", C, I}
prediction(I) :- class(C,I).

%!show_trace prediction(I).
