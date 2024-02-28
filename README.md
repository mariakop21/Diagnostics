# Multi-line diagnostics for the optical identification of Supernova Remnants

These are  diagnostics for the optical identification of Supernova Remnants (SNRs). In 
<a href="https://ui.adsabs.harvard.edu/abs/2020MNRAS.491..889K/abstract">Kopsacheili et al. 2020</a> multi-line diagnostics are presented for the separation of SNRs from HII regions. They have been built using <a href="https://ui.adsabs.harvard.edu/abs/2008ApJS..178...20A/abstract">shock</a> and photoionization or starburst (<a href="https://ui.adsabs.harvard.edu/abs/2001ApJ...556..121K/abstract">2001</a>, <a href="https://ui.adsabs.harvard.edu/abs/2010AJ....139..712L/abstract">2010</a>) models from <a href="https://ascl.net/1306.008">MAPPINGS III</a> modeling code that are considered as SNRs and HII regions respectively. 

The separation of these two types of nebulae is based on the different emission-line ratios of lines presented in their spectra. In the multi-line diagnostics the emission-line ratios predicted by the models are combined in 2 and 3 dimensions (where each dimension is an emission-line ratio), and using a Support Vector Machine (SVM) model the line (in the case of 2D) or the surface (in the case of 3D) that best separates shock from photoionization models (or SNRs from HII regions) has been calculated.

The diagnostics are basically the function that describes the aforementioned lines or surfaces. They combine the following emission-line ratios in 2 and 3 dimensions: 
$`\rm [N\,II](6583)/H\alpha,\, [S\,II](6716,6731)/H\alpha,\, [O\,I](6300)/H\alpha,\, [O\,II](3727,3729)/H\beta,\,[O\,III](5008)/H\beta `$.

In <a href="https://ui.adsabs.harvard.edu/abs/2020MNRAS.491..889K/abstract">Kopsacheili et al. 2020</a> the functions are presented in tables where one can find the coefficients combined with polynomials of 2nd and 3rd order and construct them. Here, these functions can be found in python format and used directly. In every case, in order for a source to be considered as a SNR$`^*`$ the function $f$ should be positive. Apart from the functions, the schematic respesantation of the diagnostics is presented. In every case, red color corresponds to the starburst models (HII regions) and green to the shock models (SNRs). The black lines and the blue surfaces are the lines and surfaces that best separate the two classes (i.e. the decision functions of SVM).

The scripts '2D_SNR_diagsotics.py' and '3D_SNR_diagsotics.py' are provided too, along with the ascii files
'factors_2d.txt' and 'factors_3d.txt'. The latters contain the factors axx and axxx (as presented below) that are used by the polynomials that describe the diagnostics. The '2D_SNR_diagsotics.py' and '3D_SNR_diagsotics.py' use these files in order to calculate the diagnostics. In the case of 2D diagnostics, one can run:

<pre xml:lang="latex">python 2D_SNR_diagntostics.py -ha [x1] -sii [x2] -nii [x3]  -oi [x4] -oii [x5] -oiii [x6] -hb [x7] -diag [diagntostic] </pre>

where [x1], [x2], ....., [x7] is the observed flux/luminosity of a source  of: $`\rm H\alpha(6563), [S\,II](6717,6731), [N\,II](6583), [O\,I](6300), [O\,II](3729,3731), [O\,III](5007), H\beta(4681)`$ respectively.

The parameter 'diag' refers to the 2D-diagnostics of interest and it should be one of the following:
1. 'SII-NII', 2. 'NII-OIII', 3. 'SII-OIII', 4. 'OI-OIII', 5. 'NII-OI', 
6. 'OII-OIII', 7. 'NII-OII', 8. 'SII-OI', 9. 'OI-OII', 10. 'SII-OII'

Those are the diagntostics that combine the emission line ratios: 
1. [S II]/Ha-[N II]/Ha,  2. [N II]/Ha-[O III]/Hb, 3. [S II]/Ha-[O III]/Hb, 4. [O I]/Ha-[O III]/Hb, 5. [N II]/Ha-[O I]/Ha
6. [O II]/Hb-[O III]/Hb, 7. [N II]/Ha-[O II]/Hb,  8. [S II]/Ha-[O I]/Ha,   9. [O I]/Ha-[O II]/Hb,  10. [S II]/Ha-[O II]/Hb,
   respectively.

For the 3D diagnostics:
<pre xml:lang="latex">python 3D_SNR_diagntostics.py -ha [x1] -sii [x2] -nii [x3]  -oi [x4] -oii [x5] -oiii [x6] -hb [x7] -diag [diagntostic]  </pre>

The [x1], [x2], ....., [x7] are same as in the 2D case, however now, the parameter 'diag' refers to the 3D diagnostics and it should be one of the following:]


1.'NII-SII-OIII', 2.'NII-SII-OI', 3.'NII-SII-OII',  4.'NII-OII-OIII', 5.'NII-OI-OII',

6.'NII-OI-OIII',  7.'SII-OI-OII', 8.'SII-OII-OIII', 9.'SII-OI-OIII', 10.'OI-OII-OIII',

Those are the diagntostics that combine the emission line ratios: 

1.[N II]/Ha-[S II]/Ha-[O III]/Hb,  2.[N II]/Ha-[S II]/Ha-[O I]/Ha, 3.[N II]/Ha-[S II]/Ha-[O II]/Hb,  4.[N II]/Ha-[O II]/Hb-[O III]/Hb, 5.[N II]/Ha-[O I]/Ha-[O II]/Hb,

6.[N II]/Ha-[O I]/Ha-[O III]/Hb,   7.[S II]/Ha-[O I]/Ha-[O II]/Hb, 8.[S II]/Ha-[O II]/Hb-[O III]/Hb, 9.[S II]/Ha-[O I]/Ha-[O III]/Hb, 10.[O I]/Ha-[O II]/Hb-[O III]/Hb,
respectively.

In both cases, the default value of the emission lines is 0.01. This means that if one or more emission lines are not available  they can be skipped (of course in this case the diagnsotics that use these lines cannot be calculated).  There is no default diagnostic so it should be always defined.

*$`^*`$ By using these diagnostics someone should be aware that false positives can be identified. For this reason it is more safe to consider them all as candidate SNRs.*

### $`\rm {\bf{[S\,II]/H\alpha - [N\,II]/H\alpha}}`$ 
<br> a30 = -0.043
<br> a21 =  0.175
<br> a20 = -0.257
<br> a12 =  0.029
<br> a11 = -2.452
<br> a10 =  2.244
<br> a03 = -0.217
<br> a02 =  1.388
<br> a01 =  1.116
<br> a00 =  2.763

$`\rm f\_SII\_NII(x, y) = a30x^3 + a21x^2y + a20x^2 + a12xy^2 + a11xy + a10x + a03y^3 + a02y^2 + a01y + a00`$

<font color='gray'>  where $`\rm x = log_{10}([S\,II]/H\alpha)`$ and $`\rm y = log_{10}([N\,II]/H\alpha).`$ </font>
<br> <font color='gray'>  So, in this case if f_SII_NII(x, y) > 0, the source can be considered as a SNR. </font>

![image](https://github.com/mariakop21/Diagnostics/assets/25170839/4ded3cc7-5103-4dde-b5ca-fd4044172a36)



```python
f_SII_NII = lambda x, y: (a30*x**3.0 + a21*x**2.0*y + a20*x**2.0 + a12*x*y**2.0 + a11*x*y + a10*x + 
                          a03*y**3.0 + a02*y**2.0 + a01*y + a00)
```

### $`\rm {\bf{[N\,II]/H\alpha - [O\,III]/H\beta}}`$ 

<br> a10 =  0.939
<br> a01 =  1.000
<br> a00 =  0.469

$`\rm f\_NII\_OIII(x, y) = a10x + a01y + a00 `$

<font color='gray'>  where $`\rm x = log_{10}([N\,II]/H\alpha)`$ and $` \rm y = log_{10}([O\,III]/H\beta)`$.</font> 
<br> <font color='gray'> If f_NII_OIII(x, y) > 0, the source can be considered as a SNR. </font>

![image](https://github.com/mariakop21/Diagnostics/assets/25170839/2a9b29ad-ef22-49e6-aaf6-af0c6f28d272)



```python
f_NII_OIII = lambda x, y: (a10*x + a01*y + a00)
```

### $`\rm {\bf{[S\,II]/H\alpha - [O\,III]/H\beta}}`$ 
<br> a30 =  0.079
<br> a21 =  0.148
<br> a20 =  -1.821
<br> a12 =  -0.318
<br> a11 =  -0.781
<br> a10 =  4.66
<br> a03 =  0.255
<br> a02 =  -0.479
<br> a01 =  4.433
<br> a00 =  3.403

$`\rm f\_SII\_OIII(x, y) = a30x^3 + a21x^2y + a20x^2 + a12xy^2 + a11xy + a10x + a03y^3 + a02y^2 + a01y + a00`$

<font color='gray'>  where $`\rm x = log_{10}([S\,II]/H\alpha)`$ and $`\rm y = log_{10}([O\,III]/H\beta).`$ </font>
<br> <font color='gray'>  In this case if f_SII_OIII(x, y) > 0, the source can be considered as a SNR. </font>

![image](https://github.com/mariakop21/Diagnostics/assets/25170839/68ee05eb-97a9-4ed0-8a10-fcba042bade4)



```python
f_SII_OIII = lambda x, y: (a30*x**3.0 + a21*x**2.0*y + a20*x**2.0 + a12*x*y**2.0 + a11*x*y + 
                           a10*x + a03*y**3.0 + a02*y**2.0 + a01*y + a00)
```

### $`\rm {\bf{[O\,I]/H\alpha - [O\,III]/H\beta}}`$ 
<br> a30 =  0.465
<br> a21 =  0.245
<br> a20 =  -0.432
<br> a12 =  1.067
<br> a11 =  -0.887
<br> a10 =  -0.701
<br> a03 =  0.049
<br> a02 =  -1.610
<br> a01 =  2.096
<br> a00 =  2.710

$`\rm f\_OI\_OIII(x, y) = a30x^3 + a21x^2y + a20x^2 + a12xy^2 + a11xy + a10x + a03y^3 + a02y^2 + a01y + a00`$

<font color='gray'>  where $`\rm x = log_{10}([O\,I]/H\alpha)`$ and $`\rm y = log_{10}([O\,III]/H\beta).`$ </font>
<br> <font color='gray'>  In this case if f_OI_OIII(x, y) > 0, the source can be considered as a SNR. </font>

![image](https://github.com/mariakop21/Diagnostics/assets/25170839/30944b9d-3264-4879-8007-6c75b05e9b81)



```python
f_OI_OIII = lambda x, y: (a30*x**3.0 + a21*x**2.0*y + a20*x**2.0 + a12*x*y**2.0 + a11*x*y + 
                           a10*x + a03*y**3.0 + a02*y**2.0 + a01*y + a00)
```

### $`\rm {\bf{[N\,II]/H\alpha - [O\,I]/H\alpha}}`$ 
<br> a30 =  -2.159
<br> a21 =  4.249
<br> a20 =  -0.874
<br> a12 =  0.067
<br> a11 =  4.330
<br> a10 = -0.0007
<br> a03 =  1.162
<br> a02 =  1.263
<br> a01 =  0.382
<br> a00 =  1.285

$`\rm f\_NII\_OI(x, y) = a30x^3 + a21x^2y + a20x^2 + a12xy^2 + a11xy + a10x + a03y^3 + a02y^2 + a01y + a00`$

<font color='gray'>  where $`\rm x = log_{10}([N\,II]/H\alpha)`$ and $\`rm y = log_{10}([O\,I]/H\alpha).`$ </font>
<br> <font color='gray'>  In this case if f_NII_OI(x, y) > 0, the source can be considered as a SNR. </font>

![image](https://github.com/mariakop21/Diagnostics/assets/25170839/001fde1b-d61c-42b1-b9bf-a2ac0e96c2b4)



```python
f_NII_OI = lambda x, y: (a30*x**3.0 + a21*x**2.0*y + a20*x**2.0 + a12*x*y**2.0 + a11*x*y + 
                           a10*x + a03*y**3.0 + a02*y**2.0 + a01*y + a00)
```

### $`\rm {\bf{[O\,II]/H\beta - [O\,III]/H\beta}}`$ 
<br> a30 =  -0.008
<br> a21 =  0.416
<br> a20 =  1.952
<br> a12 =  -0.616
<br> a11 =  -1.133
<br> a10 =  4.591
<br> a03 =  0.347
<br> a02 =  1.344
<br> a01 =  3.356
<br> a00 =  -2.904

$`\rm f\_OII\_OIII(x, y) = a30x^3 + a21x^2y + a20x^2 + a12xy^2 + a11xy + a10x + a03y^3 + a02y^2 + a01y + a00`$

<font color='gray'>  where $`\rm x = log_{10}([Ο\,II]/H\beta)`$ and $`\rm y = log_{10}([O\,III]/H\beta).`$ </font>
<br> <font color='gray'>  In this case if f_OII_OIII(x, y) > 0, the source can be considered as a SNR. </font>

![image](https://github.com/mariakop21/Diagnostics/assets/25170839/d3163b29-2340-4a2e-993e-5313fb98caf2)



```python
f_OII_OIII = lambda x, y: (a30*x**3.0 + a21*x**2.0*y + a20*x**2.0 + a12*x*y**2.0 + a11*x*y + 
                           a10*x + a03*y**3.0 + a02*y**2.0 + a01*y + a00)
```

### $`\rm {\bf{[N\,II]/H\alpha - [O\,II]/H\beta}}`$ 

<br> a10 =  1.262
<br> a01 =  1.000
<br> a00 =  0.581

$`\rm f\_NII\_OII(x, y) = a10x + a01y + a00`$

<font color='gray'>  where $`\rm x = log_{10}([N\,II]/H\alpha)`$ and $`\rm y = log_{10}([O\,III]/H\beta).`$ </font>
<br> <font color='gray'>  In this case if f_NII_OIII(x, y) > 0, the source can be considered as a SNR. </font>

![image](https://github.com/mariakop21/Diagnostics/assets/25170839/c7f2fc42-595b-426b-8794-e36ad5c9cbd1)



```python
f_NII_OIII = lambda x, y: (a10*x + a01*y + a00)
```

### $`\rm {\bf{[S\,II]/H\alpha - [O\,I]/H\alpha}}`$ 
<br> a30 =  0.461
<br> a21 =  2.197
<br> a20 =  -0.089
<br> a12 =  -1.036
<br> a11 =  1.932
<br> a10 =  -0.449
<br> a03 =  1.446
<br> a02 =  1.371
<br> a01 =  0.145
<br> a00 =  1.218

$`\rm f\_SII\_OI(x, y) = a30x^3 + a21x^2y + a20x^2 + a12xy^2 + a11xy + a10x + a03y^3 + a02y^2 + a01y + a00`$

<font color='gray'>  where $`\rm x = log_{10}([S\,II]/H\alpha)`$ and $`\rm y = log_{10}([O\,I]/H\alpha).`$ </font>
<br> <font color='gray'>  In this case if f_SII_OI(x, y) > 0, the source can be considered as a SNR. </font>

![image](https://github.com/mariakop21/Diagnostics/assets/25170839/ae09a313-c689-4ac1-9831-ed0491736b48)



```python
f_SII_OI = lambda x, y: (a30*x**3.0 + a21*x**2.0*y + a20*x**2.0 + a12*x*y**2.0 + a11*x*y + 
                           a10*x + a03*y**3.0 + a02*y**2.0 + a01*y + a00)
```

### $`\rm {\bf{[O\,I]/H\alpha - [O\,II]/H\beta}}`$ 
<br> a30 =  0.701
<br> a21 =  4.291
<br> a20 =  -0.842
<br> a12 =  0.124
<br> a11 =  3.095
<br> a10 =  0.719
<br> a03 =  0.432
<br> a02 =  -1.170
<br> a01 =  -2.274
<br> a00 =  5.017

$`\rm f\_OI\_OII(x, y) = a30x^3 + a21x^2y + a20x^2 + a12xy^2 + a11xy + a10x + a03y^3 + a02y^2 + a01y + a00`$

<font color='gray'>  where $`\rm x = log_{10}([O\,I]/H\alpha)`$ and $`\rm y = log_{10}([O\,II]/H\beta).`$ </font>
<br> <font color='gray'>  In this case if f_OI_OII(x, y) > 0, the source can be considered as a SNR. </font>

![image](https://github.com/mariakop21/Diagnostics/assets/25170839/5bde01ba-4720-4143-89b2-0f7d19c804dc)



```python
f_OI_OII = lambda x, y: (a30*x**3.0 + a21*x**2.0*y + a20*x**2.0 + a12*x*y**2.0 + a11*x*y + 
                           a10*x + a03*y**3.0 + a02*y**2.0 + a01*y + a00)
```

### $`\rm {\bf{[S\,II]/H\alpha - [O\,II]/H\beta}}`$ 
<br> a30 =  -0.403
<br> a21 =  -0.511
<br> a20 =  -0.575
<br> a12 =  -0.225
<br> a11 =  -0.332
<br> a10 =  4.283
<br> a03 =  1.185
<br> a02 =  0.981
<br> a01 =  -0.283
<br> a00 =  2.777

$`\rm f\_SII\_OII(x, y) = a30x^3 + a21x^2y + a20x^2 + a12xy^2 + a11xy + a10x + a03y^3 + a02y^2 + a01y + a00`$

<font color='gray'>  where $`\rm x = log_{10}([S\,II]/H\alpha)`$ and $`\rm y = log_{10}([O\,II]/H\beta).`$ </font>
<br> <font color='gray'>  In this case if f_SII_OII(x, y) > 0, the source can be considered as a SNR. </font>

![image](https://github.com/mariakop21/Diagnostics/assets/25170839/86109bb8-b5e1-4d72-a970-c31de6a14207)



```python
f_SII_OII = lambda x, y: (a30*x**3.0 + a21*x**2.0*y + a20*x**2.0 + a12*x*y**2.0 + a11*x*y + 
                           a10*x + a03*y**3.0 + a02*y**2.0 + a01*y + a00)
```

### $`\rm {\bf{[N\,II]/H\alpha - [S\,II]/H\alpha - [O\,III]/H\beta}}`$ 
<br> a300 = -2.913
<br> a201 = -0.638
<br> a210 =  1.568
<br> a200 =  0.407
<br> a102 = -0.866
<br> a111 = -2.264
<br> a101 =  1.508
<br> a120 =  1.753
<br> a110 = -6.913
<br> a100 =  0.001
<br> a003 =  1.463
<br> a012 = -1.325
<br> a002 = -2.732
<br> a021 =  1.823
<br> a011 = -2.697
<br> a001 =  4.377
<br> a030 = -1.585 
<br> a020 =  0.770
<br> a010 =  1.267
<br> a000 =  2.413

$`\rm f\_NII\_SII\_OIII(x, y, z) = a300x^3 + a201x^2z + a210x^2y + a200x^2 + a102xz^2 + a111xyz +  a101xz  + a120xy^2 + a110xy    + a100x + a003z^3 + a012yz^2 +  a002z^2 + a021y^2z + a011yz + a001z    + a030y^3   + a020y^2+  a010y + a000`$

<font color='gray'>  where $`\rm x = log_{10}([N\,II]/H\alpha)`$, $`\rm y = log_{10}([S\,II]/H\alpha)`$, and $`\rm z = log_{10}([O\,III]/H\beta).`$ </font>
<br> <font color='gray'> If f_NII_SII_OIII(x, y) > 0, the source can be considered as a SNR. </font>

![image](https://github.com/mariakop21/Diagnostics/assets/25170839/1d6cfa19-9515-4b3a-aeb9-8358af887fd3)



```python
f_NII_SII_OIII = lambda x, y, z:(a300*x**3 + a201*x**2*z + a210*x**2*y + a200*x**2 + a102*x*z**2 + a111*x*y*z + 
                                 a101*x*z + a120*x*y**2 + a110*x*y + a100*x + a003*z**3 + a012*y*z**2 + 
                                 a002*z**2 + a021*y**2*z + a011*y*z + a001*z + a030*y**3 + a020*x*y**2+  
                                 a010*y + a000)
```

### $`\rm {\bf{[N\,II]/H\alpha - [S\,II]/H\alpha - [O\,I]/H\alpha}}`$ 
<br> a300 = 0.025
<br> a201 =  0.253
<br> a210 =  0.250
<br> a200 =  -0.350
<br> a102 =  0.196
<br> a111 = 0.379
<br> a101 =  0.149
<br> a120 =  0.127
<br> a110 = -0.795
<br> a100 =  -1.821
<br> a003 =  0.223
<br> a012 =  0.014
<br> a002 = -0.804
<br> a021 =  -0.021
<br> a011 =  0.658
<br> a001 =  0.214
<br> a030 = -0.002 
<br> a020 =  0.151
<br> a010 =  -1.822
<br> a000 =  2.382

$`\rm f\_NII\_SII\_OI(x, y, z) = a300x^3 + a201x^2z + a210x^2y + a200x^2 + a102xz^2 + a111xyz +  a101xz  + a120xy^2 + a110xy    + a100x + a003z^3 + a012yz^2 +  a002z^2 + a021y^2z + a011yz + a001z    + a030y^3   + a020y^2+  a010y + a000`$

<font color='gray'>  where $`\rm x = log_{10}([N\,II]/H\alpha)`$, $`\rm y = log_{10}([S\,II]/H\alpha)`$, and $`\rm z = log_{10}([O\,I]/H\alpha).`$ </font>
<br> <font color='gray'> If f_NII_SII_OI(x, y) > 0, the source can be considered as a SNR. </font>

![image](https://github.com/mariakop21/Diagnostics/assets/25170839/1bffb43e-6300-4f27-8779-a8983c20fea3)



```python
f_NII_SII_OI = lambda x, y, z:(a300*x**3 + a201*x**2*z + a210*x**2*y + a200*x**2 + a102*x*z**2 + a111*x*y*z + 
                                 a101*x*z + a120*x*y**2 + a110*x*y + a100*x + a003*z**3 + a012*y*z**2 + 
                                 a002*z**2 + a021*y**2*z + a011*y*z + a001*z + a030*y**3 + a020*x*y**2+  
                                 a010*y + a000)
```

### $`\rm {\bf{[N\,II]/H\alpha - [S\,II]/H\alpha - [O\,II]/H\beta}}`$ 
<br> a300 = -0.140
<br> a201 = -0.388
<br> a210 =  0.231
<br> a200 =  1.460
<br> a102 =  0.067
<br> a111 = -0.460
<br> a101 =  2.639
<br> a120 =  0.283
<br> a110 = -2.699
<br> a100 = -0.610
<br> a003 =  0.361
<br> a012 =  0.141
<br> a002 =  0.283
<br> a021 =  0.098
<br> a011 = -1.050
<br> a001 =  1.626
<br> a030 = -0.055 
<br> a020 = -0.038
<br> a010 =  2.202
<br> a000 =  1.520

$`\rm f\_NII\_SII\_OII(x, y, z) = a300x^3 + a201x^2z + a210x^2y + a200x^2 + a102xz^2 + a111xyz +  a101xz  + a120xy^2 + a110xy    + a100x + a003z^3 + a012yz^2 +  a002z^2 + a021y^2z + a011yz + a001z    + a030y^3   + a020y^2+  a010y + a000`$

<font color='gray'>  where $`\rm x = log_{10}([N\,II]/H\alpha)`$, $`\rm y = log_{10}([S\,II]/H\alpha)`$, and $`\rm z = log_{10}([O\,II]/H\beta).`$ </font>
<br> <font color='gray'> If f_NII_SII_OII(x, y) > 0, the source can be considered as a SNR. </font>

![image](https://github.com/mariakop21/Diagnostics/assets/25170839/fd66ec83-5eb3-4b64-bca1-84dbbc2b6f98)



```python
f_NII_SII_OII = lambda x, y, z:(a300*x**3 + a201*x**2*z + a210*x**2*y + a200*x**2 + a102*x*z**2 + a111*x*y*z + 
                                 a101*x*z + a120*x*y**2 + a110*x*y + a100*x + a003*z**3 + a012*y*z**2 + 
                                 a002*z**2 + a021*y**2*z + a011*y*z + a001*z + a030*y**3 + a020*x*y**2+  
                                 a010*y + a000)
```

### $`\rm {\bf{[N\,II]/H\alpha - [O\,II]/H\beta - [O\,III]/H\beta}}`$ 
<br> a300 = -1.704
<br> a201 = -0.879
<br> a210 =  8.080
<br> a200 =  -1.549
<br> a102 =  -3.772
<br> a111 = -0.877
<br> a101 =  0.788
<br> a120 =  -0.372
<br> a110 =  3.313
<br> a100 =  7.034
<br> a003 =  3.011
<br> a012 =  -2.641
<br> a002 =  -2.798
<br> a021 =  1.264
<br> a011 = -1.968
<br> a001 =  5.176
<br> a030 = 0.576 
<br> a020 =  2.729
<br> a010 =  -1.199
<br> a000 =  3.478

$`\rm f\_NII\_OII\_OIII(x, y, z) = a300x^3 + a201x^2z + a210x^2y + a200x^2 + a102xz^2 + a111xyz +  a101xz  + a120xy^2 + a110xy    + a100x + a003z^3 + a012yz^2 +  a002z^2 + a021y^2z + a011yz + a001z    + a030y^3   + a020y^2+  a010y + a000`$

<font color='gray'>  where $`\rm x = log_{10}([N\,II]/H\alpha)`$, $`\rm y = log_{10}([O\,II]/H\beta)`$, and $`\rm z = log_{10}([O\,III]/H\beta).`$ </font>
<br> <font color='gray'> If f_NII_SII_OII(x, y) > 0, the source can be considered as a SNR. </font>

![image](https://github.com/mariakop21/Diagnostics/assets/25170839/9cf22ed1-abf0-42a4-b4da-173f75820306)



```python
f_NII_OII_OIII = lambda x, y, z:(a300*x**3 + a201*x**2*z + a210*x**2*y + a200*x**2 + a102*x*z**2 + a111*x*y*z + 
                                 a101*x*z + a120*x*y**2 + a110*x*y + a100*x + a003*z**3 + a012*y*z**2 + 
                                 a002*z**2 + a021*y**2*z + a011*y*z + a001*z + a030*y**3 + a020*x*y**2+  
                                 a010*y + a000)
```

### $`\rm {\bf{[N\,II]/H\alpha - [O\,I]/H\alpha - [O\,II]/H\beta}}`$ 
<br> a300 = -1.085
<br> a201 = -0.268
<br> a210 =  3.986
<br> a200 =  0.863
<br> a102 =  4.071
<br> a111 = -2.792
<br> a101 =  3.889
<br> a120 =  0.609
<br> a110 =  6.108
<br> a100 =  -3.186
<br> a003 =  0.139
<br> a012 =  -0.459
<br> a002 =  -0.768
<br> a021 =  4.849
<br> a011 = 1.608
<br> a001 =  -1.437
<br> a030 = 0.326 
<br> a020 =  -2.053
<br> a010 =  1.578
<br> a000 =  3.734

$`\rm f\_NII\_OI\_OII(x, y, z) = a300x^3 + a201x^2z + a210x^2y + a200x^2 + a102xz^2 + a111xyz +  a101xz  + a120xy^2 + a110xy    + a100x + a003z^3 + a012yz^2 +  a002z^2 + a021y^2z + a011yz + a001z    + a030y^3   + a020y^2+  a010y + a000`$

<font color='gray'>  where $\rm x = log_{10}([N\,II]/H\alpha)$, $\rm y = log_{10}([O\,I]/H\alpha)$, and $\rm z = log_{10}([O\,II]/H\beta).$ </font>
<br> <font color='gray'> If f_NII_OI_OII(x, y) > 0, the source can be considered as a SNR. </font>

![image](https://github.com/mariakop21/Diagnostics/assets/25170839/e53629f9-678c-4dee-ad23-c3e9ba803ffc)



```python
f_NII_OI_OII = lambda x, y, z:(a300*x**3 + a201*x**2*z + a210*x**2*y + a200*x**2 + a102*x*z**2 + a111*x*y*z + 
                                 a101*x*z + a120*x*y**2 + a110*x*y + a100*x + a003*z**3 + a012*y*z**2 + 
                                 a002*z**2 + a021*y**2*z + a011*y*z + a001*z + a030*y**3 + a020*x*y**2+  
                                 a010*y + a000)
```

### $`\rm {\bf{[N\,II]/H\alpha - [O\,I]/H\alpha - [O\,III]/H\beta}}`$ 
<br> a300 = -1.082
<br> a201 =  0.195
<br> a210 =  1.873
<br> a200 =  0.027
<br> a102 =  2.230
<br> a111 = -3.680
<br> a101 = -0.428
<br> a120 =  1.281
<br> a110 =  2.433
<br> a100 =  -1.752
<br> a003 =  1.842
<br> a012 =  1.837
<br> a002 =  -1.213
<br> a021 =  0.477
<br> a011 = -2.307
<br> a001 =  1.400
<br> a030 = 0.590 
<br> a020 =  0.386
<br> a010 =  -0.862
<br> a000 =  0.567

$`\rm f\_NII\_OI\_OIII(x, y, z) = a300x^3 + a201x^2z + a210x^2y + a200x^2 + a102xz^2 + a111xyz +  a101xz  + a120xy^2 + a110xy    + a100x + a003z^3 + a012yz^2 +  a002z^2 + a021y^2z + a011yz + a001z + a030y^3   + a020y^2+  a010y + a000`$

<font color='gray'>  where $`\rm x = log_{10}([N\,II]/H\alpha)`$, $`\rm y = log_{10}([O\,I]/H\alpha)`$, and $`\rm z = log_{10}([O\,III]/H\beta).`$ </font>
<br> <font color='gray'> If f_NII_OI_OIII(x, y) > 0, the source can be considered as a SNR. </font>

![image](https://github.com/mariakop21/Diagnostics/assets/25170839/d316bcd2-498e-4b78-b80b-a4dc3650ee9b)



```python
f_NII_OI_OIII = lambda x, y, z:(a300*x**3 + a201*x**2*z + a210*x**2*y + a200*x**2 + a102*x*z**2 + a111*x*y*z + 
                                 a101*x*z + a120*x*y**2 + a110*x*y + a100*x + a003*z**3 + a012*y*z**2 + 
                                 a002*z**2 + a021*y**2*z + a011*y*z + a001*z + a030*y**3 + a020*x*y**2+  
                                 a010*y + a000)
```

### $`\rm {\bf{[S\,II]/H\alpha - [O\,I]/H\alpha - [O\,II]/H\beta}}`$ 
<br> a300 = 0.042
<br> a201 = -1.707
<br> a210 =  0.359
<br> a200 =  -0.172
<br> a102 =  0.762
<br> a111 = -2.236
<br> a101 =  1.342
<br> a120 =  -0.096
<br> a110 =  2.439
<br> a100 =  -2.305
<br> a003 =  0.266
<br> a012 =  -0.094
<br> a002 =  -0.747
<br> a021 =  5.000
<br> a011 = 2.587
<br> a001 =  -1.758
<br> a030 = 0.826 
<br> a020 =  -1.274
<br> a010 =  1.213
<br> a000 =  4.108

$`\rm f\_SII\_OI\_OII(x, y, z) = a300x^3 + a201x^2z + a210x^2y + a200x^2 + a102xz^2 + a111xyz +  a101xz  + a120xy^2 + a110xy    + a100x + a003z^3 + a012yz^2 +  a002z^2 + a021y^2z + a011yz + a001z    + a030y^3   + a020y^2+  a010y + a000`$

<font color='gray'>  where $`\rm x = log_{10}([S\,II]/H\alpha)`$, $`\rm y = log_{10}([O\,I]/H\alpha)`$, and $`\rm z = log_{10}([O\,III]/H\beta).`$ </font>
<br> <font color='gray'> If f_SII_OI_OII(x, y) > 0, the source can be considered as a SNR. </font>

![image](https://github.com/mariakop21/Diagnostics/assets/25170839/b6a76454-64f6-4096-8016-359831455cbe)



```python
f_SII_OI_OII = lambda x, y, z:(a300*x**3 + a201*x**2*z + a210*x**2*y + a200*x**2 + a102*x*z**2 + a111*x*y*z + 
                                 a101*x*z + a120*x*y**2 + a110*x*y + a100*x + a003*z**3 + a012*y*z**2 + 
                                 a002*z**2 + a021*y**2*z + a011*y*z + a001*z + a030*y**3 + a020*x*y**2+  
                                 a010*y + a000)
```

### $`\rm {\bf{[S\,II]/H\alpha - [O\,II]/H\beta - [O\,III]/H\beta}}`$ 
<br> a300 =  -0.151
<br> a201 =  -0.501
<br> a210 =   0.713
<br> a200 =  -3.181
<br> a102 =  -0.304
<br> a111 =   1.194
<br> a101 =  -0.421
<br> a120 =  -1.869
<br> a110 =   2.946
<br> a100 =   3.761
<br> a003 =   2.156
<br> a012 =  -0.354
<br> a002 =  -3.318
<br> a021 =   1.078
<br> a011 =   1.088
<br> a001 =   4.722
<br> a030 =   2.269 
<br> a020 =   1.467
<br> a010 =  -3.676
<br> a000 =   4.974

$`\rm f\_SII\_OII\_OIII(x, y, z) = a300x^3 + a201x^2z + a210x^2y + a200x^2 + a102xz^2 + a111xyz +  a101xz  + a120xy^2 + a110xy    + a100x + a003z^3 + a012yz^2 +  a002z^2 + a021y^2z + a011yz + a001z    + a030y^3   + a020y^2+  a010y + a000`$

<font color='gray'>  where $`\rm x = log_{10}([S\,II]/H\alpha)`$, $`\rm y = log_{10}([O\,II]/H\beta)`$, and $`\rm z = log_{10}([O\,III]/H\beta).`$ </font>
<br> <font color='gray'> If f_SII_OII_OIII(x, y) > 0, the source can be considered as a SNR. </font>

![image](https://github.com/mariakop21/Diagnostics/assets/25170839/1cc48fbf-aa7d-4a9f-a576-e7a1b39f0a21)



```python
f_SII_OII_OIII = lambda x, y, z:(a300*x**3 + a201*x**2*z + a210*x**2*y + a200*x**2 + a102*x*z**2 + a111*x*y*z + 
                                 a101*x*z + a120*x*y**2 + a110*x*y + a100*x + a003*z**3 + a012*y*z**2 + 
                                 a002*z**2 + a021*y**2*z + a011*y*z + a001*z + a030*y**3 + a020*x*y**2+  
                                 a010*y + a000)
```

### $`\rm {\bf{[S\,II]/H\alpha - [O\,I]/H\alpha - [O\,III]/H\beta}}`$ 
<br> a300 =  -0.598
<br> a201 =   0.403
<br> a210 =  -0.896
<br> a200 =   0.873
<br> a102 =  -1.329
<br> a111 =  -3.664
<br> a101 =   1.687
<br> a120 =   1.766
<br> a110 =   0.285
<br> a100 =  -1.227
<br> a003 =   1.874
<br> a012 =   2.312
<br> a002 =  -1.495
<br> a021 =   1.356
<br> a011 =  -1.854
<br> a001 =   1.197
<br> a030 =   0.696 
<br> a020 =   0.815
<br> a010 =  -1.357
<br> a000 =   0.303

$`\rm f\_SII\_OI\_OIII(x, y, z) = a300x^3 + a201x^2z + a210x^2y + a200x^2 + a102xz^2 + a111xyz +  a101xz  + a120xy^2 + a110xy    + a100x + a003z^3 + a012yz^2 +  a002z^2 + a021y^2z + a011yz + a001z    + a030y^3   + a020y^2+  a010y + a000`$

<font color='gray'>  where $`\rm x = log_{10}([S\,II]/H\alpha)`$, $`\rm y = log_{10}([O\,I]/H\alpha)`$, and $`\rm z = log_{10}([O\,III]/H\beta).`$ </font>
<br> <font color='gray'> If f_SII_OI_OIII(x, y) > 0, the source can be considered as a SNR. </font>

![image](https://github.com/mariakop21/Diagnostics/assets/25170839/ae47bfd1-6260-48cf-bfc6-3e38a9f10443)



```python
f_SII_OI_OIII = lambda x, y, z:(a300*x**3 + a201*x**2*z + a210*x**2*y + a200*x**2 + a102*x*z**2 + a111*x*y*z + 
                                 a101*x*z + a120*x*y**2 + a110*x*y + a100*x + a003*z**3 + a012*y*z**2 + 
                                 a002*z**2 + a021*y**2*z + a011*y*z + a001*z + a030*y**3 + a020*x*y**2+  
                                 a010*y + a000)
```

### $`\rm {\bf{[O\,I]/H\alpha - [O\,II]/H\beta - [O\,III]/H\beta}}`$ 
<br> a300 =   0.768
<br> a201 =  -0.419
<br> a210 =   1.134
<br> a200 =  -0.166
<br> a102 =   1.842
<br> a111 =  -2.650
<br> a101 =  -0.174
<br> a120 =  -1.075
<br> a110 =   0.932
<br> a100 =  -0.871
<br> a003 =   0.964
<br> a012 =  -0.771
<br> a002 =  -1.476
<br> a021 =   0.185
<br> a011 =   2.248
<br> a001 =   0.824
<br> a030 =   0.452 
<br> a020 =  -0.554
<br> a010 =  -2.228
<br> a000 =   3.070

$`\rm f\_OI\_OII\_OIII(x, y, z) = a300x^3 + a201x^2z + a210x^2y + a200x^2 + a102xz^2 + a111xyz +  a101xz  + a120xy^2 + a110xy    + a100x + a003z^3 + a012yz^2 +  a002z^2 + a021y^2z + a011yz + a001z    + a030y^3   + a020y^2+  a010y + a000`$

<font color='gray'>  where $`\rm x = log_{10}([O\,I]/H\alpha)`$, $`\rm y = log_{10}([O\,II]/H\beta)`$, and $`\rm z = log_{10}([O\,III]/H\beta).`$ </font>
<br> <font color='gray'> If f_OI_OII_OIII(x, y) > 0, the source can be considered as a SNR. </font>


![image](https://github.com/mariakop21/Diagnostics/assets/25170839/840ff838-65b5-4540-aca0-4705d898118f)


```python
f_OI_OII_OIII = lambda x, y, z:(a300*x**3 + a201*x**2*z + a210*x**2*y + a200*x**2 + a102*x*z**2 + a111*x*y*z + 
                                 a101*x*z + a120*x*y**2 + a110*x*y + a100*x + a003*z**3 + a012*y*z**2 + 
                                 a002*z**2 + a021*y**2*z + a011*y*z + a001*z + a030*y**3 + a020*x*y**2+  
                                 a010*y + a000)
```

