# Input to DYNMOD

[TOC]



# General Information {#dynmod_general_information}

The input description to the `DYNMOD` module is divided into 5 sections,
each section describing one data-section referred to as A-E.

- Data Group A: [Control Information](@ref dynmod_a)
- Data Group B: [Free Vibration Analysis](@ref dynmod_b)
- Data Group C: [Regular Wave, Time Domain Analysis](@ref dynmod_c)
- Data Group D: [Irregular Wave, Time Domain Analysis](@ref dynmod_d)
- Data Group E: [Time Domain Procedure and File Storage Parameters](@ref dynmod_e)

Three different types of analysis are possible. Complete input for these
types is shown in the list below.

- Type number 1, Free vibration, requires the data sections A and B.
- Type number 2, Regular wave, requires the data sections A, C and E.
- Type number 3, Irregular wave, requires the data sections A, D and E.



# Data Group A: Control Information {#dynmod_a}

This data-group is mandatory for all types of analysis with `DYNMOD`. The
prescribed sequence must be followed.



## Principal run parameters {#dynmod_a_principal}



### Data group identifier, one input line {#dynmod_a_principal_data}

~~~
DYNMod CONTrol INFOrmation CHVERS
~~~

- `CHVERS: character(8)`: RIFLEX input file version, e.g. 3.2



### Heading, three input lines {#dynmod_a_principal_heading}

- Heading, line no 1
- Heading, line no 2
- Heading, line no 3

Identification of the run by alphanumerical text

Always three input lines which may all be blank. Each line may contain up to 60 characters



### Options and identifiers, one input line {#dynmod_a_principal_options}

~~~
IRUNCO IANAL IDRIS IDENV IDSTAT IDIRR IDRES
~~~

- `IRUNCO: character(4), default: DATA`: Code for data check or executable run
    - `= FREM`: Data generation for `FREMOD`
    - `= DATA`: Data check
    - `= ANALysis`: Analysis
- `IANAL: character(4)`: Type of analysis to be performed
    - `= EIGEn`: Eigenvalue analysis.
        - Data section B must be given
    - `= REGUlar`: Regular wave, time domain analysis.
        - Data sections C and E must be given.
    - `= IRREgular`: Irregular wave, time domain analysis.
        - Data sections D and E must be given.
- `IDRIS: character(6)`: Data set identifier corresponding to data for one riser system
established by `INPMOD` and followed by a static analysis. See
[INPMOD: Data Group B: Single Riser Data](@ref inpmod_data_group_b_single_riser_data) and
[STAMOD: Options and print switches](@ref stamod_a_principal_options).
- `IDENV: character(6)`: Environment identifier, corresponding to data for one environment on
file established by `INPMOD`. See data-group [INPMOD: Identification of the environment](@ref inpmod_d_identification) of
input description for `INPMOD`.
    - Reference to actual wave case is given in a later data-group
    - Dummy for `IRUNCO=DATAcheck`
- `IDSTAT: character(6)`: Static condition identifier, corresponding to data on file established
by `STAMOD`. See [STAMOD: Principal run parameters](@ref stamod_a_principal) of input description for `STAMOD`.
- `IDIRR: character(6)`: Data set identifier for irregular wave and motion data, either
established by a previous run or used as reference to results stored on file by this run.
- `IDRES: character(6)`: Data set identifier for this run, used as reference to results stored on files



## Static load condition {#dynmod_a_static}

For special purposes it may be convenient to change applied static loads
at the start of dynamic analysis. This option should be used with care!
One useful application is for analysing free vibration after scaling a
static nodal force to zero (`SCALSF=0.0`).

Note that some static loads are applied and some modelling features are activated in dynamic analysis 
even if they were not applied nor activated in static analysis. See 
also [Note: Static Analysis with Fixed Parameters and Parameter Variation](@ref stamod_gen_comment).


### Data group identifier, one input line {#dynmod_a_static_data}

~~~
STATic LOAD CONDition
~~~



### Scaling parameters, one line {#dynmod_a_static_scaling}

~~~
SCALVF SCALSF SCALCF
~~~

- `SCALVF: real, default: 1`: Scaling of volume forces
- `SCALSF: real, default: 1`: Scaling of specified (nodal) forces
- `SCALCF: real, default: 1`: Scaling of current velocities

All forces are scaled simultaneously as \f$ \mathrm{ F_s = SCALiF \times F_s^0 }\f$
Only `SCALSF` is active in the present version of the program.



## Random number generator {#dynmod_a_random}

In version 4.18 and later, the algorithm for generating pseudo-random
numbers may be selected by the user. The "mersenne twister" is the
recommended method and should be used unless backwards compatibility
with previous versions is required. Note that the default value may
change in a future release. The choice of random number generator will
apply to:
- generation of irregular wave time series
- initial phase angles for time domain VIV loads specified for cross-sections in INPMOD
- generation of phase angles for application of harmonic loads from a VIVANA frequency domain analysis.

It has been identified that the legacy method can give non-gaussian
and non-stationary wave elevation in SIMO for short crested waves with
more than about 30-50 discrete directions, depending on wave spectrum
and simulation duration. By choosing the mersenne twister, these
issues are avoided.

For coupled analysis, wave time series will be generated using the
random number generator specified in SIMA.


### Data group identifier, one input line {#dynmod_a_random_iden}

~~~
RANDom NUMBer GENErator
~~~


### Random number generator input, one line {#dynmod_a_random_input}

~~~
CHRAN  ISEED
~~~

- `CHRAN: character (7), default: LEGACY`: Choice of random number generator
    - `= 'LEGACY'`: Legacy random number generator used. Results will be consistent with previous RIFLEX versions.
    - `= 'TWISTER'`: Mersenne Twister' random number generator used. Results will NOT be consistent with previous RIFLEX versions.
- `ISEED: integer, default: 7`: Starting parameter of random number generator for use when input of starting value is not available; e.g. time domain VIV loads. Currently not used.



# Data Group B: Free Vibration Analysis {#dynmod_b}

This data-group is given if and only if `IANAL=EIGEn`, see [Options and identifiers, one input line](@ref dynmod_a_principal_options).



## Free vibration options {#dynmod_b_free}



### Data group identifier, one input line {#dynmod_b_free_data}

~~~
FREE VIBRation OPTIons
~~~



### Number of eigenvalues and -vectors, one input line {#dynmod_b_free_number}

~~~
NEIG NVEC
~~~

- `NEIG: integer`: Number of eigenvalues to be calculated and stored on file
- `NVEC: integer`: Number of eigenvectors to be calculated and stored on file



### Computation parameters, one input line {#dynmod_b_free_computation}

The parameters below correspond to Lanczos' method for solution of
eigenvalue problems. For a detailed discussion, see
 B. Nour-Omid, B.N. Parlett, R.L. Taylor: Lanczos versus Subspace
Iteration for Solution of Eigenvalue Problems, International Journal for
Numerical Methods in Engineering, Vol. 19, pp. 859-871, 1983.
 or B.N. Parlett: The Symmetric Eigenvalue Problem, Prentice-Hall, 1980.

~~~
EPS1 EPS2 EPS3 KSR MAXIT KEX SHIFT MAXNIV
~~~

- `EPS1: real, default: 0`: Maximum acceptable relative error in computed eigenvalues
- `EPS2: real, default: 0`: Limit value for singularity test during factorization
- `EPS3: real, default: 0`: Orthogonality limit:
    - If \f$ \mathrm{ \boldsymbol{\mathrm{v}}_i \, ^T \boldsymbol{\mathrm{v}}_i = \delta_{ii} }\f$ and
    \f$ \mathrm{ \boldsymbol{\mathrm{v}}_i\,^T \boldsymbol{\mathrm{v}}_j = \delta_{ij} }\f$
    and \f$ \mathrm{| \delta_{ij} | < EPS3 \times \delta_{ii} }\f$, \f$ \mathrm{ \quad\boldsymbol{\mathrm{v}}_i } \f$
    and \f$ \mathrm{ \boldsymbol{\mathrm{v}}_j }\f$ are orthogonal
- `KSR: integer, default: 1`: Start vector code:
    - `KSR = `\f$ \pm \f$` 1`: a pseudo-random start vector is generated by the eigenvalue solver
    - `KSR = `\f$ \pm \f$` 2`: the diagonal of the mass matrix is used as start vector
    - `KSR = `\f$ \pm \f$` 3`: a start vector of unit elements is used
    - For positive `KSR` the start vector is premultiplied with **H** before use;
if a negative value is specified the start vector is used directly.
- `MAXIT: integer, default: 5`: Maximum no of iterations in reorthogonalization.
    - If a negative value is specified, reorthogonalization is not iterative; e.g. `MAXIT = -2` will
cause a two-pass Gram-Smith orthogonalization to be employed to all new \f$ \mathrm{ \boldsymbol{\mathrm{ v_{}}}_i } \f$ (i\>1),
irrespective of `EPS3`.
    - For high values of `NEIG` (>50) a doublepass orthogonalization is recommended (`MAXIT = -2`)
- `KEX: integer, default: 0`: Parameter controlling the frequency with which the small tridiagonal eigenvalue problem is solved.
    - Must be in the range of `0 <= KEX <= 5`.
    - If a zero value is specified, a default value of 2 is used
- `SHIFT: real, default: 0`: The shift value \f$ \sigma \f$
- `MAXNIV: integer, default: 0`: Number of Lanczos steps to be used.
    - A default value suitable for the eigenvalue routines is automatically computed if a `0` is specified.
    - `MAXNIV` should only be given a value \f$ \neq \f$ `0` for small problems

If zero or negative values are specified for `EPS1-EPS3` default
values are inserted



## Print options for results {#dynmod_b_print}



### Data group identifier, one input line {#dynmod_b_print_data}

~~~
EIGEnvalue PRINt OPTIons
~~~



### Print selection parameters, one input line {#dynmod_b_print_selection}

~~~
NPEIG NPVEC IPRESW
~~~

- `NPEIG: integer`: Number of eigenvalues to be printed ( <= `NEIG`)
- `NPVEC: integer`: Number of eigenvectors to be printed ( <= `NVEC`)
- `IPRESW: integer, default: 0`: Debug print switch for eigenvalue routines



## Termination of input data {#dynmod_b_termination}

To terminate an input data stream, simply give the following, which is
interpreted as a data group identifier.

~~~
END
~~~

Note that the `END` image cannot be omitted



# Data Group C: Regular Wave, Time Domain Analysis {#dynmod_c}

This data group is given for `IANAL = REGUlar`, see [Options and identifiers, one input line](@ref dynmod_a_principal_options).
Data-group A and E must also be given for complete definition of a regular time domain analysis.



## Parameters for definition of analysis and further input {#dynmod_c_parameters}



### Data group identifier, one input line {#dynmod_c_parameters_data}

~~~
REGUlar WAVE ANALysis
~~~



### Analysis parameters, one input line {#dynmod_c_parameters_analysis}

~~~
NPER NSTPPR IRWCN IMOTD
~~~

- `NPER: integer`: Number of periods for regular wave analysis, referring to wave or motion
periods (of first vessel)
- `NSTPPR: integer, default: 80`: Number of integration time steps per period, recommended value: 50-120
- `IRWCN: integer`: Wave parameter
    - `IRWCN = 0`: No wave acting, motions must be present
    - `IRWCN = N`: Wave acting. Regular wave case N on actual environment used
in present analysis
    - If no waves are acting, the period for harmonic motions is specified in
[Motion amplitudes of support vessel, one input line](@ref dynmod_c_regular_definition_motion_amplitudes)
- `IMOTD: integer`: Platform motion parameter
    - `IMOTD = 0`: No motions, waves must be present
    - `IMOTD = 1`: Platform motion generated on the basis of wave data (wave
period and amplitude) and motion transfer functions. Reference to
transfer functions given in [Options and identifiers, one input line](@ref dynmod_a_principal_options).
    - `IMOTD = 2`: Platform motions specified in [Regular vessel motion](@ref dynmod_c_regular)

The platform motions are independent of the wave loading
parameters given in [Load modelling, regular waves](@ref dynmod_c_load).

Extreme values of response parameters from last integration period
will normally be stored on file (cfr. [File storage of displacement response](@ref dynmod_e_displacement)). In
addition, displacement histories from selected nodes and force and
curvature histories from selected elements can be stored if wanted.
Specification of such data storage is given in data groups
[File storage of displacement response](@ref dynmod_e_displacement), [File storage for internal forces](@ref dynmod_e_internal) and
[File storage for curvature response](@ref dynmod_e_curvature).



## Load modelling, regular waves {#dynmod_c_load}

This data group is given if `IRWCN >= 1` (data group [Analysis parameters, one input line](@ref dynmod_c_parameters_analysis) above).



### Data group identifier, one input line {#dynmod_c_load_data}

~~~
REGUlar WAVE LOADing
~~~



### Method for wave load calculation, one input line {#dynmod_c_load_method}

~~~
IWTYP ISURF IUPPOS
~~~

- `IWTYP: integer, default: 1`: Wave theory parameter
    - `IWTYP = 1`: Airy linear wave theory
    - `IWTYP = 2`: Stoke 5th order wave theory
- `ISURF: integer, default: 1`: Sea surface definition, see the figure 'Definition of sea surface' below.
    - Dummy if `IWTYP = 2`
    - `ISURF = 1`: Integration of wave forces to mean water level
    - `ISURF = 2`: Integration of wave forces to wave surface, deformation of
potential by stretching and compression
    - `ISURF = 3`: Integration of wave forces to wave surface, move of potential
to actual surface
    - `ISURF = 4`: Integration of wave forces to wave surface by keeping the
potential constant from mean water level to wave surface
- `IUPPOS: integer, default: 2`: Riser position parameter
    - `IUPPOS = 0`: as 1, but the riser is kept fixed in static position, for
computation of surface penetrating element. I.e. a node that is wet or dry
at the end of the static analysis will continue to be considered wet or dry
with regards to kinematics in the dynamic simulation. Recommended only for
comparison with linear methods.
    - `IUPPOS = 1`: Wave induced velocities and accelerations calculated at
static riser position
    - `IUPPOS = 2`: Wave induced velocities and accelerations calculated at
updated (dynamic) positions

Note: The option `IUPPOS = 0` cannot be combined with linear analysis, `ITDMET = 1`, or nonlinear analysis, `ITDMET = 2` and `SIMO` bodies.

![Definition of sea surface](@ref figures/um_id_fig203.svg)
@image latex figures/um_id_fig203.pdf "Definition of sea surface" width=12cm



## Regular vessel motion {#dynmod_c_regular}

This data group is given only if `IMOTD=2` (see input group [Analysis parameters, one input line](@ref dynmod_c_parameters_analysis)).



### Data group identifier, one input line {#dynmod_c_regular_data}

~~~
REGUlar VESSel MOTIon
~~~



### Definition of vessel motion, two lines for each vessel {#dynmod_c_regular_definition}

'Motion amplitudes of support vessel' and 'Motion phase angles' must be given for all `NVES` vessels in systems (totally 2x`NVES` lines).



#### Motion amplitudes of support vessel, one input line {#dynmod_c_regular_definition_motion_amplitudes}

Forced displacements are specified for the support vessel. Forced
displacements for the terminal points are found by transformations.

~~~
XAMP YAMP ZAMP XRAMP YRAMP ZRAMP PER
~~~

- `XAMP: real`: Motion amplitude, global x-direction \f$ \mathrm{[L]}\f$
- `YAMP: real`: Motion amplitude, global y-direction \f$ \mathrm{[L]}\f$
- `ZAMP: real`: Motion amplitude, global z-direction \f$ \mathrm{[L]}\f$
- `XRAMP: real`: Motion amplitude, global x-rotation \f$ \mathrm{[degrees]}\f$
- `YRAMP: real`: Motion amplitude, global y-rotation \f$ \mathrm{[degrees]}\f$
- `ZRAMP: real`: Motion amplitude, global z-rotation \f$ \mathrm{[degrees]}\f$
- `PER: real`: Period of motion \f$ \mathrm{[T]}\f$

`PER` is dummy input if a regular wave is specified, i.e. `IRWCN > 0`
(data group 
[Analysis parameters](@ref dynmod_c_parameters_analysis)).  
In the case of multiple vessels, `PER` is only read for the first
vessel and the specified period used for all vessels.


#### Motion phase angles, one input line {#dynmod_c_regular_definition_motion_angles}

~~~
XPHA YPHA ZPHA XRPHA YRPHA ZRPHA
~~~

- `XPHA: real`: Phase angle, x-motion \f$ \mathrm{[degrees]}\f$
- `YPHA: real`: Phase angle, y-motion \f$ \mathrm{[degrees]}\f$
- `ZPHA: real`: Phase angle, z-motion \f$ \mathrm{[degrees]}\f$
- `XRPHA: real`: Phase angle, x-rotation \f$ \mathrm{[degrees]}\f$
- `YRPHA: real`: Phase angle, y-rotation \f$ \mathrm{[degrees]}\f$
- `ZRPHA: real`: Phase angle, z-rotation \f$ \mathrm{[degrees]}\f$

All phase angles are defined as follows:

Positive angle: Forward phase shift; motion before sea surface at global origin.

Surface: \f$ \mathrm{\eta = \eta_a sin(\omega t + \phi_p), \quad \phi_p = -kxcos(\beta) - kysin(\beta)  }\f$

Motion: \f$ \mathrm{x_i = x_{ai}sin(\omega t + \phi_i)}\f$

Where:
- \f$ \mathrm{x_i}\f$ is equation of motion
- \f$ \mathrm{\eta_a}\f$ is wave amplitude
- \f$ \mathrm{x_{ai}}\f$ is motion amplitude `XAMP`, `YAMP`, etc.
- \f$ \mathrm{\phi_i}\f$ is phase angle, `XPHA`, `YPHA`, etc.
- \f$ \mathrm{k}\f$ is wave number
- \f$ \mathrm{\omega}\f$ is angular frequency
- \f$ \mathrm{x, y}\f$ is global coordinates

If the forward phase shift \f$ \mathrm{\phi_i^{xy}}\f$
between wave and motion at the same point (x,y) is known, the
phase into `RIFLEX` must be modified as follows:

\f$ \mathrm{\phi_i = \phi_i^{xy} + \phi_p}\f$

in order to obtain phase relation between motion at (x,y) and a wave
with start at global origin as defined above.



# Data Group D: Irregular Wave, Time Domain Analysis {#dynmod_d}

This data group is given for `IANAL=IRREgular`, see [Options and identifiers, one input line](@ref dynmod_a_principal_options).
Data group A and E must also be given for complete definition of an irregular time domain analysis.



## Irregular time series parameters {#dynmod_d_parameters}

The input in this data group is used to specify the method used for
computation of the underlaying irregular waves, i.e. the seed used for
random number generation and the frequency resolution.

The data group may be skipped if default values are wanted. The data
group is dummy if any floater force models are present in the model.
(The analysis is done in combination with `SIMO`, so-called coupled
analysis, and the irregular time series parameters defined by input to
`SIMO`).



### Data group identifier, one input line {#dynmod_d_parameters_data}

~~~
IRREgular TIMEseries PARAmeters
~~~



### Parameters, one input line {#dynmod_d_parameters_parameters}

~~~
IRAND TIMGEN DTGEN CHFREQ CHAMP
~~~

- `IRAND: integer, default: 1`: Starting parameter of random number generator
- `TIMGEN: real, defaul: 16384`: Length of prescribed wave and motion time series \f$ \mathrm{[T]}\f$
- `DTGEN: real, defaul: 0.5`: Time increment of pre-sampled time series \f$ \mathrm{[T]}\f$
- `CHFREQ: character(4), default: FFT`: Option for selecting wave frequency components
    - `= 'FFT'`: Wave frequency components are selected among the FFT frequencies given by `TIMEGEN` and `DTGEN`. The default criteria are used to find the first and last frequencies.
- `CHAMP: character(5), default: DET`: Option for selecting wave component amplitudes
    - `= 'DET'`: Deterministic wave amplitudes are used.
    - `= 'STOCH'`: Stochastic wave amplitudes are used.
    - `= 0`: Interpreted as `DET`. Included for compatibility with earlier versions.

Note that this data group is dummy for coupled analysis.

Also note that:
-   `TIMGEN` should be equal or longer than the simulation length, `TIME`,
    given in [Irregular response analysis and subsequent input](@ref dynmod_d_analysis).
-   `TIMGEN` will, if necessary, be increased to give a power of 2 time steps (`DTGEN`).
-   The actual time increment used for time domain analysis is defined
    by the parameter `DT`, see [Irregular response analysis and subsequent input](@ref dynmod_d_analysis).
-   To represent the wave surface- and motion time series properly, time
    increments, `DTGEN`, in the range 0.5-1 s are normally acceptable.



## Irregular response analysis and subsequent input {#dynmod_d_analysis}


### Data group identifier, one input line {#dynmod_d_analysis_data}

~~~
IRREgular RESPonse ANALysis
~~~



### Analysis parameters, one input line {#dynmod_d_analysis_parameters}

~~~
IRCNO TIME DT CHWAV CHMOT CHLFM TBEG ISCALE
~~~

- `IRCNO: integer/character`: Irregular wave case number in actual environment applied in this run. Dummy for coupled analysis.
    - `IRCNO = FILE` or `IRCNO = -1`: Wave time series read from file. Data groups [Irregular waves](@ref dynmod_d_irregular_waves) and
[Wave time series file](@ref dynmod_d_wave_and_motion_time_series) must be given
- `TIME: real, default: 11000`: Length of simulation \f$ \mathrm{[T]} \f$
- `DT: real, default: 0.1`: Time step \f$ \mathrm{[T]} \f$
    - See below
- `CHWAV: character(4), default: NEW`: Irregular wave indicator
    - `= 'NONE'`: No wave forces in present analysis. If specified the riser will
have forced excitation at upper end and oscillate in undisturbed water
or in constant current
    - `= NEW`: Wave forces present. New data generated. Data group [Irregular waves](@ref dynmod_d_irregular_waves) must be given.
- `CHMOT: character(4), default: STAT`: Irregular motion indicator
    - `= 'NONE'`: No irregular motions in present analysis
    - `= STAT`: Forced irregular motions present. Computation of prescribed
motions will be based on vessel position in final static position.
    - `= NEW`: Interpreted as `CHMOT=STAT`
    - `= FILE`: Forced irregular motions present. Wave frequency motion time
series read from file. Data group [Wave frequency motion time series file](@ref dynmod_d_wave_and_motion_frequency) must be given.
- `CHLFM: character(4), default: 'NONE'`: Low frequency motion indicator
    - `= 'NONE'`: No low frequency irregular motions present
    - `= FILE`: Forced low frequency irregular motions present. Low frequency
motion time series read from file. Data group [Low frequency motion time series file](@ref dynmod_d_wave_and_motion_low_frequency) must be given.
- `TBEG: real, default: 0`: Time in wave and motion time series that dynamic simulation will start from \f$ \mathrm{[T]} \f$
- `ISCALE: integer, default: 0`: Switch for scaling of terminal point motions
    - `ISCALE = 0`: No scaling
    - `ISCALE = 1`: Scaling: Input line [Support vessel motion scaling factors](@ref dynmod_d_analysis_support) has to be given

`DT` will be adjusted to get an integer ratio between `DTGEN` and
`DT`. `DT` given as negative integer defines the ratio between time step
used in pre-simulation of waves and/or WF-motions and the time step to
be used in the time simulation. (`DTGEN/DT >= 1`)

`TBEG` allows for arbitrary start point in the pre-generated time series.
If the end of the time series is reached during dynamic integration, a
warning is written and motions and water kinematics will be taken from
the start. This can also be useful for elimination of transients from
the time series statistics.

An irregular analysis without waves or vessel motions may be run by
specifying `CHWAV = 'NONE'`, `CHMOT = 'NONE'` and `CHLFM = 'NONE'`.
`IRCNO` must still reference a legal irregular wave case, but the wave
will not be used as no wave kinematics will be generated and not
vessel motions be applied.


### Support vessel motion scaling factors. Only given for ISCALE=1. One line for each vessel in system (NVES lines) {#dynmod_d_analysis_support}

~~~
SCALX SCALY SCALZ SCALXR SCALYR SCALZR
~~~

- `SCALX: real, default: 1`: Scaling for global X-motion \f$ \mathrm{[1]}\f$
- `SCALY: real, default: 1`: Scaling for global Y-motion \f$ \mathrm{[1]}\f$
- `SCALZ: real, default: 1`: Scaling for global Z-motion \f$ \mathrm{[1]}\f$
- `SCALXR: real, default: 1`: Scaling for global X-rotation \f$ \mathrm{[1]}\f$
- `SCALYR: real, default: 1`: Scaling for global Y-rotation \f$ \mathrm{[1]}\f$
- `SCALZR: real, default: 1`: Scaling for global Z-rotation \f$ \mathrm{[1]}\f$

The motions are scaled directly as \f$ \mathrm{DISP_i = SCAL_i \times Motion_i}\f$
where \f$ \mathrm{Motion_i}\f$ is the precomputed motion quantity \f$ \mathrm{_i}\f$.



## Irregular waves {#dynmod_d_irregular_waves}

This data group is omitted for `CHWAV='NONE'`, see data group [Analysis parameters, one input line](@ref dynmod_d_analysis_parameters).

The data group also controls the method for computation of wave
kinematics and motions of the support vessels. In this context FFT or
FFT and cosine series combined means that the vessel motion is
pre-generated by means of FFT, while the wave kinematics are either
pre-generated (FFT) or computed during the actual simulation by use of
cosine series. “Cosine series only” means that both vessel motion and
wave kinematics are computed based on cosine series. It is possible to
overrule the cosine series application for wave kinematics for parts of
the the system by specifying FFT in the detailed specifications,
see [Additional detailed specification of wave kinematics points (optional)](@ref dynmod_d_irregular_waves_procedure_additional).
(“FFT” or “FFT and cosine series combined only”.)



### Data group identifier, one input line {#dynmod_d_irregular_waves_data}

~~~
IRREgular WAVE PROCedure
~~~



### Procedure for wave force calculation, one input line {#dynmod_d_irregular_waves_procedure}

~~~
IUPPOS ISURF KINOFF CHSTEP NODSTP ZLOWER ZUPPER IOPDIF IOPWKI
~~~

- `IUPPOS: integer, default: 1`: Position for calculation of irregular wave kinematics
    - `= 1`: Kinematics at static positions
    - `= 2`: Kinematics at instantaneous positions calculated by summation of cosine components.
    - `= -2`: Kinematics at static positions calculated by summation of cosine components. This option is mainly useful for testing.
    - `= 0`: As 1 but riser fixed in static position, ("wet” elements also "wet" dynamic)
- `ISURF: integer, default: 1`: Code for kinematics in wave zone
    - `= 1`: Integration of wave forces to mean water level
    - `= 2`: Integration of wave forces to wave surface by stretching and compression of the wave potential
    - `= 3`: Integration of wave forces to wave surface by moving the potential to actual surface
    - `= 4`: Integration of wave forces to wave surface by keeping the potential constant from mean water level to wave surface
    - `= 5`: 2nd order wave (integration of wave forces to wave surface)
        - The formulation for 2nd order wave kinematics is based on the Stoke 2nd order wave theory. Only available for kinematics calculated at static position; `IUPPOS = 1 or IUPPOS = 0`.

- `KINOFF: integer, default: 0`: Code for default kinematics points procedure
    - `= 0`: Default procedure on. The initial selection of positions for
computation of kinematics is determined by the parameters `NODSTP`, `ZLOWER`
and `ZUPPER` for all lines in the system. Subsequent specification
(see [Additional detailed specification of wave kinematics points (optional)](@ref dynmod_d_irregular_waves_procedure_additional))
will replace the initial selection.
    - `= 1`: Default procedure off. Kinematics will only be computed at
positions given by subsequent specification
(see [Additional detailed specification of wave kinematics points (optional)](@ref dynmod_d_irregular_waves_procedure_additional))
- `CHSTEP: character(4)`: Code for interpretation of the next parameter
    - `= NODE`: Next parameter interpreted as `NODSTP`
- `NODSTP: integer`: Node step for calculating wave kinematics. (Dummy for `KINOFF = 1`)
    - Kinematics calculated for every `NODSTP` node between `ZLOWER` and `ZUPPER`
(see [Definition of NODSTP, ZLOWER and ZUPPER](@ref Definition_of_NODSTP_ZLOWER_and_ZUPPER)).
    - For intermediate nodes kinematics are derived by linear interpolation.
    - Wave kinematics will always be calculated at submerged supernodes.
    - Note that a negative value of `NODSTP` may be given. The distance between
`ZUPPER` and `ZLOWER` is then divided into 4 (equal) intervals and `NODSTP` is
increased from `ABS(NODSTP)` in the upper interval via `2xABS(NODSTP)` in
the next interval and `4xABS(NODSTP`) to `8xABS(NODSTP)` in the two lower
intervals, see [Definition of NODSTP, ZLOWER and ZUPPER](@ref Definition_of_NODSTP_ZLOWER_and_ZUPPER).
- `ZLOWER: real, default: -WDEPTH`: Z-coordinate indicating lowest node position for which wave kinematics
are calculated \f$ \mathrm{[L]}\f$
    - See [Definition of NODSTP, ZLOWER and ZUPPER](@ref Definition_of_NODSTP_ZLOWER_and_ZUPPER).
    - Dummy for `KINOFF = 1`
    - For `WDEPTH`, see [INPMOD: Water depth and wave indicator](@ref inpmod_d_water)
- `ZUPPER: real, default: 4 x STD_WA`: Upper limit for wave kinematics \f$ \mathrm{[L]}\f$
    - Dummy for `KINOFF = 1`
    - `STD_WA` is the standard deviation of the total wave elevation
- `IOPDIF: integer, default: 0`: Option for specification of wave kinematic transfer function.
    - `IOPDIF = 0`: No transfer function to be specified
    - `IOPDIF = 1`: Read transfer functions from the file specified in [Wave kinematics transfer function file name](@ref dynmod_d_irregular_waves_procedure_trffile) (below).
- `IOPWKI: integer, default: 0`: Option for specification of wave kinematic time series.
    - `IOPWKI = 0`: No wave kinematics time series to be specified
    - `IOPWKI = 2`: Read wave kinematics time series from the binary file specified in
[Wave kinematics time series file name](@ref dynmod_d_irregular_waves_procedure_tsfile) (below).


`NODSTP`, `ZLOWER` and `ZUPPER` will normally be sufficient for specifying the
selection of wave kinematics points.

Note that for large or complicated systems [Additional detailed specification of wave kinematics points (optional)](@ref dynmod_d_irregular_waves_procedure_additional)
may be used to override the selection given by `NODSTP`, `ZLOWER` and `ZUPPER`; e.g.
skip generation of wave kinematics for selected lines, generate
kinematics at more points along an important line.


\anchor Definition_of_NODSTP_ZLOWER_and_ZUPPER
![Definition of NODSTP, ZLOWER and ZUPPER](@ref figures/um_id_fig222.svg)
@image latex figures/um_id_fig222.pdf "Definition of NODSTP, ZLOWER and ZUPPER" width=12cm

Note that the definition of ISURF is also used to determine where to apply wind forces to airfoil cross sections near the water line.
That is, no wind forces are applied to wet sections of the element.
The wind speed is nevertheless taken to be zero at or below the mean water level.

Note that the option `IUPPOS = 0` cannot be combined with linear analysis, `ITDMET = 1`, or nonlinear analysis, `ITDMET = 2` and `SIMO` bodies.


#### Wave kinematics transfer function file name {#dynmod_d_irregular_waves_procedure_trffile}

This data group is omitted for `IOPDIF = 0`
~~~
CHFDIF
~~~

- `CHFDIF: character(80)`: File name with wave kinematic transfer function.
    - The file format is described in [Diffracted Wave Transfer Functions at Points](@ref dynmod_description_wave).



#### Wave kinematics time series file name {#dynmod_d_irregular_waves_procedure_tsfile}

This data group is omitted for `IOPWKI = 0`

Wave kinematics read from file will replace the corresponding wave
kinematics calculated by `DYNMOD`. These kinematics will then be used
in the calculation of Morison type hydrodynamic loads on `RIFLEX`
elements. Loads on `SIMO` bodies will NOT be affected.

`RIFLEX` vessel motions based on vessel motion transfer functions and
MacCamy Fuchs and Potential flow loads on `RIFLEX` elements are
per-generated from the wave Fourier components and are therefore NOT
affected by the wave kinematics read from file. Elements with MacCamy
Fuchs or Potential flow loads may not have kinematics read from file.

If kinematics read from file are used in a simulation with `SIMO`
bodies, vessel motions based on vessel motion transfer functions or
pre-generated hydrodynamic loads, the user must ensure that the
kinematics are consistent with the Fourier components.

~~~
CHFDIF
~~~

- `CHFWKI: character(80)`: File name with wave kinematic time series.
    - The file format is specified by `IOPWKI` and is the same as the kinematics file with the same format exported from DYNMOD using
[Storage of irregular wave kinematics] (@ref dynmod_d_storage)


~~~
ICOLMX ICOLTM
~~~

- `ICOLMX: integer, default: 0`: Maximum number of columns on file. For binary format, `IOPWKI = 2`, this includes the two columns of FORTRAN specific data. Please see the key file `key_<prefix>_wavkin.txt` generated when storing kinematics.
- `ICOLTM: integer, default: 2`: Column number on file for time


#### Additional detailed specification of wave kinematics points (optional) {#dynmod_d_irregular_waves_procedure_additional}

As many input lines as needed. Note three alternative formats.



##### For wave kinematics calculated by the program from the undisturbed waves.

~~~
LINE-ID CHSTEP = NODE NODSTP
~~~

- `LINE-ID: character(8)`: Line identifier
- `CHSTEP: character(4)`: `= Node`
- `NODSTP: integer`: Node step for calculating wave kinematics
    - `= 0`: No kinematics for this line
    - `> 0`: Kinematics for each `NODSTP` node



##### For wave kinematics given by wave kinematics transfer functions (diffracted waves)

~~~
LINE-ID CHSTEP= DIFF ILSEG ILNODE IVES PTNOUS
~~~

- `LINE-ID: character(8)`: Line identifier
- `CHSTEP: character(4)`: `= DIFF`
- `ILSEG: integer`: Local segment number within line LINE-ID
- `ILNODE: integer`: Local node number within ILSEG
- `IVES: integer`:
    - `= 0`: Use undisturbed wave kinematics at this node
    - `> 0`: Support vessel number. Used as reference to transfer function for diffracted wave kinematics.
- `PTNOUS: integer`: Point reference(s) to transfer function for diffracted wave kinematics

Up to 30 values of PTNOUS may be given on each line. The diffracted kinematics at the specified
node will be generated by interpolation based on the nearest point references. 

##### For wave kinematics given by wave kinematics time series

~~~
LINE-ID CHSTEP= WKFI ILSEG ILNODE ICOLST
~~~

- `LINE-ID: character(8)`: Line identifier
- `CHSTEP: character(4)`: `= WKFI`
- `ILSEG: integer`: Local segment number within line LINE-ID
- `ILNODE: integer`: Local node number within ILSEG
- `ICOLST: integer`: Column number for the first wave kinematics time series for this node


## Wave and motion time series files {#dynmod_d_wave_and_motion}



### Wave time series file {#dynmod_d_wave_and_motion_time_series}

This data group is given only if `IRCNO = FILE`.



#### Data group identifier, one input line {#dynmod_d_wave_and_motion_time_series_data}

~~~
WAVE TIME SERIes
~~~



#### Wave time series file information {#dynmod_d_wave_and_motion_time_series_file}

~~~
CHFTSF IFORM ICOTIM ICOWAV
~~~

- `CHFTSF: character(60)`: File name
- `IFORM: integer, default: 1`: File format code
    - `= ASCI`: Column organised ASCII file
    - `= STAR`: Startimes file
- `ICOTIM: integer, default: 1`: Column number for time
    - Dummy for `IFORM = STAR`
- `ICOWAV: integer/real, default: 2`: Column or time series number for wave elevation

The wave direction is given by the parameter `WADR1` given in `INPMOD`
for the irregular wave case `IRCNO` referred to in [Analysis parameters, one input line](@ref dynmod_d_analysis_parameters).

`ICOTIM` and `ICOWAV` will refer to columns on an ASCII file; e.g. `ICOTIM=1`
and `ICOWAV=2` if the time and wave elevation are in the first and second
columns; or to a time series number on a Startimes file; e.g.
`ICOWAV=10.01` for time series 10, version 1.

An arbitrary time step may be used on an ASCII file, while the
Startimes file has a fixed step. Linear interpolation is used to get the
motions at the time step (DTWF)



#### Direction, location of measurement and cut-off for filtering {#dynmod_d_wave_and_motion_time_series_direction}

~~~
WAVDIR XGWAV YGWAV TMIN TMAX
~~~

- `WAVDIR: real, default: 0`: Wave direction \f$ \mathrm{[deg]}\f$
- `XGWAV: real, default: 0`: Global x-coordinate for position where time series is measured
- `YGWAV: real, default: 0`: Global y-coordinate for position where time series is measured
- `TMIN: real, default: 0`: Period corresponding to cut-off frequency for filtering
- `TMAX: real, default: 0`: Period corresponding to cut-off frequency for filtering

If `TMIN` and `TMAX` are both zero: No filtering

If `TMIN` and `TMAX` are both different from zero: band-pass filtering

Filtering is not implemented in present version



### Wave frequency motion time series file {#dynmod_d_wave_and_motion_frequency}

This data group is given only if `CHMOT=FILE`. Note that data must be
given for all vessels in the system.

#### Data group identifier, one input line {#dynmod_d_wave_and_motion_frequency_data}

~~~
WFMOtion TIME SERIes
~~~



#### Wave frequency motions file information, NVES input lines {#dynmod_d_wave_and_motion_frequency_motions}

~~~
IVES CHFTSF IFORM IKIND IROT ICOTIM ICOXG ICOYG ICOZG ICOXGR ICOYGR ICOZGR
~~~

- `IVES: integer`: Vessel Number
- `CHFTSF: character(60)`: File name
- `IFORM: character(4), default: ASCI`: File format code
    - `= ASCI`: Column organised ASCII file
    - `= STAR`: Startimes file
    - `= NONE`: No wave frequency motions for this vessel. The remainder of this
input line is dummy
- `IKIND: character(4), default: POSI`: Kind of motion time series input
    - `= POSI`: Global positions, i.e. global coordinates. The rotations are applied in the Euler sequence: Rz-Ry-Rx. Consistent with vessel motion time series from `SIMO`.
    - `= DYND`: Global dynamic displacements; i.e. global coordinates minus the final static position. The rotations are applied in the Euler sequence: Rx-Ry-Rz
- `IROT: character(4), default: DEGR`: Unit of rotations
    - `= DEGR`: Rotations given in degrees
    - `= RADI`: Rotations given in radians
- `ICOTIM: integer, default: 1`: Column number for time
    - Dummy for `IFORM = STAR`
- `ICOXG: integer/real, default: 0`: Column or time series number for specification of global x-motion. Absolute position if `IKIND = POSI`, relative to static position if `IKIND = DYND`.
- `ICOYG: integer/real, default: 0`: Column or time series number for specification of global y-motion. Absolute position if `IKIND = POSI`, relative to static position if `IKIND = DYND`.
- `ICOZG: integer/real, default: 0`: Column or time series number for specification of global z-motion. Absolute position if `IKIND = POSI`, relative to static position if `IKIND = DYND`.
- `ICOXGR: integer/real, default: 0`: Column or time series number for specification of global x-rotation. Absolute position if `IKIND = POSI`, relative to static position if `IKIND = DYND`.
- `ICOYGR: integer/real, default: 0`: Column or time series number for specification of global y-rotation. Absolute position if `IKIND = POSI`, relative to static position if `IKIND = DYND`.
- `ICOZGR: integer/real, default: 0`: Column or time series number for specification of global z-rotation. Absolute position if `IKIND = POSI`, relative to static position if `IKIND = DYND`.

Dofs may be omitted by giving `ICOxxx=0`

`ICOxxx` will refer to a column for an ASCII file; e.g. `ICOX=2` if the
dynamic x motion time series is in the second column; or to a time
series number for a Startimes file, e.g. `ICOX=1.02` for time series 1,
version 2.

An arbitrary time step may be used on an ASCII file, while the
Startimes file has a fixed time step. Linear interpolation is used to
get the motions at the time step (`DTWF`).

Translational dofs are given in length units. Rotational dofs are given
in degrees or radians, depending on the option `IROT`.

If only one rotation is nonzero or if all rotations are small, the
order in which the rotations are applied will not be significant.

Please note that the line length of ASCII input files is currently
limited to 260 characters, see [Formats](@ref how_to_run_formats) in 
[How to Run the Program](@ref how_to_run_input). Note that a
RIFLEX input line may be split into several lines on the input file.



### Low frequency motion time series file {#dynmod_d_wave_and_motion_low_frequency}

This data group is given only if `CHLFM=FILE`. Note that data must be
given for all vessels in the system.



#### Data group identifier, one input line {#dynmod_d_wave_and_motion_low_frequency_data}

~~~
LFMOtion TIME SERIes
~~~



#### Low frequency motions file information, NVES input lines {#dynmod_d_wave_and_motion_low_frequency_file}

~~~
IVES CHFTSF IFORM IKIND IROT ICOTIM ICOXG ICOYG ICOZGR
~~~

- `IVES: integer`: Vessel Number
- `CHFTSF: character(60)`: File name
- `IFORM: character(4), default: ASCI`: File format code
    - `= ASCI`: Column organised ASCII file
    - `= STAR`: Startimes file
    - `= NONE`: No wave frequency motions for this vessel. The remainder of this
input line is dummy
- `IKIND: character(4), default: POSI`: Kind of motion time series input
    - `= POSI`: Global positions, i.e. global coordinates. The rotations are applied in the Euler sequence: Rz-Ry-Rx. Consistent with vessel motion time series from `SIMO`.
    - `= DYND`: Global dynamic displacements; i.e. global coordinates minus the final static position. The rotations are applied in the Euler sequence: Rx-Ry-Rz
- `IROT: character(4), default: DEGR`: Unit of rotations
    - `= DEGR`: Rotations given in degrees
    - `= RADI`: Rotations given in radians
- `ICOTIM: integer, default: 1`: Column number for time
    - Dummy for `IFORM = STAR`
- `ICOXG: integer/real, default: 0`: Column or time series number for specification of global x-motion. Absolute position if `IKIND = POSI`, relative to static position if `IKIND = DYND`.
- `ICOYG: integer/real, default: 0`: Column or time series number for specification of global y-motion. Absolute position if `IKIND = POSI`, relative to static position if `IKIND = DYND`.
- `ICOZGR: integer/real, default: 0`: Column or time series number for specification of global z-rotation. Absolute position if `IKIND = POSI`, relative to static position if `IKIND = DYND`.

Dofs may be omitted by given `ICOxxx=0`

`ICOxxx` will refer to a column for an ASCII file; e.g. `ICOSUR=2` if the
dynamic x motion time series is in the second column; or to a time
series number for a Startimes file, e.g. `ICOX=1.02` for time series 1,
version 2.

An arbitrary time step may be used on an ASCII file, while the
Startimes file has a fixed time step. Linear interpolation is used to
get the motions at the time step (`DTWF`).

Translational dofs are given in length units. Rotational dofs are given
in degrees or radians, depending on the option `IROT`.

If only one rotation is nonzero or if all rotations are small, the
order in which the rotations are applied will not be significant.


## Print options for FFT analysis {#dynmod_d_print}



### Data group identifier, one input line {#dynmod_d_print_data}

~~~
IRREgular FOURier PRINt
~~~



### Fourier print options {#dynmod_d_print_fourier}

~~~
IPMOTI IPWAFO IPHFTS IPLFTS IPTOMO IPVEAC
~~~

- `IPMOTI: integer, default: 0`: Print option for the main routine
    - `<= 0`: No print
    - `> 1`: Key information printed
    - `> 2`: Some more data printed
    - `> 5`: Low level debug print during numerical integration activated
- `IPWAFO: integer, default: 0`: Print option for the wave fourier component generation
    - Not active in present version
- `IPHFTS: integer, default: 0`: Print option for HF-time series generation
    - `<= 0`: No print
    - `> 0`: Print of wave frequency vessel motion time series
- `IPLFTS: integer, default: 0`: Print option for LF-time series generation
    - `<= 0`: No print
    - `> 0`: Print of low frequency vessel motion time series
- `IPTOMO: integer, default: 0`: Print option for TOTAL motion time series generation
    - `<= 0`: No print
    - `> 0`: Print of total vessel motion time series
- `IPVEAC: integer, default: 0`: Print option for generation of water particle velocities and
acceleration
    - `<= 0`: No print
    - `> 1`: Key information printed
    - `> 2`: Some data printed
    - `> 5`: Extensive debug print of arrays with water particle velocities and accelerations

This data-group is normally supposed to be omitted. Increasing
value of print options gives increasing amount of print.



## Storage of irregular wave kinematics (optional) {#dynmod_d_storage}



### Data group identifier, one input line {#dynmod_d_storage_data}

~~~
IRREgular KINEmatics STORage
~~~



### Wave kinematics storage options one input line {#dynmod_d_storage_wave}

~~~
NLKINE IKINFM
~~~

- `NLKINE: integer, default: 0`: Number of specifications for storage of wave kinematics
    - `= 0`: Wave elevation, velocities and accelerations are stored for all kinematics nodes. Currently, no other value is allowed.
- `IKINFM: integer, default: 2`: File format for kinematics storage
    - `= 1`: ASCII format
    - `= 2`: Binary format

Pre-generated wave kinematics are written to `<prefix>_wavkin.asc` or
`<prefix>_wavkin.bin`. Kinematics calculated during the simulation;
`IUPPOS = 2 or -2`; are written to `<prefix>_updkin.asc` or
`<prefix>_updkin.bin`.

The contents are described in `key_<prefix>_wavkin.txt` or
`key_<prefix>_updkin.txt`.



# Data Group E: Time Domain Procedure and File Storage Parameters {#dynmod_e}

This data group must always be given for `IANAL = REGU` and `IRRE` (time
domain analysis) specified in input line [Options and identifiers, one input line](@ref dynmod_a_principal_options).



## Method of analysis and subsequent input {#dynmod_e_method}



### Data group identifier, one input line {#dynmod_e_method_data}

~~~
TIME DOMAin PROCedure
~~~



### Method and subsequent input, one input line {#dynmod_e_method_method}

~~~
ITDMET INEWIL
~~~

- `ITDMET: integer, default: 1`: Method indicator
    - `ITDMET = 0`: Prestochastic analysis only. The rest of the data in input
groups E are irrelevant
    - `ITDMET = 1`: Linear analysis
    - `ITDMET = 2`: Nonlinear analysis. More information to define method is
given in [Nonlinear step by step integration](@ref dynmod_e_nonlinear)
- `INEWIL: integer, default: 1`: Procedure indicator
    - `INEWIL = 1`: Newmark's procedure
    - `INEWIL = 2`: Wilson’s procedure, illegal for non-linear analysis



### Time integration and damping parameters, one input line {#dynmod_e_method_time}

This data group can be omitted if default values are wanted.

~~~
BETIN GAMMA TETHA A1 A2 A1T A1TO A1B A2T A2TO A2B DAMP_OPT
~~~


- `BETIN: real, default: 4/6`: Inverse value of beta-parameter of the Newmark beta-family of integration operators
    - `BETIN = 4.0` gives beta=1/4,i.e. constant average acceleration method
- `GAMMA: real, default: 0.5`: Value of the parameter gamma of the Newmark operators (usually equal to 0.5)
- `TETHA: real, default: See below`: Value of the parameter tetha in Wilson's integration method
- `A1: real, default: 0`: Global mass proportional damping factor \f$ \mathrm{a_1}\f$, see definition below
- `A2: real, default: 0.001/0`: Global stiffness proportional damping factor \f$ \mathrm{a_2}\f$
- `A1T: real, default: 0`: Additional local mass proportional damping factor \f$ \mathrm{a_{1t}}\f$ for tension
- `A1TO: real, default: 0`: Additional local mass proportional damping factor \f$ \mathrm{a_{1to}}\f$ for torsion
- `A1B: real, default: 0`: Additional local mass proportional damping \f$ \mathrm{a_{1b}}\f$ for bending
- `A2T: real, default: 0`: Additional local stiffness proportional damping factor \f$ \mathrm{a_{2t}}\f$ for tension
- `A2TO: real, default: 0`: Additional local stiffness proportional damping factor \f$ \mathrm{a_{2to}}\f$ for torsion
- `A2B: real, default: 0`: Additional local stiffness proportional damping factor \f$ \mathrm{a_{2b}}\f$ for bending
- `DAMP_OPT: character(4), default: TOTA`: Option for stiffness contribution to Rayleigh damping
    - `= TOTA`: Stiffness proportional damping is applied using total stiffness, i.e. both material and geometric stiffness
    - `= MATE`: Stiffness proportional damping is applied using material stiffness only


Default values:

- For `INEWIL=1` (Newmark) the following alternative default values are: `BETIN=4.0`, `THETA=1.0`, `A2=0.001`
- For `INEWIL=2` (Wilson) default values are: `BETIN=6.0`, `TETHA=1.4` (linear)


#### Global proportional damping formulation:

\f$ \boldsymbol{\mathrm C} = a_1 \boldsymbol{\mathrm M} + a_2 \boldsymbol{\mathrm K} \f$

This means that the global damping matrix \f$ \boldsymbol{\mathrm C} \f$ is established as a
linear combination of the global mass (\f$ \boldsymbol {\mathrm M}\f$) and the total or material stiffness (\f$ \boldsymbol {\mathrm K} \f$) matrices.

The mass and stiffness-proportional damping specified here will not be applied to elements for which mass- and/or stiffness-proportional damping is specified in INPMOD.

#### Numerical values of \f$ \mathrm{a_1} \f$ and \f$ \mathrm{a_2} \f$:

Let the structural damping to critical damping ratio, \f$ \mathrm{c/(2m \omega) }\f$,
at two natural frequencies \f$ \mathrm{\omega_1 }\f$ and \f$ \mathrm{\omega_2 }\f$ be \f$ \mathrm{\lambda_1 }\f$ and \f$ \mathrm{\lambda_2 }\f$, respectively.  
Then `A1` and `A2` can be computed as:
- \f$ \mathrm{a_1 = \frac{2 \omega_1 \omega_2 }{ \omega_2^2 - \omega_1^2}(\lambda_1 \omega_2 - \lambda_2 \omega_1) }\f$
- \f$ \mathrm{a_2 = \frac{2( \omega_2 \lambda_2 - \omega_1 \lambda_1) }{ \omega_2^2 - \omega_1^2} }\f$


#### Additional local proportional damping formulation:

In this approach, the damping coefficients are introduced in the local
degrees of freedom in order to allow for different damping levels in
bending, torsion and tension. The element damping matrix can the be
written as

\f$ \boldsymbol{\mathrm c} = a_1 \boldsymbol{\mathrm M} +a_{1t} \boldsymbol{\mathrm m}_t + a_{1to} \boldsymbol{\mathrm m}_{to} + a_{1b} \boldsymbol{\mathrm m}_b + a_2 \boldsymbol{\mathrm K} + a_{2t} \boldsymbol{\mathrm k}_t + a_{2to} \boldsymbol{\mathrm k}_{to} + a_{2b} \boldsymbol{\mathrm k}_{b} \f$

where subscripts \f$ \mathrm{ _t }\f$, \f$ \mathrm{ _{to} }\f$ and \f$ \mathrm{_b }\f$ refer to tension, torsion and bending contributions, respectively,
and the matrices \f$ \boldsymbol{\mathrm c_{} }\f$, \f$ \boldsymbol{\mathrm m }\f$ and \f$ \boldsymbol{\mathrm k_{} }\f$ are local element matrices; e.g.
\f$ \boldsymbol{\mathrm k}_b \f$ includes all bending deformation
terms in the local element stiffness matrix.

For cross sections applied for blades of a operating wind turbine the matrix \f$ \boldsymbol{\mathrm k_{} }\f$ should only 
include the material stiffness matrix. The geometric stiffness matrix should not be included as this would introduce damping 
of the rigid body motion.

One should be careful with global mass proportional damping as
this may introduce internal damping from rigid body motion.

If \f$ \mathrm{a_1 = }\f$ `0`, \f$ \mathrm{a_2}\f$ simply becomes \f$ \mathrm{2 \lambda / \omega}\f$.

Note that proportional damping (global and local) adds to a possible
structural damping arising from hysteresis in bending moment/curvature
relation.



### Non-linear force model, one input line. Always submit for linear and non-linear analysis {#dynmod_e_method_non}

~~~
INDINT INDHYD MAXHIT EPSHYD TRAMP INDREL ICONRE ISTEPR LDAMP
~~~

- `INDINT: integer, default: 1`: Indicator for modelling forces from internal slug flow
    - Nonlinear analysis only.
    - `INDINT = 1`: Forces from internal slug flow not considered
    - `INDINT = 2`: Forces from internal slug flow considered.
    - Data group [Slug force calculations](@ref dynmod_e_slug) or [Import of internal flow data from file](@ref dynmod_e_import) must be given.
- `INDHYD: integer, default: 1`: Indicator for hydrodynamic force model. Linear analysis only.
    - (see 'Dynamic Time Domain Analysis' in the Theory Manual).
    - `INDHYD = 1`: No force iteration, use of displacements and velocities at previous time step
    - `INDHYD = 2`: No force iteration, use of displacements, velocities and accelerations at previous time step (not recommended)
    - `INDHYD = 3`: Force iteration performed
- `MAXHIT: integer, default: 5`: Maximum number of load iterations. Linear analysis only.
    - A negative value gives print of convergence for each step, then `MAXHIT = ABS(MAXHIT)`
- `EPSHYD: real, default: 0.01`: Convergence control parameter for force iteration. Linear analysis only.
    - Dummy for `INDHYD = 1, 2` \f$ \mathrm{[1]}\f$
- `TRAMP: real, default: 10`: Duration of start-up procedure \f$ \mathrm{[T]}\f$
- `INDREL: integer, default: 0`: Indicator for rupture/release
    - `INDREL = 0`: No riser rupture/release
    - `INDREL = 1`: Riser rupture/release will be simulated
- `ICONRE: integer, default: 0`: Ball joint connector no. to be released
    - `ICONRE = 0`: All ball joint connectors in the system are released simultaneously
    - `ICONRE = i`: Ball joint connector no. i is released. See reference number ("ref no")
      in the table Components on the `STAMOD` result file for
      connector numbering. The connectors are normally numbered from
      the first end as 1, 2 etc. following the `FEM` model.
- `ISTEPR: integer, default: 0`: Time step no. for release (nonlinear analysis only)
    - In linear analysis the ball joint connector will be released at the first step
- `LDAMP: integer, default: 0`: Option for calculation of proportional damping matrix in nonlinear analysis.
    - Irrelevant for linear analyses
    - `LDAMP = 0`: Use constant proportional damping matrix calculated at static position
    - `LDAMP = 1`: Use updated proportional damping matrix according to instantaneous mass and stiffness matrices

For non-linear analysis (`ITDMET = 2`, see [Method and subsequent input, one input line](@ref dynmod_e_method_method)) `INDHYD` can
have the values 1 or 2. Input of 3 will be interpreted as 2. Load
iteration for non-linear analysis will always be performed in connection
with equilibrium iteration, but not during equilibrium correction.

If load convergence is not obtained after `MAXHIT` iteration,
computation will proceed after output of warning.

As a release/rupture analysis is very sensitive, a short time step and rather firm convergence
limit is required. If the response of part of the system is not of interest after the release,
the [Boundary change option](@ref dynmod_e_time_boundary) may be used to fix the nodes in this part of the system.

\anchor Definition_of_clutch_start_up_procedure
![Definition of clutch (start up procedure)](@ref figures/um_id_fig237.svg)
@image latex figures/um_id_fig237.pdf "Definition of clutch (start up procedure)" width=16cm



## Nonlinear step by step integration {#dynmod_e_nonlinear}

This data group is only given for `ITDMET=2` (input group [Method and subsequent input, one input line](@ref dynmod_e_method_method)).



### Data group identifier, one input line {#dynmod_e_nonlinear_data}

~~~
NONLinear INTEgration PROCedure
~~~



### Specification of incrementation procedure, one input line {#dynmod_e_nonlinear_specification}

~~~
ITFREQ ISOLIT MAXIT DACCU ICOCOD IVARST ITSTAT CHNORM EACCU
~~~

- `ITFREQ: integer, default: 1`: Frequency of equilibrium iteration
    - `ITFREQ <= 0`: Iteration will not be performed
    - `ITFREQ >= 1`: Iteration will be performed every `ITFREQ` time step. For steps without iteration equilibrium correction will be performed.
    - The remaining variables in this input line are dummy if `ITFREQ <= 0`
- `ISOLIT: integer, default: 1`: Type of iteration if iteration is to be performed
    - `ISOLIT = 1`: True Newton-Raphson, updating of geometric stiffness from axial force
    - `ISOLIT = 2`: Modified Newton-Raphson iteration
    - Modified Newton-Raphson iteration is not included in the current version of the program
- `MAXIT: integer, default: 10`: Maximum number of iterations for steps with iteration
- `DACCU: real, default:` \f$ 10^{-6}\f$: Desired accuracy for equilibrium iteration measured by a modified
Euclidean displacement norm (norm of squared translations)
    - Recommended values: \f$ 10^{-6} - 10^{-5} \f$ cfr. `STAMOD` analysis \f$ \mathrm{[1]}\f$
- `ICOCOD: integer, default: 1`: Code for continuation after iteration
    - `ICOCOD = 0`: Computations interrupted if accuracy requirements are not fulfilled
    - `ICOCOD = 1`: Computations continue even if accuracy requirements are not fulfilled. Warning is printed
- `IVARST: integer, default: 0`: Code for automatic subdivision of time step
    - `IVARST = 0`: No subdivision
    - `IVARST > 0`: Automatic subdivision of time step if required accuracy is
not obtained with original time step or if incremental rotations are to large.
    - Maximum number of subdivisions: \f$ \mathrm{ 2^{IVARST} }\f$
- `ISTAT: integer, default: 1`: Code for time integration information
    - `ITSTAT = 0`: No information
    - `ITSTAT > 1`: Number of iterations, subdivisions and obtained accuracy are presented
- `CHNORM: character(4), default: DISP`: Convergence norm switch
        - `= DISP`: Use the default Euclidean displacement norm only
        - `= BOTH`: Use both the default Euclidean displacement norm and the energy norm  
- `EACCU: real, default:` \f$ 10^{-6} \f$: Required accuracy measured by energy norm
        - Dummy if `CHNORM=DISP`  



## Modification to water kinematics {#dynmod_e_modification}

Modification to water kinematics due to moonpool kinematics may be
specified. The water kinematics will be based on the velocities and
acceleration of the actual support vessel or floater force model
specified.



### Data group identifier, one input line {#dynmod_e_modification_data}

~~~
WATEr KINEmatic CONDition
~~~



### Rigid moonpool column, one input line {#dynmod_e_modification_data_rigid}

~~~
RIGId MOONpool COLumn
~~~



#### Specification of number of moonpools, one input line {#dynmod_e_modification_data_rigid_number}

~~~
NLSPEC
~~~

- `NLSPEC: integer`: Number of Rigid Moonpool Columns



#### Specification of support vessel moonpool, one input line. {#dynmod_e_modification_data_rigid_support}

~~~
CHSUPP IVES ZLLOW ZLUP
~~~

- `CHSUPP: character`: Type of support vessel
    - `= VESSEL`: `RIFLEX` support vessel (Prescribed motions)
    - `= FLOATER`: Floater force model
- `IVES: integer`: Support vessel number
- `ZLLOW: real`: Lower Z limit (local vessel system) \f$ \mathrm{[L]}\f$
- `ZLUP: real`: Upper Z limit (local vessel system) \f$ \mathrm{[L]}\f$

One input line



#### Specification of lines within present moonpool, one input line {#dynmod_e_modification_data_rigid_lines}

~~~
LINE-ID1 LINE-ID2 ....... LINE-IDi .........LINE-IDn
~~~

- `LINE-ID: character(8)`: Line identifiers within moon pool



The data groups 'Specification of support vessel moonpool' and 'Specification of lines within present moonpool' are to be repeated `NLSPEC` times.

- Rigid moonpool column may not be combined with CHMOT='NONE': No irregular motions, for irregular wave analysis .
- Rigid moonpool column may not be combined with IMOTD = 0: No motions, for regular wave analysis.
- If current is loaded in static analysis, the current forces will be removed at start of dynamic analysis for lines within moonpool and may create a transient.


## Slug force calculations {#dynmod_e_slug}

This data group is only given for `INDINT=2` ([Non-linear force model, one input line. Always submit for linear and non-linear analysis](@ref dynmod_e_method_non)), and slug
forces can only be specified for single risers.



### Data group identifier, one input line {#dynmod_e_slug_data}

Restrictions
- The main riser line has to be modelled by beam elements
- Consistent formulation (Lumped mass option is prohibited)

Assumptions
- The total slug mass is constant, \f$\boldsymbol{\mathrm{M_S}}\f$. Initial length is \f$\boldsymbol{\mathrm{L_{S0}}}\f$
- The specified velocity refers to the gravity centre of the slug, initially at the half length.
- The slug specification is superimposed on the riser mass, including any internal fluid flow.
- The internal cross-section area is not used in the slug modelling
- The slug length is divided into sections. Initially the sections are
of equal length \f$\boldsymbol{\mathrm{dl_{S,0}}}\f$. The density, (mass per unit length) is
constant within each section. Initially the mass per unit length is \f$\boldsymbol{\mathrm{m_0 = M_S/L_{S0}}}\f$


#### Input description for slug force specification

~~~
SLUG FORCe SPECification
~~~



### Specification of slug data, one input line {#dynmod_e_slug_specification}

~~~
TSLUG ICOSLG SLGLEN SLGMAS SLGVEL IDENS IVEL NCYCLE CYCTIM
~~~

- `TSLUG: real, default: 0`: Time when slug enters first end of main riser line \f$ \mathrm{[T]}\f$
- `ICOSLG: integer, default: 1`: Interruption parameter
    - `=0`: Analysis termination controlled by slug
    - `=1`: Analysis termination controlled by specified length of simulation (TIME)
- `SLGLEN: real`: Initial slug length \f$ \mathrm{[L]}\f$
- `SLGMAS: real`: Slug mass \f$ \mathrm{[M]}\f$
- `SLGVEL: real`: Initial slug velocity \f$ \mathrm{[L/T]}\f$
- `IDENS: integer, default: 0`: Control parameter density
    - `= 0`: Constant density
    - `= 1`: Variable density with vertical position
- `IVEL: integer, default: 0`: Control parameter velocity
    - `= 0`: Constant velocity
    - `= 1`: Variable velocity
    - The specified velocity refers to the gravity centre of the slug
- `NCYCLE: integer, default: 1`: Number of slug cycles
- `CYCTIM: real`: Slug cycle time (dummy if `NCYCLE = 1`) \f$ \mathrm{[T]}\f$



#### if `IDENS = 1`:

~~~
Z2 SLGMA2 ZREF
~~~

- `Z2: real`: Second vertical position where the slug unit mass is specified \f$ \mathrm{[L]}\f$
- `SLGMA2: real`: Slug unit mass at `Z2` \f$ \mathrm{[M/L]}\f$
- `ZREF: real < 0`: Reference depth \f$ \mathrm{[L]}\f$
    - `ZREF` < \f$\mathrm{Z_{MIN}}\f$, where \f$\mathrm{Z_{MIN}}\f$ is lowest vertical position along the main riser line


The unit mass at a specific z-position is calculated according to the following equation:

\f$ \mathrm{m(Z_i) = A(Z_i-Z_{REF})^\alpha  }\f$

where
- \f$\mathrm{ \alpha = \frac{ln(m_1/m_2)}{ln(\frac{Z_1 - Z_{REF}}{Z_2 - Z_{REF}})}}\f$
- \f$\mathrm{A = \frac{m_1}{(Z_1 - Z_{REF})^\alpha } }\f$
- \f$ \mathrm{m_1}\f$: `SLGMAS/SLGLEN`
- \f$ \mathrm{m_2}\f$: `SLGMA2`
- \f$ \mathrm{Z_1}\f$: Vertical coordinate at inlet, end 1 of main riser line

![Internal slug flow](@ref figures/um_fig_244.svg)
@image latex figures/um_fig_244.pdf "Internal slug flow" width=12cm

#### if `IVEL = 1`:

~~~
DELVEL VEXP
~~~

- `DELVEL: real`: Velocity specification
- `VEXP: real`: Exponent for velocity

The unit mass at a specific z-position is calculated according to the
following equation:

\f$ \mathrm{V(Z_i) = V_1 - \Delta V |Z_i - Z_1|^\alpha}\quad \f$ for \f$\quad \mathrm{(Z_i - Z_1) >= 0}\f$

\f$ \mathrm{V(Z_i) = V_1 + \Delta V |Z_i - Z_1|^\alpha}\quad \f$ for \f$\quad \mathrm{(Z_i - Z_1) < 0}\f$

Where:
- \f$ \mathrm{V_1}\f$: Initial slug velocity (Velocity at inlet)
- \f$ \mathrm{\Delta V}\f$: **DELVEL**
- \f$ \mathrm{Z_i}\f$: Vertical coordinate at inlet, end 1 of main riser line
- \f$ \mathrm{\alpha}\f$: **VEXP**



## Import of internal flow data from file {#dynmod_e_import}

This data group is only given for `INDINT=2` (see [Non-linear force model, one input line. Always submit for linear and non-linear analysis](@ref dynmod_e_method_non))



### Data group identifier, 1 input line {#dynmod_e_import_data}

~~~
IMPOrt FLOW DATA
~~~



### Specification of input flow file, one input line {#dynmod_e_import_specification}

~~~
IMRL CHOPAD CHFFLW
~~~

- `IMRL: integer, default: 0`: Main riser line number
    - `= 0`: All lines
- `CHOPAD: character(4), default: REPL`: Fluid contents option
    - `= REPL`: Specified flow replaces that given in the Main Riser Line definition
    - `= ADDI`: Specified flow is in addition to that given in the Main Riser Line definition
- `CHFFLW: character(70)`: Name of flow data file

The flow input file is described in [See Internal flow description](@ref dynmod_description_internal)



## Dynamic current variation {#dynmod_e_dynamic_current}

Available for nonlinear dynamic analysis, but only when the current
profile is specified explicitly on the `INPMOD` input file. This means
that this data group cannot be given for coupled analysis or when the
current is specified on a `CURMOD` input file. However, dynamic
current conditions can alternatively be specified using `CURMOD`.

Varying current velocity and direction are specified at the current
levels defined in the preceding static analysis. The varying current is
to be described in a separate file. For description of the file format,
confer chapter [Description of Additional Input Files: Dynamic Current Variation](@ref dynmod_description_current).



### Data group identifier, one input line {#dynmod_e_dynamic_current_data}

~~~
DYNAmic CURRent VARIation
~~~



### File name {#dynmod_e_dynamic_current_file}

~~~
CHFCUR
~~~

- `CHFCUR: character(80)`: File name with current velocity and direction

ASCII file containing current velocity and direction at specified time
instants. The velocity and directions have to be given at all levels
defined in the preceding static analysis.



## Dynamic nodal forces {#dynmod_e_dynamic_nodal}

This data group enables the user to specify additional dynamic nodal
force components. The force components may either be described by simple
functions or read from a separate input file. For file description, see
chapter [Description of Additional Input Files: Dynamic Nodal Forces](@ref dynmod_description_nodal).



### Data group identifier, one input line {#dynmod_e_dynamic_nodal_data}

~~~
DYNAmic NODAl FORCes
~~~



### Number of specified components specified by functions or by time series on file {#dynmod_e_dynamic_nodal_number}

~~~
NDCOMP CINPUT CHFLOA
~~~

- `NDCOMP: integer`: Number of load components to be specified
- `CINPUT: character(6), default: 'NOFILE'`: Type of force specification
    - `CINPUT = NOFILE`: Forces described by simple expression
    - `CINPUT = FILE`: Forces described by time series on file
- `CHFLOA: character(80)`: File name for time series of force components.
    - Dummy if `CINPUT = NOFILE`



### Force component description {#dynmod_e_dynamic_nodal_force}

~~~
LINE-ID ILSEG ILNOD ILDOF CHICOO IFORTY TIMEON TIMEOF P1 P2 P3
~~~

- `LINE-ID: character(8)`: Line identifier
- `ILSEG: integer`: Segment number within actual line
- `ILNOD: integer`: Local node/element number within segment
- `ILDOF: integer`: Degree of freedom within the specified node/element
    - `ILDOF = 7...12` at end 2 of an element
- `CHICOO: character(6)`: Coordinate system code
    - `CHICOO = GLOBAL`: Force component refers to global system, unless the node has skew or vessel boundaries.
      If the node has skew or vessel boundaries, `CHICOO=GLOBAL` means that the load component acts in the skew (vessel) system.
      The force is applied at the specified node.
    - `CHICOO = LOCAL`: Force component refers to local system. The force is applied to the specified element.
- `IFORTY: integer`: Force component type
    - `IFORTY = 1`: Constant force
    - `IFORTY = 2`: Harmonic force
    - `IFORTY = 3`: Ramp
- `TIMEON: real`: Time for switching component on
- `TIMOFF: real`: Time for switching component off
- `P1: real`: Force component parameter
    - `IFORTY = 1`: Magnitude, \f$\mathrm{[F, FL]}\f$
    - `IFORTY = 2`: Amplitude, \f$\mathrm{[F, FL]}\f$
    - `IFORTY = 3`: Force derivative, \f$\mathrm{[F/T, FL/T]}\f$
- `P2: real`: Force component parameter
    - `IFORTY = 1`: Dummy
    - `IFORTY = 2`: Period \f$\mathrm{[T]}\f$
    - `IFORTY = 3`: Dummy
- `P3: real`: Force component parameter
    - `IFORTY = 1`: Dummy
    - `IFORTY = 2`: Phase \f$\mathrm{[deg]}\f$
    - `IFORTY = 3`: Dummy

`IFORTY, TIMEON, TIMEOFF, P1, P2` and `P3` are dummy for `CINPUT = FILE`, time series on file. For file
description, see chapter [Description of Additional Input Files: Dynamic Nodal Forces](@ref dynmod_description_nodal).

For simulation time, t, `TIMEON` <= t <= `TIMOFF` the force component \f$\mathrm{(F)}\f$ will be applied as:
- `IFORTY = 1`: \f$\mathrm{F = P1}\f$
- `IFORTY = 2`: \f$\mathrm{F = P1 \times sin(\frac{2\pi}{P2}\times (t- TIMEON) +P3 \frac{\pi}{180} ) }\f$
- `IFORTY = 3`: \f$\mathrm{F = P1 \times (t - TIMEON)}\f$



## Dynamic tension variation {#dynmod_e_dynamic_tension}



### Data group identifier, one input line {#dynmod_e_dynamic_tension_data}

~~~
DYNAmic TENSion VARIation
~~~



### Specification of dynamic tension variation {#dynmod_e_dynamic_tension_specification}

~~~
SNOD-ID TCX TCV TCA IOPDTV
~~~

- `SNOD-ID: character(8)`: Supernode identifier for dynamic tension variation.
    - Must be identical to the last node-id in stroke storage specification if stroke storage is specified.
- `TCX: real, default: 0`: Coefficient for tension variation due to relative displacement between vessel and riser \f$\mathrm{[F/L]}\f$
- `TCV: real, default: 0`: Coefficient for tension variation due to relative velocity between vessel and riser \f$\mathrm{[FT/L]}\f$
- `TCA: real, default: 0`: Coefficient for tension variation due to relative acceleration between vessel and riser \f$\mathrm{\left[ FT^2/L\right] }\f$
- `IOPDTV: integer, default: 0`: Option for updating tension during iterations (relevant for nonlinear time domain analysis only):
    - `= 0`: Not updated
    - `= 1`: Updated

The resulting dynamic tension is given by:

\f$\mathrm{\Delta T = TCX \times x + TCV \times \dot{x} + TCA \times \ddot{x} }\f$

where \f$\mathrm{x}\f$ is the relative vertical displacement between the vessel and
the riser. The vertical riser displacements are directly available in a
nonlinear time domain analysis. In a linear analysis, the vertical
displacements are estimated from the displacements along lines `ILIN1`
.... `ILINN` (as in linear stroke calculations). [File storage for stroke response](@ref dynmod_e_stroke)
must be given if specification of dynamic tension variation is included.
In both linear and nonlinear analyses platform motions will be
modified for platform setdown if `SETLEN > 0` in 
[File storage for stroke response](@ref dynmod_e_stroke).



## Time domain loading {#dynmod_e_time}



### Data group identifier, one input line {#dynmod_e_time_data}

~~~
TIME DOMain LOADing
~~~



### Load type to be activated, one input line {#dynmod_e_time_load}

~~~
LOTYPE NLSPEC CINPUT CHFLOA IFORM
~~~

- `LOTYPE: character`:
    - `= SEGV`: Segment length variation (Nonlinear analysis only)
    - `= TEMP`: Temperature variation (Nonlinear analysis only)
    - `= PRES`: Pressure variation (Nonlinear analysis only)
    - `= BOUN`: Boundary change (Nonlinear analysis only)
    - `= VIVA`: Harmonic loads from VIVANA (Nonlinear analysis only)
    - `= WINC`: Winch run (Nonlinear analysis only)
    - `= WIND`: Wind event. Only available for `IWITYP=14`, Stationary uniform wind with shear.
    - `= SHUT`: Wind turbine shutdown fault options (Nonlinear analysis only)
    - `= BLAD`: Wind turbine blade pitch fault options (Nonlinear analysis only)
- `NLSPEC: integer, default: See below`: Number of load specification to follow
- `CINPUT: character, default: 'NOFILE'`:
    - `= NOFILE`: All load specification given below
    - `= FILE`: Load specification read from file `CHFLOA`
- `CHFLOA: character, default: See below`: Load specification file.
    - Dummy for `CINPUT = NOFILE`
- `IFORM: integer, default: 1`: File format

For `LOTYPE = VIVA`:
- `NLSPEC = 1, CINPUT=FILE` and `IFORM=1`
- The default value of `CHFLOA` is `<prefix>_ifnviv.ffi`

For `LOTYPE = WIND`:
- `NLSPEC = 1, CINPUT=NOFILE`

For `LOTYPE = SHUT`:
- `NLSPEC = 1, CINPUT=NOFILE`

For `LOTYPE = BLAD`:
- `NLSPEC = 1, CINPUT=NOFILE`



### Segment length variation, NLSPEC input lines for LOTYPE = SEGV {#dynmod_e_time_segment}

~~~
LINE-ID ISEG TBEG TENO SLRATE
~~~

- `LINE-ID: character(8)`: Line identifier
- `ISEG: integer`: Local segment within line `LINE-ID`
- `TBEG: real`: Start time for segment length variation \f$\mathrm{[T]}\f$
- `TEND: real`: End time for segment length variation \f$\mathrm{[T]}\f$
    - `TEND > TBEG`
- `SLRATE: real`: Segment length variation per time unit \f$\mathrm{[L/T]}\f$



### Temperature variation, NLSPEC input lines if LOTYPE = TEMP {#dynmod_e_time_temperature}

~~~
LINE-ID ISEG IEL TBEG TEND TEMP
~~~

- `LINE-ID: character(8)`: Line identifier
- `ISEG: integer/character`: Local segment number within line `LINE-ID`
    - `= 0 / ALL`: All segments in specified line
- `IEL: integer/character`: Local element number within segment `ISEG`
    - `= 0 / ALL`: All elements in specified segment
- `TBEG: real`: Start time for temperature variation \f$\mathrm{[T]}\f$
- `TEND: real`: End time for temperature variation \f$\mathrm{[T]}\f$
    - `TEND > TBEG`
- `TEMP: real`: Temperature at end of temperature variation

The temperature is varied linearly during the load group from the
starting temperature ending with the temperature specified here.

A linear variation of temperature over a sequence of elements may be
specified by giving a negative element number at the second end of the
linear variation.



### Pressure variation, NLSPEC input lines if LOTYPE = PRES {#dynmod_e_time_pressure}

~~~
MRL-ID TBEG TEND PRESSI DPRESS VVELI
~~~

- `MRL-ID: character(8)`: Reference to Main Riser Line identifier
- `TBEG: real`: Start time for pressure variation \f$\mathrm{[T]}\f$
- `TEND: real`: End time for pressure variation \f$\mathrm{[T]}\f$
    - `TEND > TBEG`
- `PRESSI: real, default: 0`: Final pressure at inlet end \f$\mathrm{\left [F/L^2\right ]}\f$
- `DPRESS: real, default: 0`: Final pressure drop \f$\mathrm{\left[ F/L^3\right ]}\f$
- `VVELI: real, default: 0`: Final fluid velocity \f$\mathrm{\left[ L^3/T\right] }\f$
    - Dummy in present version



### Boundary change, 3 x NLSPEC input lines for LOTYPE = BOUN {#dynmod_e_time_boundary}

#### Time for boundary change

~~~
TIMCHG
~~~

- `TIMCHG: real`: Time for boundary change \f$\mathrm{[T]}\f$



#### Identification of node for boundary change

~~~
IREF-ID ILSEG ILNODE IOP
~~~

- `IREF-ID: character(8)`: Reference to line or supernode identifier.
- `ILSEG: integer`: 
   - If `IREF-ID` refers to a line, `ILSEG` is the segment number within this line
   - If `IREF-ID` refers to a supernode, `ILSEG` must be zero
- `ILNODE: integer`: 
   - If `IREF-ID` refers to a line, `ILNODE` is the node number within segment `ILSEG`
   - If `IREF-ID` refers to a supernode, `ILNODE` must be zero
- `IOP: integer`: Parameter for boundary change option
    - `=  0`: Boundary conditions: fixed, pre-scribed or free
    - `= -1`: Boundary conditions: rigid node connection (The node will become a slave node.)

Ordinary (line end) supernodes and SIMO body nodes with `CHLOCA_OPT='POSI'` may have 
boundary change.




#### Status for nodal degrees of freedom if `IOP = 0`

~~~
IPOS IX IY IZ IRX IRY IRZ
~~~

- `IPOS: integer`: Boundary condition type
    - `IPOS = 0`: The node is fixed in global system
    - `IPOS = N`: The node is attached to support vessel no N
- `IX: integer`: Boundary condition code for translation in X-direction
    - `IX = 0`: Free
    - `IX = 1`: Fixed of prescribed
- `IY: integer`: Boundary condition code for translation in Y-direction
    - Same interpretation as for `IX`.
- `IZ: integer`: Boundary condition code for translation in Z-direction
    - Same interpretation as for `IX`.
- `IRX: integer`: Boundary condition code for rotation around X-direction
    - Same interpretation as for `IX`.
- `IRY: integer`: Boundary condition code for rotation around Y-direction
    - Same interpretation as for `IX`.
- `IRZ: integer`: Boundary condition code for rotation around Z-direction
    - Same interpretation as for `IX`.



#### Identification of master node if `IOP = 1`

~~~
LINE-ID ILSEG ILNODE
~~~

- `LINE-ID: character(8)`: Line identifier
- `ILSEG: integer`: Segment number within the actual line
- `ILNODE: integer`: Local node number within segment



### Specification of harmonic loads from VIVANA, one input line for LOTYPE = VIVA {#dynmod_e_time_viv}

~~~
CHFRQ ALIM ISEED TPLOT
~~~

- `CHFRQ: character, default: DOMI`:
    - `= ALL`: All responses frequencies from `VIVANA` included
    - `= AMIN`: Response frequencies with normalized cross-flow response larger
    than `AMIN` included
    - `= DOMI`: Only the dominating response frequency included
- `ALIM: real, default: 0`: Cross-flow displacement to diameter ratio \f$\mathrm{[1]}\f$
    - Dummy for `CHFRQ` \f$ \neq \f$ `ALIM`
- `ISEED: integer, default: 280495`: Seed
- `TPLOT: real, default: 2`: VIV response plot interval. Key VIV results from the last `TPLOT` interval
    of the simulation are stored on the `_dynmod.mpf` file
    - `TPLOT > 0`: Given as number of whole response periods
    - `TPLOT < 0`: Given as time \f$\mathrm{[T]}\f$



### Winch run, NLSPEC input lines for LOTYPE = WINC {#dynmod_e_time_winch}

~~~
IWINCH TBEG TEND WIVEL
~~~

- `IWINCH: integer`: Winch number
- `TBEG: real`: Start time for winch run \f$\mathrm{[T]}\f$
- `TEND: real`: End time for winch run \f$\mathrm{[T]}\f$
- `WIVEL: real`: Winch velocity \f$\mathrm{[L/T]}\f$
    - `WIVEL > 0`: Winching out, i.e. the winch run will increase the active line length.



### Wind event specification, two or three input lines for LOTYPE = WIND {#dynmod_e_wind_event}

In the following IEC 2005 refers to the standard
"IEC 61400-1 Wind turbines – Part 1: Design requirements – 2005".

An IEC 2005 extreme wind event may only be applied to a stationary
uniform wind with shear, `IWITYP=14`.


#### Start time and wind turbine reference

~~~
TIME WIND-TURBINE-ID
~~~

- `TIME: real`: Start time for wind event \f$\mathrm{[T]}\f$
- `WIND-TURBINE-ID: character(8)`: Wind turbine identifier given in `INPMOD`. `NONE` may be given to skip the wind turbine reference for the events ECD, EOG and EDC with `CLASS = NONE`; i.e. detailed specification of event. 


#### Extreme wind event

~~~
CHEVEN CLASS CHDIR
~~~

- `CHEVEN: character(12)`: Extreme wind event. The following values are currently available:
    - `= IEC2005_ECD `: IEC 2005 extreme coherent gust with direction change
    - `= IEC2005_EWSV`: IEC 2005 extreme vertical wind shear
    - `= IEC2005_EWSH`: IEC 2005 extreme horizontal wind shear
    - `= IEC2005_EOG `: IEC 2005 extreme operating gust
    - `= IEC2005_EDC `: IEC 2005 extreme direction change
- `CLASS: character(4)`: Wind turbine class, ref IEC 2005. Legal values are `IA`, `IIA`, `IIIA`, `IB`, `IIB`, `IIIB`, `IC`, `IIC`, `IIIC`, `S` or `NONE`, detailed specification of event parameters.
- `CHDIR: character(4)`: Direction of event. Dummy for `CHEVEN = IEC2005_EOG`.
    - `= POS `: For ECD and EDC, the wind shifts clockwise (viewed from above). For EWSV, the wind increases at the top of the rotor disk and decrease at the bottom. For EWSH, the wind increases on the left side of the rotor disk and decrease on the right side when viewed along the shaft from the hub.
    - `= NEG `: For ECD and EDC, the wind shifts counter-clockwise (viewed from above). For EWSV, the wind decreases at the top of the rotor disk and increases at the bottom. For EWSH, the wind decreases on the left side of the rotor disk and increases on the right side when viewed along the shaft from the hub.
    - `= NONE`: Only allowed for `CHEVEN = IEC2005_EOG`.


#### Additional input for wind turbine class S

If `CLASS = S`, the following additional input line is given:

~~~
VREF IREF
~~~

- `VREF: real`: Reference wind speed average over 10 min \f$\mathrm{[L/T]}\f$
- `IREF: real`: Expected value of the turbulence intensity at 15 m/s \f$\mathrm{[1]}\f$


#### Detailed specification of IEC2005 ECD event

If `CLASS = NONE` and `CHEVEN = IEC2005_ECD`, the following additional input line is given:

~~~
VEL_EVENT DIR_EVENT TIME_EVENT
~~~

- `VEL_EVENT: real, default: 0.0`: Velocity change \f$\mathrm{[L/T]}\f$
- `DIR_EVENT: real, default: 0.0`: Direction change \f$\mathrm{[deg]}\f$
- `TIME_EVENT: real > 0`: Duration of event \f$\mathrm{[T]}\f$


#### Detailed specification of IEC2005 EWSV or EWSH  event

If `CLASS = NONE` and `CHEVEN = IEC2005_EWSV or IEC2005_EWSH`, the following additional input line is given:

~~~
VEL_EVENT TIME_EVENT
~~~

- `VEL_EVENT: real, default: 0.0`: Maximum velocity change at edge of rotor \f$\mathrm{[L/T]}\f$
- `TIME_EVENT: real > 0`: Duration of event \f$\mathrm{[T]}\f$



#### Detailed specification of IEC2005 EOG event

If `CLASS = NONE` and `CHEVEN = IEC2005_EOG`, the following additional input line is given:

~~~
VEL_EVENT TIME_EVENT
~~~

- `VEL_EVENT: real, default: 0.0`: Range of velocity from minimum to maximum during the event \f$\mathrm{[L/T]}\f$
- `TIME_EVENT: real > 0`: Duration of event \f$\mathrm{[T]}\f$


#### Detailed specification of IEC2005 EDC event

If `CLASS = NONE` and `CHEVEN = IEC2005_EDC`, the following additional input line is given:

~~~
DIR_EVENT TIME_EVENT
~~~

- `DIR_EVENT: real, default: 0.0`: Direction change \f$\mathrm{[deg]}\f$
- `TIME_EVENT: real > 0`: Duration of event \f$\mathrm{[T]}\f$


### Wind turbine shutdown fault options {#dynmod_e_wt_shutdown}

The specifications given for turbine shutdown will overrule commanded blade pitch and torque, 
given by the wind turbine control system. Wind turbine blade pitch faults will override the wind 
turbine shutdown options.


#### Start time and wind turbine reference

~~~
TSTART WIND-TURBINE-ID
~~~

- `TSTART: real`: Start time for shutdown \f$\mathrm{[T]}\f$
- `WIND-TURBINE-ID: character(8)`: Reference to wind turbine identifier 

#### Number of pairs in rate of change in pitch and maximum pitch

~~~
NPAIR
~~~

- `NPAIR: integer`: Number of pairs in tabulated rate of pitch change and maximum pitch at the rate of pitch change


#### Rate of change in pitch and maximum pitch at the rate of change in pitch, NPAIR input lines

~~~
RATE  MAX_PITCH
~~~

- `RATE: real`: Rate of change in pitch angle (absolute value) \f$\mathrm{[deg/T]}\f$
    - `RATE > 0`

- `MAX_PITCH: real`: Maximum pitch angle for the rate of change in pitch \f$\mathrm{[deg]}\f$
    - `MAXPITCH > 0`

`MAX_PITCH` values must be given in increasing order.


Example:


Type of shutdown   | Pitch change rate |  Maximum pitch    
------------------ | ----------------- | -----------------
normal             | 1.0 deg/T to      | 90.0 deg   


Example:
    
Type of shutdown   | Pitch change rate |  Maximum pitch    
------------------ | ----------------- | -----------------
open-loop          | 8.0 deg/T to      | 40.0 deg 
 -                 | 4.0 deg/T to      | 90.0 deg


Example:

Type of shutdown   | Pitch change rate |  Maximum pitch    
------------------ | ----------------- | -----------------
emergency          | 8.0 deg/T to      | 90.0 deg



#### Generator torque fault options 

~~~
CHFAULT
~~~
- `CHFAULT: character(6)`:
    - `= NONE  `: No generator torque fault, the calculated generator torque will be applied in full
    - `= LOSS  `: Total loss of generator torque
    - `= BACKUP`: Backup power, generator torque will follow scaled torque control


##### Scale factor for generator torque, One input line for `CHFAULT = BACKUP` 

~~~
SF
~~~
- `SF: real`: Scale factor for generator torque
    - `SF >= 0`


#### Mechanical brake option

~~~
CHBRAKE
~~~
- `CHBRAKE: character(6)`:
    - `= NONE  `: No mechanical brake
    - `= BRAKE `: Mechanical brake (Linear damping)


##### Torque damping coefficient and brake uploading duration, One input line for `CHBRAKE = BRAKE ` 

~~~
TORQUE_DAMP UPL_DURATION
~~~
- `TORQUE_DAMP: real`: Linear torque damping coefficient \f$\mathrm{[FLT/deg]}\f$
    - `TORQUE_DAMP >= 0`
- `UPL_DURATION: real`: Brake uploading duration to full braking torque \f$\mathrm{[T]}\f$
    - `UPL_DURATION >= 0`

***

### Wind turbine blade pitch fault options {#dynmod_e_wt_blade_pitch_fault}

Wind turbine blade pitch faults will override commanded blade pitch given by the wind 
turbine control system or by the wind turbine shutdown options.



#### Wind turbine reference

~~~
WIND-TURBINE-ID
~~~

- `WIND-TURBINE-ID: character(8)`: Reference to wind turbine identifier 


#### Number of blades for fault specification

~~~
NBL_FAULT
~~~

- `NBL_FAULT: integer`: Number of blades for fault specification
    - `NBL_FAULT >= 0`

The subsequent input specification must be given per blade with pitch fault

#### Start time and line (foil blade) reference for fault specification

~~~
TSTART LINE-ID
~~~

- `TSTART: real`: Start time for blade pitch fault \f$\mathrm{[T]}\f$
- `LINE-ID: character(8)`: Reference to line identifier 
 

#### Type of blade pitch fault

~~~
CHFAULT
~~~
- `CHFAULT: character(4)`:
    - `= SEIZ`: Seized - Fixed pitch from time of occurrence
    - `= RUNA`: Runaway - Pitch change rate from time of occurrence to final pitch 
    - `= BIAS`: Actuator bias - Fixed pitch fault from time of occurrence


##### Rate of change in pitch and final pitch, One input line for `CHFAULT = RUNA` 

~~~
RATE  FINAL_PITCH
~~~

- `RATE: real`: Rate of change in pitch (absolute value) \f$\mathrm{[deg/T]}\f$
    - `RATE >= 0`
- `FINAL_PITCH: real`: Final pitch  \f$\mathrm{[deg]}\f$



##### Pitch deviation from required pitch, One input line for `CHFAULT = BIAS` 

~~~
DEL_PITCH UPL_DURATION
~~~

- `DEL_PITCH: real`: Fixed pitch deviation from required pitch \f$\mathrm{[deg]}\f$
- `UPL_DURATION: real`: Bias uploading duration to full pitch deviation \f$\mathrm{[T]}\f$
    - `UPL_DURATION >= 0`






## File storage of displacement response {#dynmod_e_displacement}

Before specifying file storage of response, note that meaningful
output from `OUTMOD` can be dependent on which and how much information
that is stored on file from `DYNMOD`. Examples of such output options in
`OUTMOD` are time series of element angles and distance between elements, see
[Element angle time series from time domain analysis](@ref outmod_c_element) and
[Distance time series calculated from the time domain analyses](@ref outmod_c_distance).

There are limitations in storage capacity due to:
-   Disk/user size
-   Maximum number of arrays that may be stored on the `ifndyn.ffi` file. A message is printed if this
    limit is exceeded. The maximum number of arrays on the file may be changed using the environmental
    variable RIFLEX_MAXDYN_IFNDYN. The minimum value is 50000 and the maximum is 2000000. The default is 200000.



### Data group identifier, one input line {#dynmod_e_displacement_data}

~~~
DISPlacement RESPonse STORage
~~~



### Specification of displacements to be stored {#dynmod_e_displacement_specification}



#### Amount of storage, one input line  {#dynmod_e_displacement_specification_amount}

~~~
IDISP NODISP IDISFM
~~~

- `IDISP: integer`: Code for storage of nodal displacements. Storage for every `IDISP` time
step (`IDISP=2` gives storage for every second step).
- `NODISP: integer > 0`: Number of input lines given specifying node numbers where displacements are
stored.
- `IDISFM: integer, default: 0: integer`: Format code for storage and/or output of nodal displacements.
    - `IDISFM = 0`: Storage only on `ifndyn` file.
    - `IDISFM = 1`: Storage on `ifndyn` file and additional file in ASCII format.
    - `IDISFM = 2`: Storage on `ifndyn` file and additional file in BINARY format.
    - `IDISFM = -1`: Storage only on additional file in ASCII format. Results are not available in `OUTMOD`.
    - `IDISFM = -2`: Storage only on additional file in BINARY format. Results are not available in `OUTMOD`.

Note that data must be stored on the `ifndyn` file in order to be
available for `OUTMOD`.

If `IDISFM`\f$ \neq \f$ `0` is specified, an
additional result file and a key file will be created. The file names
will be based on the name of the `DYNMOD` result file;
`<prefix>_dynmod.res`. An additional ASCII file will be
`<prefix>_noddis.asc` and an additional binary file will be
`<prefix>_noddis.bin`. The key file `key_<prefix>_noddis.txt` will
describe how data is stored on the additional output file. The key file
may be viewed in a text editor.



#### Specification of nodes for displacement storage, NODISP input lines {#dynmod_e_displacement_specification_specification}

~~~
LINE-ID ISEG INOD
~~~

- `LINE-ID: character(8)`: Line identifier
- `ISEG: integer`: Segment number of line
- `INOD: integer/character`: Local node number on actual segment

Consecutively numbered nodes may be specified implicitly by
assigning a negative value to the last of two adjacent `INOD`. In this
case `LINE-ID` and `ISEG` must be the same for the two nodes.

All nodes within one segment may be specified by simply giving `ALL` as
input to `INOD`.



## File storage for internal forces {#dynmod_e_internal}



### Data group identifier, one input line {#dynmod_e_internal_data}

~~~
FORCe RESPonse STORage
~~~



### Specification of forces to be stored {#dynmod_e_internal_specification}



#### Amount of storage, one input line {#dynmod_e_internal_specification_amount}

~~~
IFOR NOFORC IFORFM IELTFM
~~~

- `IFOR: integer`: Code for file storage of internal forces. Forces are stored for every
`IFOR` time step. (`IFOR=3` gives storage for every third step)
- `NOFORC: integer > 0`: Number of input lines given to specify elements for which forces are stored.
- `IFORFM: integer, default: 0`: Format code for storage and / or output of element forces
    - `IFORFM = 0`: Storage only on `ifndyn` file
    - `IFORFM = 1`: Storage on `ifndyn` file and additional file in ASCII format
    - `IFORFM = 2`: Storage on `ifndyn` file and additional file in BINARY format
    - `IFORFM = -1`: Storage only on additional file in ASCII format. Results are not available in `OUTMOD`.
    - `IFORFM = -2`: Storage only on additional file in BINARY format. Results are not available in `OUTMOD`.
- `IELTFM: integer, default: 0`: Format code for or output of element transformation matrices
    - `IELTFM = 0`: No output
    - `IELTFM = ±1`: Output on additional file in ASCII format
    - `IELTFM = ±2`: Output on additional file in BINARY format

Note that data must be stored on the `ifndyn` file in order to be
available for `OUTMOD`.

If `IFORFM`\f$ \neq \f$ `0` is specified, an
additional result file and a key file will be created. The file names
will be based on the name of the `DYNMOD` result file;
`<prefix>_dynmod.res`. An additional ASCII file will be
`<prefix>_elmfor.asc` and an additional binary file will be
`<prefix>_elmfor.bin`. The key file `key_<prefix>_elmfor.txt` will
describe how data is stored on the additional output file. The key file
may be viewed in a text editor.

For nonlinear analysis with pipe-in-pipe elements, the contact forces
will be written to `<prefix>_cntfor.asc` or `.bin` if `IFORFM`\f$ \neq \f$ `0`.
The contents are described on the corresponding key file `key_<prefix>_cntfor.txt`.

Roller contact forces will be stored on separate result files if `IDCOM = LAYFLX`,
see [INPMOD: Selection of riser type and identifier](@ref inpmod_b_riser_type_specification_selection_of_riser) .

If `IELTFM`\f$ \neq \f$ `0` is specified, an
additional result file and a key file will be created. The file names
will be based on the name of the `DYNMOD` result file;
`<prefix>_dynmod.res`. An additional ASCII file will be
`<prefix>_elmtra.asc` and an additional binary file will be `<prefix>_elmtra.bin`. The key file `key_<prefix>_elmtra.txt` will describe how
data is stored on the additional output file. The key file may be viewed in a text editor.



#### Specification of elements for force storage, NOFORC input lines {#dynmod_e_internal_specification_specification}

~~~
LINE-ID ISEG IEL
~~~

- `LINE-ID: character(8)`: Line identifier
- `ISEG: integer`: Local segment number within line `LINE-ID`
- `IEL: integer/character`: Local element number within segment `ISEG`
    - `= ALL`: All elements in specified segment

Consecutively numbered elements may be specified implicitly by
assigning a negative value to the last of two adjacent elements, `IEL`. In
this case `LINE-ID` and `ISEG` must be the same for the two elements.

All elements within one segment may be specified by simply giving `ALL` as
input to `IEL`.



## File storage for curvature response {#dynmod_e_curvature}

Curvature estimates based on nodal displacements may be generated by
`OUTMOD` (see [Curvature time series calculated from dynamic nodal displacements](@ref outmod_c_curvature_nodal)) even though curvatures are not
stored from `DYNMOD`.



### Data group identifier, one input line {#dynmod_e_curvature_data}

~~~
CURVature RESPonse STORage
~~~



### Specification of curvature to be stored {#dynmod_e_curvature_specification}



#### Amount of storage, one input line {#dynmod_e_curvature_specification_amount}

~~~
ICURV NOCURV ICURFM
~~~

- `ICURV: integer`: Code for storage of curvature response. Curvature is stored for every `ICURV` time
step
- `NOCURV: integer > 0`: Number of input lines given to specify elements for which curvatures are stored.
- `ICURFM: integer, default: 0: integer`: Format code for storage and/or output of element curvature.
    - `ICURFM = 0`: Storage only on `ifndyn` file.
    - `ICURFM = 1`: Storage on `ifndyn` file and additional file in ASCII format.
    - `ICURFM = 2`: Storage on `ifndyn` file and additional file in BINARY format.
    - `ICURFM = -1`: Storage only on additional file in ASCII format. Results are not available in `OUTMOD`.
    - `ICURFM = -2`: Storage only on additional file in BINARY format. Results are not available in `OUTMOD`.

Note that data must be stored on the `ifndyn` file in order to be
available for `OUTMOD`.

If `ICURFM`\f$ \neq \f$ `0` is specified, an
additional result file and a key file will be created. The file names
will be based on the name of the `DYNMOD` result file;
`<prefix>_dynmod.res`. An additional ASCII file will be
`<prefix>_elmcur.asc` and an additional binary file will be
`<prefix>_elmcur.bin`. The key file `key_<prefix>_elmcur.txt` will
describe how data is stored on the additional output file. The key file
may be viewed in a text editor.



#### Specification of elements for curvature storage, NOCURV input lines {#dynmod_e_curvature_specification_specification}

~~~
LINE-ID ISEG IEL
~~~

- `LINE-ID: character(8)`: Line identifier
- `ISEG: integer`: Local segment number within line `LINE-ID`
- `IEL: integer/character`: Local element number within segment `ISEG`
    - `= ALL`: All elements in specified segment

Consecutively numbered elements may be specified implicitly by
assigning a negative value to the last of two adjacent elements, `IEL`. In
this case `LINE-ID` and `ISEG` must be the same for the two elements.

All elements within one segment may be specified by simply giving `ALL` as
input to `IEL`.



## Envelope curve specification {#dynmod_e_envelope}

This data group enables the user to compute envelopes from both regular
and irregular analysis. For irregular analysis mean and standard
deviation of response will be printed on the _dynmod.res file.


### Data group identifier, one line {#dynmod_e_envelope_data}

~~~
ENVElope CURVe SPECification
~~~



### Specification {#dynmod_e_envelope_specification}



#### Options for calculation and printing {#dynmod_e_envelope_specification_options}

~~~
IENVD IENVF IENVC TENVS TENVE NPREND NPRENF NPRENC IFILMP
~~~
- `IENVD: integer, default: 1`: Calculation option for displacement envelopes
    - `= 0`: not calculated
    - `= 1`: calculated
- `IENVF: integer, default: 1`: Calculation option for force envelopes
    - `= 0`: not calculated
    - `= 1`: calculated
- `IENVC: integer, default: 1`: Calculation option for curvature envelopes
    - `= 0`: not calculated
    - `= 1`: calculated
- `TENVS: real`: Simulation start time for calculating envelopes \f$\mathrm{[T]}\f$
- `TENVE: real, default:` \f$10^{6}\f$: Simulation end time for calculating envelopes \f$\mathrm{[T]}\f$
- `NPREND: integer, default: 0`: Print option for displacement envelopes
    - `= 0`: Not printed
    - `= 1`: print
- `NPRENF: integer, default: 0`: Print option for force envelopes
    - `= 0`: not printed
    - `= 1`: print
- `NPRENC: integer, default: 0`: Print option for curvature envelopes
    - `= 0`: not printed
    - `= 1`: print
- `IFILMP: integer, default: 2`: MatrixPlot file option; specifies amount of results written to the file `<prefix>_dynmod.mpf`. `0 <= IFILMP <= 4`.
    - `= 0`: No print
    - `= 1`: Minimum values, maximum values and standard deviations
    - `= 2`: Minimum values, maximum values and standard deviations (identical to specifying `IFILMP = 1`)
    - `= 3`: Minimum values, maximum values, standard deviations, mean values and mean-crossing periods
    - `= 4`: Minimum values, maximum values, standard deviations, mean values, mean-crossing periods, skewness and kurtosis


Note that the mean-crossing period, skewness and kurtosis will be
inaccurate for time series with constant or near constant values.


## File storage for stroke response {#dynmod_e_stroke}

The stroke is stored for presentation and / or post-processing in `OUTMOD`



### Data group identifier, one input line {#dynmod_e_stroke_data}

~~~
STROke RESPonse STORage
~~~



### Specification of stroke calculation and storage {#dynmod_e_stroke_specification}

~~~
ISTRO SNOD-ID IOPSTR SETLEN XRSTRO YRSTRO NLINST LINE-ID1 .. LINE-IDnlinst
~~~

- `ISTRO: integer, default: 1`: Code for storage of stroke response. Storage for every `ISTRO` time step
(`ISTRO=2` gives storage for every second step)
- `SNOD-ID: character(8)`: Supernode identifier for stroke calculation
- `IOPSTR: integer, default: 0`: Option for reference coordinates
    - `= 0`: Initial stressfree configuration used as reference
    - `= 1`: Final static configuration used as reference (under implementation)
- `SETLEN: real, default: 0`: Tendon length for set-down correction
- `XRSTRO: real, default: 0`: Global X coordinate of node `INODST`’s reference point for set-down calculations.
    - Dummy of `SETLEN = 0`.
- `YRSTRO: real, default: 0`: Global Y coordinate of node `INODST`’s reference point for set-down calculations.
    - Dummy of `SETLEN = 0`.
- `NLINST: integer, default: 0`: Number of lines used in calculating stroke
    - Dummy for nonlinear analysis
- Lines (line identifiers) used in stroke calculation
    - Dummy for nonlinear analysis
    - `LINE-ID1: character(8)`:
    - .
    - .
    - .
    - `LINE-IDnlinst: character(8)`:

Stroke may only be calculated for supernodes. No set-down correction if `SETLEN = 0.0`



## File storage for sum forces {#dynmod_e_sum}

The element sum forces are the sum of the stiffness, damping and
inertia forces. The sum force in the local axial direction will be stored for each specified element.



### Data group identifier, one input line {#dynmod_e_sum_data}

~~~
SUMFORCe RESPonse STORage
~~~



### Specification of forces to be stored {#dynmod_e_sum_specification}



#### Amount of storage, one input line {#dynmod_e_sum_specification_amount}

~~~
ISFOR NOSFOR ISFOFM
~~~

- `ISFOR: integer`: Code for file storage of sum forces. Forces are stored for every `ISFOR` time
step (`ISFOR=3` gives storage for every third step)
- `NOSFOR: integer > 0`: Number of input lines given to specify elements for which sum forces are stored.
- `ISFORM: integer, default: -1: integer`: Format code for storage and/or output of sum element forces.
    - `ISFORM = -1`: Storage on additional file in ASCII format only.
    - `ISFORM = -2`: Storage on additional file in BINARY format only.

This data group is available for nonlinear time domain analysis only.

If `ISFORM`\f$ \neq \f$ `0` is specified, an
additional result file and a key file will be created. The file names
will be based on the name of the `DYNMOD` result file;
`<prefix>_dynmod.res`. An additional ASCII file will be
`<prefix>_elmsfo.asc` and an additional binary file will be
`<prefix>_elmsfo.bin`. The key file `key_<prefix>_elmsfo.txt` will
describe how data is stored on the additional output file. The key file
may be viewed in a text editor.



#### Specification of elements for force storage, NOSFOR input lines {#dynmod_e_sum_specification_specification}

~~~
LINE-ID ISEG IEL
~~~


- `LINE-ID: character(8)`: Line identifier
- `ISEG: integer`: Local segment number within line `LINE-ID`
- `IEL: integer/character`: Local element number within segment `ISEG`
    - `= ALL`: All elements in specified segment

Consecutively numbered elements may be specified implicitly by
assigning a negative value to the last of two adjacent elements, `IEL`. In
this case `LINE-ID` and `ISEG` must be the same for the two elements.

All elements within one segment may be specified by simply giving `ALL` as
input to `IEL`.



## File storage for wind turbine responses {#dynmod_wt_resp}

This option enables export of wind turnine key responses to file in binary or ASCII format

### Data group identifier, one input line {#dynmod_wt_resp_id}

~~~
TURBine RESPonse STORage
~~~

#### Time interval for storage, one input line {#dynmod_wt_dt}

~~~
DT_WTR
~~~

- `DT_WTR: real`: Desired time interval for storage [T]
    - `DT_WTR = 0`: Storage at each simulation time step

Note that `DT_WTR ` will be adjusted to get an integer ratio between the simulation time step  `DT` 
and the specified storage interval `DT_WTR`.


#### Amount of storage, one input line {#dynmod_no_wt}

~~~
NOTURB ITURBFM
~~~

- `NOTURB: integer`: Number of wind turbines for storage 
- `ITURBFM: integer`: File format code for storage
    - `ITURBFM = 1`: Storage on file in ASCII format.
    - `ITURBFM = 2`: Storage on file in binary format.

Note that `NOTURB` has to be set to 1 in present program version

The wind turbine responses are written to `<prefix>_witurb.asc` or
`<prefix>_witurb.bin`. 

The contents are described in `key_<prefix>_witurb.txt` 



#### Wind turbine identification for storage, `NOTURB` input lines {#dynmod_wt_id}

~~~
TURB-ID
~~~

- `TURB-ID: character(8)`: Wind turbine identifier

## File storage for wind turbine blade responses {#dynmod_wtbl_resp}

This option enables export of wind turbine blade responses to file in binary or ASCII format.

### Data group identifier, one input line {#dynmod_wtbl_resp_id}

~~~
WTBLade RESPonse STORage
~~~

#### Specification of the amount of responses, one input line {#dynmod_wtblresp_amount}

~~~
AMOUNT
~~~

- `AMOUNT: character(3)`: Amount of blade responses storage
    - `AMOUNT = MIN`: Minimum amount of responses:
                    - Drag and lift force intensities in foil system
                    - Relative wind velocity in foil system
                    - Angle of attack in foil system
    - `AMOUNT = MED`: Medium amount of responses. In addition to minimum amount:
                    - Drag-, lift and moment coefficients in foil system
                    - Induced wind speed in foil system
                    - Remote incoming wind speed including tower effect in foil system
                    - Separation point position in foil system
                    - Axial and tangential induction factors in rotor system
                    - Axial and tangential load intensities in rotor system
                    - Annulus average axial- and tangential induction velocity
    - `AMOUNT = MAX`: Maximum amount of responses. In addition to medium amount:
                    - Transformation matrix between foil and rotor systems
   


#### Time interval for storage, number of input lines and file format code, one input line {#dynmod_wtbl_dt}

~~~
DT_TBR  NOSPEC  IBLADFM
~~~

- `DT_TBR: real`: Desired time interval for storage [T]
    - `DT_TBR = 0`: Storage at each simulation time step
- `NOSPEC: integer > 0`: Number of input lines given to specify elements for which blade responses  are stored.
- `IBLADFM: integer`: File format code for storage
    - `IBLADFM = 1`: Storage on file in ASCII format. 
    - `IBLADFM = 2`: Storage on file in binary format.

Note that `DT_TBR ` will be adjusted to get an integer ratio between the simulation time step  `DT` 
and the specified storage interval `DT_TBR`.

The wind turbine responses are written to `<prefix>_blresp.asc` or
`<prefix>_blresp.bin`. <

The contents are described in `key_<prefix>_blresp.txt` 


#### Specification of elements for blade response storage, NOSPEC input lines {#dynmod_noblres_iel}

~~~
LINE-ID  ISEG  IEL
~~~

- `LINE-ID: character(8)`: Line identifier
- `ISEG: integer/character`: Local segment number within line `LINE-ID`
- `IEL: integer/character`: Local element number within segment `ISEG`


All elements within the line may be specified by simply giving `ALL` as
input to `ISEG`. Thus `IEL` will be dummy input. 

All elements within one segment may be specified by giving `ALL` as
input to `IEL`.





## Export of element responses {#dynmod_e_export}

This option enables export of element responses for subsequent
communication with general advanced animation tools. The instruction is
applicable for non-linear dynamic analysis only.

### Data group identifier, one input line {#dynmod_e_export_data}

~~~
STORe VISUalisation RESPonses
~~~



### Amount of response storage and file format, one input line {#dynmod_e_export_amount}

~~~
TCONDS TCONDE DELT CHFORM
~~~

- `TCONDS: real, default: 0`: Start time for export
- `TCONDE: real, default:` \f$ 10^5\f$: End time for export
- `DELT: real, default: See below`: Time increment for export
- `CHFORM: character`:
    - `= VIS`: Export to file format used by the computer program SIMVIS for response visualization subsequent to dynamic analysis
    - `= RAF`: Export to file format of type RAF

Default values of `DELT`:
- `DTWF`: Time increment used for pre-sampling of irregular waves and prescribed motions
- `DT`: Time increment used in time integration for regular analysis



### Detailed specification of exported element responses {#dynmod_e_export_detailed}

This data group is optionally given for `CHFORM = VIS`

In present version it is possible to specify element responses in form
of effective tension, resulting curvature and longitudinal stress (if
available). By default all available element responses for all lines
will be exported. This input line makes it possible limit or specify
response types for selected lines in the system.



Number of input lines: as many as necessary.
~~~
OPTION CHRESP CHILIN
~~~

- `OPTION: character`:
    - `= STORE`
    - `= NOSTORE`
- `CHRESP: character`: Response type to be exported
    - `= EFF-AX-FORCE`: Effective tension
    - `= RES-CURV`: Resultant curvature
    - `= LONG-STRESS`: Longitudinal stress
    - `= ALL`: All of the above described responses
- `CHILIN: character`:
    - `= LINE-ID`: Line identifier
    - `= ALL`: All lines



## Termination of input data {#dynmod_e_termination}

To terminate an input data stream, simply give the following, which is
interpreted as a data-group identifier.

~~~
END
~~~



# Description of Additional Input Files {#dynmod_description}



## Dynamic Current Variation {#dynmod_description_current}

The file "CHFCUR" specified in [Dynamic current variation](@ref dynmod_e_dynamic_current),
contains the description of dynamic current variation. The file is a
free format sequential ASCII-file.

The current velocity and direction have to be specified at all levels
defined in the preceding static analysis. The static current profile is
interpreted as the current profile at time equal to zero. The dynamic
current profile is described at an arbitrary number of time instants,
given by increasing values. Linear interpolation is used for
intermediate values. If the last defined time instant is exceeded during
simulation, the current profile is assumed constant and equal to the
last specification for the continued simulation.



File description

### Number of specified time instants, one input line {#dynmod_description_current_number}

~~~
NDYCUR
~~~

- `NDYCUR: integer > 1`: The number of time instants for which current profile is given.

The input data in 'Number of levels and time instant, one input line' and
'Current velocity and direction, one input line per current level, i.e.
NLCUR input lines' (below) must be given in one block for each defined time instant.



#### Number of levels and time instant, one input line {#dynmod_description_current_number_levels}

~~~
NLCUR TIMDCU
~~~

- `NLCUR: integer`: Number of levels in current profile. The number of levels has to be
equal the number used in the preceding static analysis
- `TIMDCU: real > 0`: Time instant for the specified current profile \f$ \mathrm{[T]} \f$



#### Current velocity and direction, one input line per current level, i.e. NLCUR input lines {#dynmod_description_current_number_velocity}

~~~
CURDIR CURVEL CURVEZ
~~~

- `CURDIR: real`: Direction of current velocity.
    - The angle is measured in degrees from global x-axis counter clockwise to the current vector, confer [Current parameters](@ref inpmod_d_current)
- `CURVEL: real, default: 0`: Current velocity \f$ \mathrm{[L/T]} \f$
- `CURVEZ: real, default: 0`: Vertical current velocity \f$ \mathrm{[L/T]} \f$



## Dynamic Nodal Forces {#dynmod_description_nodal}

The file "CHFLOA" specified in [Dynamic nodal forces](@ref dynmod_e_dynamic_nodal), 
contains the description of dynamic nodal load components;
i.e. user-deined external dynamic loads given as time series. The file
is a free format sequential ASCII-file. Two alternative formats are
available; the original format with multiple input lines for each time
instant loads are specified for and the column format with one line
for each time instant loads are specified for. The first input line in
the file is used to determine which format the file is read in. If
only one number is found on the first input line, the file is read
using the original format. If more than one number is found, the file
is read using the column format.

The dynamic nodal load components are described by values at specified
time instants, which must be increasing. Intermediate values are found
by linear interpolation. Between the start of the simulation and the
first time instant with specified loads, the loads are linearly
increased from zero to the first values given. If the simulation
continues after the last defined time instant, the nodal load components
are kept constant at the last values given.

The number of nodal load components, location and direction are
defined in [Dynamic nodal forces](@ref dynmod_e_dynamic_nodal). This
data group also defines the order in which the load components are to
be specified on the file.


### File description - original format

### Number of specified time instants, one input line {#dynmod_description_nodal_number}

~~~
NTDFO
~~~

- `NTDFO: integer >= 1`: Number of time instants for which nodal load components are specified.

The input data in 'Number of load components and time instant, one input line' and 'Load components, MDCOMP input lines'
(below) must be given in one block for each defined time instant.



### Number of load components and time instant, one input line {#dynmod_description_nodal_number__load1}

~~~
MDCOMP TIMDFO
~~~

- `MDCOMP: integer`: Number of load components.
    - Used for control: `MDCOMP = NDCOMP`
    - `NDCOMP` is specified in [Dynamic nodal forces](@ref dynmod_e_dynamic_nodal)
- `TIMDFO: real > 0`: Time instant for the specified load components \f$ \mathrm{[T]} \f$



### Load components, MDCOMP input lines {#dynmod_description_nodal_number_load2}

~~~
RLMAG
~~~

- `RLMAG: real`: Magnitude of load component \f$ \mathrm{[F]} \f$, \f$ \mathrm{[FL]} \f$

### File description - column format

### Time Step and Load Components, one line for each time step {#dynmod_description_nodal_number_load2_col}

~~~
TIMDFO  RLMAGi ..... RLMAGn
~~~

- `TIMDFO: real > 0`: Time instant for the specified load components \f$ \mathrm{[T]} \f$
- `RLMAGi: real`: Magnitude of load component \f$ \mathrm{[F]} \f$, \f$ \mathrm{[FL]} \f$

`RLMAGi` must be repeated  n=`MDCOMP` times.

## Diffracted Wave Transfer Functions at Points {#dynmod_description_wave}

The file "CHFDIF" specified in [Irregular Waves](@ref dynmod_d_irregular_waves) contains the
wave kinematics transfer functions.



### Data group identifier, one input line {#dynmod_description_wave_identification_data}

~~~
FIRSt ORDEr DIFFracted wave transfer functions
~~~



### Text describing the linear incoming wave to diffracted wave transfer functions, two input lines {#dynmod_description_wave_identification_text}

~~~
TXDI1
~~~

- `TXDI1: character(60)`: Character string



### Point reference, one input line {#dynmod_description_wave_identification_point1}

~~~
PTNOUS IVES
~~~

- `PTNOUS: integer`: Point number defined by user
- `IVES: integer`: Support vessel number



### Point coordinates, one input line {#dynmod_description_wave_identification_point2}

~~~
XBDY YBDY ZBDY
~~~

- `XBDY: real`: x-coordinate of where transfer function is calculated, given in support
vessel coordinate system \f$ \mathrm{[L]} \f$
- `YBDY: real`: y-coordinate of where transfer function is calculated, given in support
vessel coordinate system \f$ \mathrm{[L]} \f$
- `ZBDY: real`: z-coordinate of where transfer function is calculated, given in support
vessel coordinate system \f$ \mathrm{[L]} \f$



### Dimensioning parameters, one input line {#dynmod_description_wave_identification_dimensioning}

~~~
NDIR NFRE ITYPIN
~~~

- `NDIR: integer`: Total number of wave directions (for this point)
- `NFRE: integer`: Total number of frequencies (for this point)
- `ITYPIN: integer`: Code for which format the transfer functions are given in
    - `= 1`: Complex form
    - `= 2`: Amplitude ratio \f$ \mathrm{[1]} \f$ and phase \f$ \mathrm{[deg]} \f$
    - `= 3`: Amplitude ratio \f$ \mathrm{[1]} \f$ and phase \f$ \mathrm{[rad]} \f$



### Data identification, one input line {#dynmod_description_wave_unknown1_data}

~~~
WAVE DIREctions DIFFracted wave transfer functions
~~~



### Directions, NDIR input lines {#dynmod_description_wave_unknown1_directions}

~~~
IDIR DIR
~~~

- `IDIR: integer`: Direction number (between 1 and `NDIR`)
- `DIR: real`: Propagation direction of incoming wave, \f$ \mathrm{[deg]} \f$



### Data identification, one input line {#dynmod_description_wave_unknown2_data}

~~~
WAVE FREQuencies DIFFracted wave transfer functions
~~~



### Frequencies, NFRE input lines {#dynmod_description_wave_unknown2_frequencies}

~~~
IFRE FRE
~~~

- `IFRE: integer`: Frequency number (between 1 and `NFRE`)
- `FRE: real`: Angular frequency of incoming wave, \f$ \mathrm{[rad/T]} \f$



### Data identification, one input line {#dynmod_description_wave_unknown3_data}

~~~
WAVE ELEVation DIFFracted wave transfer function
~~~

or

~~~
XVELocity DIFFracted WAVE transfer function
~~~

~~~
YVELocity DIFFracted WAVE transfer function
~~~

~~~
ZVELocity DIFFracted WAVE transfer function
~~~



### Diffracted wave transfer function, NDIR x NFRE input lines {#dynmod_description_wave_unknown3_ddimensioning}

~~~
IDIR IFRE A B
~~~

- `IDIR: integer`: Direction number
- `IFRE: integer`: Frequency number
- `A: real`: Interpretation according to value of `ITYPIN`
    - `ITYPIN = 1`: Real part
    - `ITYPIN = 2`: Amplitude ratio \f$ \mathrm{[1],[rad/m]} \f$
    - `ITYPIN = 3`: Amplitude ratio \f$ \mathrm{[1],[rad/m]} \f$
- `B: real`: Interpretation according to value of `ITYPIN`
    - `ITYPIN = 1`: Imaginary part
    - `ITYPIN = 2`: Phase angle \f$ \mathrm{[deg]} \f$
    - `ITYPIN = 3`: Phase angle \f$ \mathrm{[rad]} \f$

Transfer functions for accelerations will be calculated based on
velocity transfer functions



## Internal flow description {#dynmod_description_internal}

The file "CHFFLW" specified in [Import of internal flow data from file (Deprecated functionality)](@ref dynmod_e_import)
contains a description of the time-varying internal flow.

### Heading, one input line {#dynmod_description_internal_heading}

- `<TEXT>: character(78)`:

The heading will be echoed on the `<prefix>_dynmod.res` result file.



### Specification of internal flow conditions. {#dynmod_description_internal_specification}

Data groups 'Specification of time...' and 'Specification of flow conditions...' (below) are repeated as many times as necessary. At least two time steps must be given.



#### Specification of time, one input line {#dynmod_description_internal_specification_time}

~~~
CHIDEN TIME
~~~

- `CHIDEN: character(4)`:
    - `= TIME`
- `TIME: real`: Time for the following specified flow conditions



#### Specification of flow conditions, as many input lines as needed. (Zero input lines may be given.) {#dynmod_description_internal_specification_flow}

~~~
IFE1 IFE2 DEN VEL
~~~

- `IFE1: integer`: First flow element with these conditions
- `IFE2: integer`: Last flow element with these conditions
- `DEN: real`: Density of contents \f$ \mathrm{\left[ M/L^3 \right]} \f$
- `VEL: real`: Velocity of contents \f$ \mathrm{[L/T]} \f$

The elements in the MRL(s) are numbered consecutively along the MRL. A
table of the flow element numbering may be found on the `<prefix>_stamod.res` file.



### End, one input line {#dynmod_description_internal_end}

~~~
END
~~~
