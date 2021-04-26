%!trace_rule {"rec_hypertension is false"}
tree_node(0,P,left) :- holds(P,rec_hypertension,false).

%!trace_rule {"rec_vhc is false"}
tree_node(1,P,left) :- holds(P,rec_vhc,false), tree_node(0,P,left).

%!trace_rule {"don_acv is false"}
tree_node(2,P,left) :- holds(P,don_acv,false), tree_node(1,P,left).

%!trace_rule {"don_microesteatosis <= 0.5"}
tree_node(3,P,left) :- le(P,don_microesteatosis,50), tree_node(2,P,left).

%!trace_rule {"rec_abdominal_surgery is false"}
tree_node(4,P,left) :- holds(P,rec_abdominal_surgery,false), tree_node(3,P,left).

%!trace_rule {"rec_afp <= 2.350000023841858"}
tree_node(5,P,left) :- le(P,rec_afp,235), tree_node(4,P,left).

%!trace_rule {"rec_afp <= 1.8499999642372131"}
tree_node(6,P,left) :- le(P,rec_afp,184), tree_node(5,P,left).

alive(P) :- tree_node(6,P,left).
%!trace_rule {"rec_afp > 1.8499999642372131"}
tree_node(6,P,right) :- gt(P,rec_afp,184), tree_node(5,P,left).

%!trace_rule {"rec_provenance <= 0.5"}
tree_node(8,P,left) :- le(P,rec_provenance,50), tree_node(6,P,right).

alive(P) :- tree_node(8,P,left).
%!trace_rule {"rec_provenance > 0.5"}
tree_node(8,P,right) :- gt(P,rec_provenance,50), tree_node(6,P,right).

not_alive(P) :- tree_node(8,P,right).
%!trace_rule {"rec_afp > 2.350000023841858"}
tree_node(5,P,right) :- gt(P,rec_afp,235), tree_node(4,P,left).

%!trace_rule {"rec_provenance <= 1.5"}
tree_node(11,P,left) :- le(P,rec_provenance,150), tree_node(5,P,right).

%!trace_rule {"rec_provenance <= 0.5"}
tree_node(12,P,left) :- le(P,rec_provenance,50), tree_node(11,P,left).

%!trace_rule {"rec_afp <= 4.950000047683716"}
tree_node(13,P,left) :- le(P,rec_afp,495), tree_node(12,P,left).

alive(P) :- tree_node(13,P,left).
%!trace_rule {"rec_afp > 4.950000047683716"}
tree_node(13,P,right) :- gt(P,rec_afp,495), tree_node(12,P,left).

alive(P) :- tree_node(13,P,right).
%!trace_rule {"rec_provenance > 0.5"}
tree_node(12,P,right) :- gt(P,rec_provenance,50), tree_node(11,P,left).

alive(P) :- tree_node(12,P,right).
%!trace_rule {"rec_provenance > 1.5"}
tree_node(11,P,right) :- gt(P,rec_provenance,150), tree_node(5,P,right).

not_alive(P) :- tree_node(11,P,right).
%!trace_rule {"rec_abdominal_surgery is true"}
tree_node(4,P,right) :- holds(P,rec_abdominal_surgery,true), tree_node(3,P,left).

alive(P) :- tree_node(4,P,right).
%!trace_rule {"don_microesteatosis > 0.5"}
tree_node(3,P,right) :- gt(P,don_microesteatosis,50), tree_node(2,P,left).

alive(P) :- tree_node(3,P,right).
%!trace_rule {"don_acv is true"}
tree_node(2,P,right) :- holds(P,don_acv,true), tree_node(1,P,left).

%!trace_rule {"rec_afp <= 3.850000023841858"}
tree_node(20,P,left) :- le(P,rec_afp,385), tree_node(2,P,right).

%!trace_rule {"rec_afp <= 3.049999952316284"}
tree_node(21,P,left) :- le(P,rec_afp,304), tree_node(20,P,left).

%!trace_rule {"don_microesteatosis <= 0.5"}
tree_node(22,P,left) :- le(P,don_microesteatosis,50), tree_node(21,P,left).

%!trace_rule {"rec_afp <= 2.549999952316284"}
tree_node(23,P,left) :- le(P,rec_afp,254), tree_node(22,P,left).

%!trace_rule {"rec_abdominal_surgery is false"}
tree_node(24,P,left) :- holds(P,rec_abdominal_surgery,false), tree_node(23,P,left).

%!trace_rule {"rec_provenance <= 1.0"}
tree_node(25,P,left) :- le(P,rec_provenance,100), tree_node(24,P,left).

alive(P) :- tree_node(25,P,left).
%!trace_rule {"rec_provenance > 1.0"}
tree_node(25,P,right) :- gt(P,rec_provenance,100), tree_node(24,P,left).

alive(P) :- tree_node(25,P,right).
%!trace_rule {"rec_abdominal_surgery is true"}
tree_node(24,P,right) :- holds(P,rec_abdominal_surgery,true), tree_node(23,P,left).

alive(P) :- tree_node(24,P,right).
%!trace_rule {"rec_afp > 2.549999952316284"}
tree_node(23,P,right) :- gt(P,rec_afp,254), tree_node(22,P,left).

%!trace_rule {"rec_abdominal_surgery is false"}
tree_node(29,P,left) :- holds(P,rec_abdominal_surgery,false), tree_node(23,P,right).

%!trace_rule {"rec_provenance <= 0.5"}
tree_node(30,P,left) :- le(P,rec_provenance,50), tree_node(29,P,left).

not_alive(P) :- tree_node(30,P,left).
%!trace_rule {"rec_provenance > 0.5"}
tree_node(30,P,right) :- gt(P,rec_provenance,50), tree_node(29,P,left).

alive(P) :- tree_node(30,P,right).
%!trace_rule {"rec_abdominal_surgery is true"}
tree_node(29,P,right) :- holds(P,rec_abdominal_surgery,true), tree_node(23,P,right).

not_alive(P) :- tree_node(29,P,right).
%!trace_rule {"don_microesteatosis > 0.5"}
tree_node(22,P,right) :- gt(P,don_microesteatosis,50), tree_node(21,P,left).

%!trace_rule {"rec_afp <= 2.700000047683716"}
tree_node(34,P,left) :- le(P,rec_afp,270), tree_node(22,P,right).

alive(P) :- tree_node(34,P,left).
%!trace_rule {"rec_afp > 2.700000047683716"}
tree_node(34,P,right) :- gt(P,rec_afp,270), tree_node(22,P,right).

not_alive(P) :- tree_node(34,P,right).
%!trace_rule {"rec_afp > 3.049999952316284"}
tree_node(21,P,right) :- gt(P,rec_afp,304), tree_node(20,P,left).

alive(P) :- tree_node(21,P,right).
%!trace_rule {"rec_afp > 3.850000023841858"}
tree_node(20,P,right) :- gt(P,rec_afp,385), tree_node(2,P,right).

%!trace_rule {"rec_afp <= 308.25"}
tree_node(38,P,left) :- le(P,rec_afp,30825), tree_node(20,P,right).

%!trace_rule {"rec_abdominal_surgery is false"}
tree_node(39,P,left) :- holds(P,rec_abdominal_surgery,false), tree_node(38,P,left).

%!trace_rule {"rec_provenance <= 0.5"}
tree_node(40,P,left) :- le(P,rec_provenance,50), tree_node(39,P,left).

%!trace_rule {"rec_afp <= 7.25"}
tree_node(41,P,left) :- le(P,rec_afp,725), tree_node(40,P,left).

%!trace_rule {"don_microesteatosis <= 1.0"}
tree_node(42,P,left) :- le(P,don_microesteatosis,100), tree_node(41,P,left).

alive(P) :- tree_node(42,P,left).
%!trace_rule {"don_microesteatosis > 1.0"}
tree_node(42,P,right) :- gt(P,don_microesteatosis,100), tree_node(41,P,left).

not_alive(P) :- tree_node(42,P,right).
%!trace_rule {"rec_afp > 7.25"}
tree_node(41,P,right) :- gt(P,rec_afp,725), tree_node(40,P,left).

alive(P) :- tree_node(41,P,right).
%!trace_rule {"rec_provenance > 0.5"}
tree_node(40,P,right) :- gt(P,rec_provenance,50), tree_node(39,P,left).

%!trace_rule {"rec_afp <= 4.599999904632568"}
tree_node(46,P,left) :- le(P,rec_afp,459), tree_node(40,P,right).

%!trace_rule {"don_microesteatosis <= 1.0"}
tree_node(47,P,left) :- le(P,don_microesteatosis,100), tree_node(46,P,left).

alive(P) :- tree_node(47,P,left).
%!trace_rule {"don_microesteatosis > 1.0"}
tree_node(47,P,right) :- gt(P,don_microesteatosis,100), tree_node(46,P,left).

not_alive(P) :- tree_node(47,P,right).
%!trace_rule {"rec_afp > 4.599999904632568"}
tree_node(46,P,right) :- gt(P,rec_afp,459), tree_node(40,P,right).

alive(P) :- tree_node(46,P,right).
%!trace_rule {"rec_abdominal_surgery is true"}
tree_node(39,P,right) :- holds(P,rec_abdominal_surgery,true), tree_node(38,P,left).

%!trace_rule {"rec_afp <= 106.5"}
tree_node(51,P,left) :- le(P,rec_afp,10650), tree_node(39,P,right).

not_alive(P) :- tree_node(51,P,left).
%!trace_rule {"rec_afp > 106.5"}
tree_node(51,P,right) :- gt(P,rec_afp,10650), tree_node(39,P,right).

alive(P) :- tree_node(51,P,right).
%!trace_rule {"rec_afp > 308.25"}
tree_node(38,P,right) :- gt(P,rec_afp,30825), tree_node(20,P,right).

not_alive(P) :- tree_node(38,P,right).
%!trace_rule {"rec_vhc is true"}
tree_node(1,P,right) :- holds(P,rec_vhc,true), tree_node(0,P,left).

%!trace_rule {"rec_afp <= 12.449999809265137"}
tree_node(55,P,left) :- le(P,rec_afp,1244), tree_node(1,P,right).

%!trace_rule {"don_acv is false"}
tree_node(56,P,left) :- holds(P,don_acv,false), tree_node(55,P,left).

alive(P) :- tree_node(56,P,left).
%!trace_rule {"don_acv is true"}
tree_node(56,P,right) :- holds(P,don_acv,true), tree_node(55,P,left).

%!trace_rule {"rec_abdominal_surgery is false"}
tree_node(58,P,left) :- holds(P,rec_abdominal_surgery,false), tree_node(56,P,right).

%!trace_rule {"rec_afp <= 6.349999904632568"}
tree_node(59,P,left) :- le(P,rec_afp,634), tree_node(58,P,left).

%!trace_rule {"don_microesteatosis <= 0.5"}
tree_node(60,P,left) :- le(P,don_microesteatosis,50), tree_node(59,P,left).

%!trace_rule {"rec_afp <= 5.099999904632568"}
tree_node(61,P,left) :- le(P,rec_afp,509), tree_node(60,P,left).

alive(P) :- tree_node(61,P,left).
%!trace_rule {"rec_afp > 5.099999904632568"}
tree_node(61,P,right) :- gt(P,rec_afp,509), tree_node(60,P,left).

not_alive(P) :- tree_node(61,P,right).
%!trace_rule {"don_microesteatosis > 0.5"}
tree_node(60,P,right) :- gt(P,don_microesteatosis,50), tree_node(59,P,left).

not_alive(P) :- tree_node(60,P,right).
%!trace_rule {"rec_afp > 6.349999904632568"}
tree_node(59,P,right) :- gt(P,rec_afp,634), tree_node(58,P,left).

alive(P) :- tree_node(59,P,right).
%!trace_rule {"rec_abdominal_surgery is true"}
tree_node(58,P,right) :- holds(P,rec_abdominal_surgery,true), tree_node(56,P,right).

alive(P) :- tree_node(58,P,right).
%!trace_rule {"rec_afp > 12.449999809265137"}
tree_node(55,P,right) :- gt(P,rec_afp,1244), tree_node(1,P,right).

%!trace_rule {"rec_abdominal_surgery is false"}
tree_node(67,P,left) :- holds(P,rec_abdominal_surgery,false), tree_node(55,P,right).

%!trace_rule {"don_microesteatosis <= 1.0"}
tree_node(68,P,left) :- le(P,don_microesteatosis,100), tree_node(67,P,left).

%!trace_rule {"rec_afp <= 214.5"}
tree_node(69,P,left) :- le(P,rec_afp,21450), tree_node(68,P,left).

%!trace_rule {"rec_afp <= 42.44999885559082"}
tree_node(70,P,left) :- le(P,rec_afp,4244), tree_node(69,P,left).

%!trace_rule {"don_acv is false"}
tree_node(71,P,left) :- holds(P,don_acv,false), tree_node(70,P,left).

%!trace_rule {"rec_afp <= 26.59999942779541"}
tree_node(72,P,left) :- le(P,rec_afp,2659), tree_node(71,P,left).

not_alive(P) :- tree_node(72,P,left).
%!trace_rule {"rec_afp > 26.59999942779541"}
tree_node(72,P,right) :- gt(P,rec_afp,2659), tree_node(71,P,left).

alive(P) :- tree_node(72,P,right).
%!trace_rule {"don_acv is true"}
tree_node(71,P,right) :- holds(P,don_acv,true), tree_node(70,P,left).

not_alive(P) :- tree_node(71,P,right).
%!trace_rule {"rec_afp > 42.44999885559082"}
tree_node(70,P,right) :- gt(P,rec_afp,4244), tree_node(69,P,left).

not_alive(P) :- tree_node(70,P,right).
%!trace_rule {"rec_afp > 214.5"}
tree_node(69,P,right) :- gt(P,rec_afp,21450), tree_node(68,P,left).

alive(P) :- tree_node(69,P,right).
%!trace_rule {"don_microesteatosis > 1.0"}
tree_node(68,P,right) :- gt(P,don_microesteatosis,100), tree_node(67,P,left).

%!trace_rule {"don_acv is false"}
tree_node(78,P,left) :- holds(P,don_acv,false), tree_node(68,P,right).

not_alive(P) :- tree_node(78,P,left).
%!trace_rule {"don_acv is true"}
tree_node(78,P,right) :- holds(P,don_acv,true), tree_node(68,P,right).

alive(P) :- tree_node(78,P,right).
%!trace_rule {"rec_abdominal_surgery is true"}
tree_node(67,P,right) :- holds(P,rec_abdominal_surgery,true), tree_node(55,P,right).

not_alive(P) :- tree_node(67,P,right).
%!trace_rule {"rec_hypertension is true"}
tree_node(0,P,right) :- holds(P,rec_hypertension,true).

%!trace_rule {"rec_abdominal_surgery is false"}
tree_node(82,P,left) :- holds(P,rec_abdominal_surgery,false), tree_node(0,P,right).

%!trace_rule {"don_microesteatosis <= 0.5"}
tree_node(83,P,left) :- le(P,don_microesteatosis,50), tree_node(82,P,left).

%!trace_rule {"rec_afp <= 209.94999980926514"}
tree_node(84,P,left) :- le(P,rec_afp,20994), tree_node(83,P,left).

%!trace_rule {"rec_vhc is false"}
tree_node(85,P,left) :- holds(P,rec_vhc,false), tree_node(84,P,left).

%!trace_rule {"rec_provenance <= 1.0"}
tree_node(86,P,left) :- le(P,rec_provenance,100), tree_node(85,P,left).

%!trace_rule {"rec_afp <= 4.799999952316284"}
tree_node(87,P,left) :- le(P,rec_afp,479), tree_node(86,P,left).

alive(P) :- tree_node(87,P,left).
%!trace_rule {"rec_afp > 4.799999952316284"}
tree_node(87,P,right) :- gt(P,rec_afp,479), tree_node(86,P,left).

%!trace_rule {"don_acv is false"}
tree_node(89,P,left) :- holds(P,don_acv,false), tree_node(87,P,right).

alive(P) :- tree_node(89,P,left).
%!trace_rule {"don_acv is true"}
tree_node(89,P,right) :- holds(P,don_acv,true), tree_node(87,P,right).

%!trace_rule {"rec_afp <= 7.450000047683716"}
tree_node(91,P,left) :- le(P,rec_afp,745), tree_node(89,P,right).

alive(P) :- tree_node(91,P,left).
%!trace_rule {"rec_afp > 7.450000047683716"}
tree_node(91,P,right) :- gt(P,rec_afp,745), tree_node(89,P,right).

alive(P) :- tree_node(91,P,right).
%!trace_rule {"rec_provenance > 1.0"}
tree_node(86,P,right) :- gt(P,rec_provenance,100), tree_node(85,P,left).

alive(P) :- tree_node(86,P,right).
%!trace_rule {"rec_vhc is true"}
tree_node(85,P,right) :- holds(P,rec_vhc,true), tree_node(84,P,left).

%!trace_rule {"rec_afp <= 9.150000095367432"}
tree_node(95,P,left) :- le(P,rec_afp,915), tree_node(85,P,right).

alive(P) :- tree_node(95,P,left).
%!trace_rule {"rec_afp > 9.150000095367432"}
tree_node(95,P,right) :- gt(P,rec_afp,915), tree_node(85,P,right).

%!trace_rule {"don_acv is false"}
tree_node(97,P,left) :- holds(P,don_acv,false), tree_node(95,P,right).

alive(P) :- tree_node(97,P,left).
%!trace_rule {"don_acv is true"}
tree_node(97,P,right) :- holds(P,don_acv,true), tree_node(95,P,right).

%!trace_rule {"rec_afp <= 19.549999713897705"}
tree_node(99,P,left) :- le(P,rec_afp,1954), tree_node(97,P,right).

not_alive(P) :- tree_node(99,P,left).
%!trace_rule {"rec_afp > 19.549999713897705"}
tree_node(99,P,right) :- gt(P,rec_afp,1954), tree_node(97,P,right).

alive(P) :- tree_node(99,P,right).
%!trace_rule {"rec_afp > 209.94999980926514"}
tree_node(84,P,right) :- gt(P,rec_afp,20994), tree_node(83,P,left).

not_alive(P) :- tree_node(84,P,right).
%!trace_rule {"don_microesteatosis > 0.5"}
tree_node(83,P,right) :- gt(P,don_microesteatosis,50), tree_node(82,P,left).

alive(P) :- tree_node(83,P,right).
%!trace_rule {"rec_abdominal_surgery is true"}
tree_node(82,P,right) :- holds(P,rec_abdominal_surgery,true), tree_node(0,P,right).

%!trace_rule {"rec_afp <= 1.3499999642372131"}
tree_node(104,P,left) :- le(P,rec_afp,134), tree_node(82,P,right).

not_alive(P) :- tree_node(104,P,left).
%!trace_rule {"rec_afp > 1.3499999642372131"}
tree_node(104,P,right) :- gt(P,rec_afp,134), tree_node(82,P,right).

alive(P) :- tree_node(104,P,right).
