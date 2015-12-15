
#include <stdio.h>
#include <math.h>
#include <vector>
#include <boost/python/module.hpp>
#include <boost/python/def.hpp>

#define PI 3.14159265359

using namespace std;
/*
class Cangmom
{
  public:
   float Jplus(float j, float m){return sqrt(j*(j+1)-m*(m+1));};
   float Jminus(float j, float m){return sqrt(j*(j+1)-m*(m-1));};
   float fct(int x);
   float CG(float,float,float,float,float,float);
   float ThreeJ(float,float,float,float,float,float);
   float Tri(float,float,float);
   float SixJ(float,float,float,float,float,float);
   float RacahW(float,float,float,float,float,float);
   float NineJ(float,float,float,float,float,float,float,float,float);
   float NormNineJ(float,float,float,float,float,float,float,float,float);
};
*/

float Jplus(float j, float m){return sqrt(j*(j+1)-m*(m+1));};
float Jminus(float j, float m){return sqrt(j*(j+1)-m*(m-1));};

float fct(int x)
{
   if (x < 0) return 0;
   float f = 1;
   for(int i=2;i<=x;i++)
   {
      f*= i;
   }
   return f;
}



float CG(float j1, float m1, float j2, float m2, float J, float M)
{
   if ((m1+m2)!=M || fabs(m1)>j1 || fabs(m2)>j2 || fabs(M)>J)
      return 0;
   if ( j1>(j2+J) || j1<fabs(j2-J) )
      return 0;
      
   // Step 1:  Find all overlaps < (j1, k1)(j2,J-k1) | JJ >
   // They are related by applying J+ to the j1 and j2 components
   // and setting the sum equal to J+|JJ> = 0. Normalization is from completeness.
   // Start with < (j1,j1)(j2,J-j1) | JJ >, with weight 1
   vector<float> Norm;
   vector<float> K;
   Norm.push_back(1.0);
   for (float k=j1;k>=(J-j2);k--)
   {
      K.push_back(k);
   }
   float n = 1;
   for (unsigned int i=1;i<K.size();i++)
   {
      float k = K[i];
      n *= -Jplus(j2,J-k-1) / Jplus(j1,k);
      Norm.push_back(n);
   }
   float div_factor = 0;
   for (unsigned int i=0;i<Norm.size();i++)
   {
      n = Norm[i];
      div_factor += n*n;
   }
   for (unsigned int i=0;i<Norm.size();i++)
   {
      Norm[i] /= sqrt(div_factor);
   }
   // Step 2: Apply J- to get from |JJ> to |JM>, and do the same
   // with j1 and j2. Do this for all the overlaps found in Step 1
   float cg = 0;
   for (unsigned int i=0;i<K.size();i++)
   {
     float k1 = K[i];
     float k2 = J-k1;
     if ( (k1<m1) || (k2<m2) ) continue;
     // multiply by a factor F to account for all the ways
     // you can get there by applying the lowering operator
     float F = fct(k1-m1+k2-m2) / ( fct(k1-m1)*fct(k2-m2) );
     // Apply the lowering operators
     float c1=1,c2=1,C=1;

     for (float k=k1;k>m1;k-=1)
       c1 *= Jminus(j1,k);
     for (float k=k2;k>m2;k-=1)
       c2 *= Jminus(j2,k);
     for (float k=J;k>M;k-=1)
       C  *= Jminus(J,k);
     cg += c1*c2/C * Norm[i] * F;
    }
    return cg;
}


float ThreeJ(float J1,float M1, float J2, float M2, float J, float M)
{
  return pow(-1,J1-J2+M)/sqrt(2*J+1)*CG(J1,M1,J2,M2,J,-M);
}

float Tri(float j1,float j2,float j3)
{
   return fct(j1+j2-j3) * fct(j1-j2+j3) * fct(-j1+j2+j3)/fct(j1+j2+j3+1);
}

//#####################################################################
//  Wigner 6-J symbol { j1 j2 j3 }  See definition and Racah formula at
//                    { J1 J2 J3 }  http://mathworld.wolfram.com/Wigner6j-Symbol.html
float SixJ(float j1, float j2, float j3, float J1, float J2, float J3)
{
  
  float triads[4][3] = {{j1,j2,j3},{j1,J2,J3},{J1,j2,J3},{J1,J2,j3}};
  
  for (int i=0;i<4;i++)
  {
     if ( (triads[i][0]+triads[i][1]<triads[i][2])
       || (triads[i][0]-triads[i][1]>triads[i][2])
       || ((int)(2*(triads[i][0]+triads[i][1]+triads[i][2]))%2>0) )
         return 0;
  } 
  float sixj = 0;
  for (float t=j1+j2+j3; t<=(j1+j2+j3+J1+J2+J3); t+=1)
  {
     float ff = fct(t-j1-j2-j3)*fct(t-j1-J2-J3)*
                fct(t-J1-j2-J3)*fct(t-J1-J2-j3)*
                fct(j1+j2+J1+J2-t)*fct(j2+j3+J2+J3-t)*
                fct(j3+j1+J3+J1-t) ;
     if (ff>0)
     {
        sixj += pow(-1,t) * fct(t+1)/ff;
     }
  
  }
  for (int i=0;i<4;i++)
  {
     sixj *= sqrt(Tri( triads[i][0],triads[i][1],triads[i][2]));
  }
  return sixj;
}

//###################################################################
//  Normalized 6-J symbol
//  [ J1 J2 J12 ]
//  [ J3 J  J23 ] = < J1 (J2 J3 J23) J M | (J1 J2 J12) J3 J M >
//
float NormSixJ(float J1, float J2, float J12, float J3, float J, float J23)
{
   return pow(-1,J1+J2+J3+J) * sqrt( (2*J12+1)*(2*J23+1) ) * SixJ(J1,J2,J12,J3,J,J23);
}

/*
float RacahW(float j1, float j2, float j3, float J1, float J2, float J3)
{
   return pow(-1,j1+j2+j3+J1) * SixJ(j1,j2,j3,J1,J2,J3);
}
*/

/*
float RacahW(float j1, float j2, float j3, float j4, float J, float K)
{
   return pow(-1,j1+j2+j3+j4) * SixJ(j1,j2,J,j3,j4,K);
}
*/

float RacahW(float j1, float j2, float j3, float j4, float J, float K)
{
   int sign = 1-2*(int(j1+j2+j3+j4)%2);
   //return sign * SixJ(j1,j2,J,j3,j4,K);
   return sign * SixJ(j1,j2,j3,j4,J,K);
}


float NineJ(float j1,float j2, float J12, float j3, float j4, float J34, float J13, float J24, float J)
{
   float ninej = 0;
   for (float g = fabs(J-j1); g<=J+j1; g+=1)
   {
      ninej += pow(-1,2*g) * (2*g+1)
                * SixJ(j1,j2,J12,J34,J,g)
                * SixJ(j3,j4,J34,j2,g,J24)
                * SixJ(J13,J24,J,g,j1,j3);
   }
   return ninej;
}

// Reduced matrix element of a spherical harmonic of rank Y between two single-particle states with
// angular momenta l and L
float LYL(int l,int Y,int L)
{
   return pow(-1,l)*sqrt( (2*l+1)*(2*Y+1)*(2*L+1)/(4*PI) ) * ThreeJ(l,0,Y,0,L,0);
}


float NormNineJ(float j1,float j2, float J12, float j3, float j4, float J34, float J13, float J24, float J)
{
   return sqrt( (2*J13+1)*(2*J24+1)*(2*J12+1)*(2*J34+1) ) * NineJ(j1,j2,J12,j3,j4,J34,J13,J24,J);

}

// Coefficient of fractional parentage for a j^3 configuration.
// 
float CFP3(float j, float J1, float J)
{
   float J0 = 0;
   float sj = SixJ(j,j,J0,J,j,J0);
   while (abs(sj) < 1e-5 && J0 < 2*j+0.1)
   {
      J0 += 2.0;
      sj = SixJ(j,j,J0,J,j,J0);
   }
   float del = fabs(J1-J0)<1e-5 ? 1.0 : 0.0;
   float cfp = del + 2*sqrt((2*J0+1)*(2*J1+1)) * SixJ(j,j,J1,J,j,J0);
   cfp /= sqrt(3+6*(2*J0+1)*sj);
   return cfp;
}


/*
void initCangmom()
{

};
*/

using namespace boost::python;

BOOST_PYTHON_MODULE(Cangmom)
{
   def("Jplus", Jplus);
   def("Jminus", Jminus);
   def("fct", fct);
   def("CG", CG);
   def("ThreeJ",ThreeJ);
   def("SixJ",SixJ);
   def("NormSixJ",NormSixJ);
   def("NineJ",NineJ);
   def("NormNineJ",NormNineJ);
   def("LYL",LYL);
   def("RacahW",RacahW);
   def("Tri",Tri);
//   def("initCangmom",initCangmom);
   def("CFP3",CFP3);

}

