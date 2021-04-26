gt(P, F, T) :- holds(P, F, V), V>T, thres(T).
le(P, F, T) :- holds(P, F, V), V<=T, thres(T).
between(P, F, Min, Max) :- holds(P, F, V), V>Min, thres(Min), V<=Max, thres(Max).

%!trace_rule {"Good (>5 years)"}
   prediction(P) :- alive(P).
%!trace_rule {"Bad (<5years)"}
   prediction(P) :- not_alive(P).

%!show_trace prediction(P).


thres(50).
thres(235).
thres(184).
thres(150).
thres(495).
thres(385).
thres(304).
thres(254).
thres(100).
thres(270).
thres(30825).
thres(725).
thres(459).
thres(10650).
thres(1244).
thres(634).
thres(509).
thres(21450).
thres(4244).
thres(2659).
thres(20994).
thres(479).
thres(745).
thres(915).
thres(1954).
thres(134).