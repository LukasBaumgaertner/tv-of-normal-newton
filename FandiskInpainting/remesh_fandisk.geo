/*********************************************************************
 *
 *  From Gmsh tutorial 13
 *
 *  Remeshing STL with compounds
 *
 *********************************************************************/

Merge "fandisk_deleted.stl";
Merge "fandisk_fill_area.stl";

Coherence;
CreateTopology;

Delete Physicals;


ss[] = Surface "*";
For i In {1 : #ss[]-1}
  //Compound Surface(s+i) = ss[i];
  Compound Surface(ss[i]+1000) = ss[i];
  Physical Surface(ss[i]) = ss[i]+1000;
EndFor

Delete{
  //Surface{1};
  //Surface{2};
}


Physical Surface(0) = {1};

Field[7] = MathEval;
Field[7].F = "0.08";
Background Field = 7;

Mesh 2;
