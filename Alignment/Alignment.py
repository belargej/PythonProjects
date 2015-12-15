#!/usr/bin/python3 -i

from Cangmom import *
from numpy import array,arange
import numpy.polynomial.legendre as legendre
from math import cos,pi

####################################################################
####################################################################
#  Populate a state J1 with some m-state distribution Pm1
#  gamma decay to state J2, photon carries angular momentum L12
#     ( ie for an E2 transition 2+ -> 0+, J1=2 J2=0 L12=2 )
#     if there is mixing, give delta12 and L12 is the lower of the two
#     angular momenta
#  gamma decay again to state J3
#  initial m-state distribution can be listed as an array ( mj = -j ... +j )
#  or read from a file
#
#				- Ragnar Stroberg, May 2014
#
J1   = 4.0
J2   = 2.0
L12  = 2.0
delta12 = 0.0

J3 = 0.0
L23 = 2.0
delta23 = 0.0

# beam velocity. used if you want to
# plot the angular distribution in the
# lab frame
beta=0.345

# manual m-state population
Pm1 = [
0.14,
0.13,
0.12,
0.1,
0.1,
0.1,
0.12,
0.13,
0.14,
]

# options for reading m-state population from a file
read_from_tostevin_file = False
read_from_knockdif_file = False

# the included tostevin file is for a 9/2+ initial state
mstate_file = './state_9'
# the included knockdif file is for a 7/2- initial state
#mstate_file = 'knockdif.output'

# making plots requires pyROOT
makeplots = True
fitwithgaussian = False


####################################################################
###########     END OF USER INPUTS      ############################
####################################################################

##
## formulas taken from Olliver et al. PRC 68, 044312
##

def F(k,l,ll,Jf,Ji):
   coef = (-1)**(Jf+Ji+1)*((2*k+1)*(2*l+1)*(2*ll+1)*(2*Ji+1))**(1./2)
   tj = ThreeJ(l,1,ll,-1,k,0)
   sj = SixJ(l,ll,k,Ji,Ji,Jf)
   return coef * tj * sj

def A(k,l,Jf,Ji,delta):
   Ak = F(k,l,l,Jf,Ji)
   Ak += 2 * delta * F(k,l,l+1,Jf,Ji)
   Ak += delta**2 * F(k,l+1,l+1,Jf,Ji)
   return Ak/(1.+delta**2)

def B(k,Ji,Pm):
   Bksum = 0
   for i,P in enumerate(Pm):
      m = -Ji + i
      tj = ThreeJ(Ji,-m,Ji,m,k,0)
      Bksum += (-1)**(Ji+m) * tj * P
   return ((2*k+1)*(2*Ji+1))**(1./2) * Bksum



def ReadTostevinFile(filename):
   f = open(filename)
   Pmarray = []
   line = ''
   while 'Sum of all states' not in line:
      line = f.readline()
   line = f.readline()
   line = f.readline()
   while '--------' not in line:
      Pmarray.append(float(line.split()[2]))
      line = f.readline()
   f.close()
   return Pmarray


# Read a file from knockdif. These are given in
# terms of m_L, so we have to convert to m_J
def ReadKnockDifFile(filename):
   f = open(filename)
   Pml = []
   Pmj = []
   for line in f:
      if 'Stripping X-section' in line:
         Pml.append(float(line.split()[7]))
   l = len(Pml)-1
   if abs(J1-l)>0.6:
      print("Error: J1 = %f,   l = %f. Wrong m substate file?" %(J1,l))
   for i in arange(0,2*J1+1):
      mj = -J1 + i
      pmj = 0
      for ml in arange(mj-0.5,mj+1.5):
         if abs(ml)>l: continue
         cg = CG(J1,mj,0.5,ml-mj,l,ml)
         if ml == 0:
            pmj += cg*cg*Pml[abs(int(round(ml)))]
         else:
            pmj += cg*cg*Pml[abs(int(round(ml)))]/2.0
      Pmj.append(pmj)
   return Pmj
 

# Angular distribution W(theta)
def W(ak,costheta):
   a = []
   for x in ak:
      a.append(x)
      a.append(0)
   return legendre.legval(costheta,a)



# make sure everything is cast as floats
J1   = float(J1)
J2   = float(J2)
L12  = float(L12)
delta12 = float(delta12)
J3   = float(J3)
L23  = float(L23)
delta23 = float(delta23)


if (int(round(2*J1)))%2 > 0:
   J1label = "%.0f/2" %(2*J1)
   J2label = "%.0f/2" %(2*J2)
   J3label = "%.0f/2" %(2*J3)
else:
   J1label = "%.0f" %(J1)
   J2label = "%.0f" %(J2)
   J3label = "%.0f" %(J3)


if read_from_tostevin_file:
   Pm1 = ReadTostevinFile(mstate_file)
elif read_from_knockdif_file:
   Pm1 = ReadKnockDifFile(mstate_file)


# Normalize the Pm1 distribution, in case the user didn't
Pm1 = array(Pm1)/sum(Pm1)

if len(Pm1) != int(round(2*J1+1)):
   print("Error! I only have %d m-substates. Should have %d for J1=%.1f" % (len(Pm1),int(round(2*J1+1)),J1) )
   quit()

klist = range(0,10,2)
mstates1 = arange(-J1,J1+1)
mstates2 = arange(-J2,J2+1)

Pm2 = []
for m2 in mstates2:
   pm = 0
   for i,m1 in enumerate(mstates1):
      pm += Pm1[i] * CG(J1,m1,L12,m2-m1,J2,m2)**2 * (2*J1+1)/(2*J2+1)
   Pm2.append(pm)

# Normalize away rounding errors
Pm2 = array(Pm2)/sum(Pm2)

Ak12 = [ A(k,L12,J2,J1,delta12) for k in klist ]
Bk12 = [ B(k,J1,Pm1) for k in klist ]
ak12 = [ a*b for a,b in zip(Ak12,Bk12) ]

Ak23 = [ A(k,L23,J3,J2,delta23) for k in klist ]
Bk23 = [ B(k,J2,Pm2) for k in klist ]
ak23 = [ a*b for a,b in zip(Ak23,Bk23) ]

print ("%s -> %s" % (J1label,J2label))
print ("%3s  %14s  %14s  %14s" % ('k','Ak','Bk','ak'))
print (55*'-')

for k,A,B,a in zip(klist,Ak12,Bk12,ak12):
   print ("%3d  %14.7e  %14.7e  %14.7e" % (k,A,B,a))

print ("")
print ("%s -> %s" % (J2label,J3label))
print ("%3s  %14s  %14s  %14s" % ('k','Ak','Bk','ak'))
print (55*'-')

for k,A,B,a in zip(klist,Ak23,Bk23,ak23):
   print ("%3d  %14.7e  %14.7e  %14.7e" % (k,A,B,a))



if makeplots:
   try: from ROOT import *
   except:
     print("ERROR!")
     print("I can't find ROOT for plotting. Try doing")
     print("module load root")
     print("an re-runnin the script.")

   gStyle.SetBarWidth(0.1)
   gStyle.SetOptTitle(0)
   
   c1 = TCanvas("c1","c1")
   
   
   gMstates1 = TGraph(len(mstates1),array(mstates1),array(Pm1))
   gMstates1.Draw("APB")

   gMstates2 = TGraph(len(mstates2),mstates2+0.1,Pm2)
   gMstates2.SetFillColor(kRed)
   gMstates2.Draw("SAME B")
  
   if fitwithgaussian:
      gMstates1.Fit("gaus")
      gMstates2.Fit("gaus")
      gMstates1.GetFunction("gaus").SetLineColor(kBlack)
   


 
   gMstates1.GetYaxis().SetRangeUser(0,0.27)
   
   tlegend = TLegend(0.1,0.7,0.4,0.9)
   tlegend.SetBorderSize(0)
   tlegend.SetFillStyle(0)
   tlegend.AddEntry(gMstates1,"%s m states"%(J1label))
   tlegend.AddEntry(gMstates2,"%s m states"%(J2label))
   tlegend.Draw()
   
   c1.Update()
   
   

   
   c2 = TCanvas("c2","c2")
   thetas = arange(0.,180.)
   costheta = array([ cos(t) for t in thetas*pi/180.])
   
   gW1   = TGraph(len(thetas),thetas,W(ak12,costheta))
   gW2   = TGraph(len(thetas),thetas,W(ak23,costheta))
   gWIso = TGraph(len(thetas),thetas,W([1.0],costheta))

   gW1.SetLineColor(kBlack)
   gW2.SetLineColor(kRed)
   gW1.SetLineWidth(2)
   gW2.SetLineWidth(2)

   gWIso.SetLineColor(kBlack)
   gWIso.SetLineWidth(1)
   gWIso.SetLineStyle(7)

   gW1.Draw("AL")
   gW2.Draw("SAME L")
   gWIso.Draw("SAME L")
   gW1.GetYaxis().SetRangeUser(0.,2.0)
   gW1.GetXaxis().SetTitle("Rest frame #theta")
   gW1.GetXaxis().CenterTitle(1)
   gW1.GetYaxis().SetTitle("W(#theta)")
   gW1.GetYaxis().CenterTitle(1)

   tlegend_rest = TLegend(0.7,0.7,0.95,0.9)
   tlegend_rest.SetBorderSize(0)
   tlegend_rest.SetFillStyle(0)
   tlegend_rest.AddEntry(gW1,"%s#rightarrow%s"%(J1label,J2label),"L")
   tlegend_rest.AddEntry(gW2,"%s#rightarrow%s" %(J2label,J3label),"L")
   tlegend_rest.Draw()

   c2.Update()
  
 
   costhetacm = (costheta-beta)/(1-beta*costheta)
   c3 = TCanvas("c3","c3")
   gW1_boosted = TGraph(len(thetas),thetas,W(ak12,costhetacm)*(1-beta**2)/(1-beta*costheta)**2)
   gW2_boosted = TGraph(len(thetas),thetas,W(ak23,costhetacm)*(1-beta**2)/(1-beta*costheta)**2)
   gWIso_boosted = TGraph(len(thetas),thetas,W([1.0],costhetacm)*(1-beta**2)/(1-beta*costheta)**2)
   
   gW1_boosted.Draw("AL")
   gW2_boosted.Draw("SAME L")
   gWIso_boosted.Draw("SAME L")
   gW1_boosted.GetYaxis().SetRangeUser(0.,2.7)
   
   gW1_boosted.GetXaxis().SetTitle("Lab #theta")
   gW1_boosted.GetXaxis().CenterTitle(1)
   gW1_boosted.GetYaxis().SetTitle("W(#theta)")
   gW1_boosted.GetYaxis().CenterTitle(1)
   
   gW1_boosted.SetLineColor(kBlack)
   gW2_boosted.SetLineColor(kRed)
   gW1_boosted.SetLineWidth(2)
   gW2_boosted.SetLineWidth(2)
   gWIso_boosted.SetLineColor(kBlack)
   gWIso_boosted.SetLineWidth(1)
   gWIso_boosted.SetLineStyle(7)
   tlegend_lab = TLegend(0.7,0.7,0.95,0.90)
   tlegend_lab.SetBorderSize(0)
   tlegend_lab.SetFillStyle(0)
   tlegend_lab.AddEntry(gW1_boosted,"%s#rightarrow%s"%(J1label,J2label),"L")
   tlegend_lab.AddEntry(gW2_boosted,"%s#rightarrow%s" %(J2label,J3label),"L")
   tlegend_lab.Draw()
   c3.Update()



