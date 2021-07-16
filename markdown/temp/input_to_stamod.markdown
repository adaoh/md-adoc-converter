# Input to STAMOD




## General Information {#stamod_general_information}

The input to the `STAMOD MODULE` is divided into 3 main sections, referred
to ass

-   [Data Group A: Control Information] (@ref stamod_a)
-   [Data Group B: Static Analysis with Fixed Parameters] (@ref stamod_b)
-   [Data Group C: Static Analysis with Parameter Variation] (@ref stamod_c)

Theoretical description of the static analysis procedures is given in
the chapters 'Static Catenary Analysis ' and 'Static Finite Element Analysis ' in the `RIFLEX` Theory Manual. Guidance to static analysis is
given in the 'Guidance to Static Analysis' section of the 'Static Finite Element Analysis' part of the `RIFLEX` Theory Manual.


## Note: Static Analysis with Fixed Parameters and Parameter Variation {#stamod_gen_comment}

In static analysis with fixed parameters, loads types can be activated by the user specified input.
For specification of the load types, see data group identfier [LOAD GROUP DATA] (@ref stamod_b_incremental_load_data). 

In static analysis with parameter variation, loads types are activated using the
 data group identfier [PARAmeter VARIation DEFInition] (@ref stamod_c_parameter_number). 
The loads that can be activated by user specification are

- Static offset variation
- Current variation
- Specified force variation
- Bottom friction forces
- Global springs
- Material memory function
- Boundary change

In addition, a set of load types are automatically activated using the  data group identfier
 [PARAmeter VARIation DeFInition] (@ref stamod_c_parameter_number). These loads types are
- Volume forces
- Tensioner forces
- Roller contact forces
- Initail stressed elements
- Floater forces


Note that if current, wind and specfied force are specified in `STAMOD` but not activated using the 
data group identfier [LOAD GROUP DATA] (@ref stamod_b_incremental_load_data), current load, wind load 
and specified force will be applied in `DYNMOD`. 
Volume forces will be activated i `DYNMOD` if not activated by using the data group identfier `LOAD GROUP DATA`.



## Data Group A: Control Information {#stamod_a} 

This data group is mandatory for all types of analysis with `STAMOD`.




### Principal run parameters {#stamod_a_principal}




#### Data group identifier, one input line {#stamod_a_principal_data}

~~~
STAMod CONTrol INFOrmation CHVERS
~~~

- `CHVERS: character(8)`: `RIFLEX` input file version, e.g. 3.6




#### Heading, three input lines {#stamod_a_principal_heading}

Identification of the run alphanumerical text. This text will be output when running `STAMOD`.

~~~
 HEAD1 HEAD2 HEAD3
~~~

- `HEAD1: character`: Line 1 of heading text 
- `HEAD2: character`: Line 2 of heading text 
- `HEAD3: character`: Line 3 of heading text 

Always 3 input lines which may all be blank




#### Options and print switches, one input line {#stamod_a_principal_options}

~~~
IRUNCO IDRIS IANAL IPRDAT IPRCAT IPRFEM IPFORM IPRNOR IFILFM IFILCO
~~~

- `IRUNCO: integer, default: 0`: Run code for data check or executable run
    - `IRUNCO = 0`: Data check run
    - `IRUNCO = 1`: Analysis run
    - `IRUNCO = 2`: Restart analysis. The data group 'Specification of restart run' must be given subsequent to this input line 
- `IDRIS: character(6)`: Data set identifier corresponding to data for one riser system established by `INPMOD`  
- `IANAL: integer`: Type of analysis to be performed
    - `IANAL = 1`: Static analysis. Data group B must be provided for this analysis 
    - `IANAL = 2`: Static analysis with parameter variation. Data groups B and C must be provided
- `IPRDAT: integer, default: 2`: Print switch for the amount of output from the data generation
    - `IPRDAT=1`: Only identifiers and a few key data are printed
    - `IPRDAT>2`: Tabulated print of system and environmental data (recommended)
    - `IPRDAT=-5`: Print of system presented by segment and print of environment data
- `IPRCAT: integer, default: 1`: Print switch for the amount of output from the catenary analysis
    - `IPRCAT=1`: Gives print of final catenary solution
    - `IPRCAT=5`: Gives in addition print of stress free configuration
    - `IPRCAT=10`: Gives in addition print of the catenary iteration (for debug purposes)
- `IPRFEM: integer, default: 1`: Print switch for the amount of output from `FEM` analysis
    - `IPRFEM=1`: Results are printed for the equilibrium configuration at the end of the 
    final static load step. If the analysis includes parameter variation, results are
    also printed after the final parameter variation load step. 
    - `IPRFEM=5`: Results are printed for equilibrium configurations at the end of each load group
    - `IPRFEM=10`: Results are printed for the equilibrium configurations at every load step
- `IPFORM: integer, default: 1`: Format for print of `FEM` results
    - `IPFORM=-1`: Debug format
    - `IPFORM=1`: Results are presented line by line. Moments and curvatures are given at both element ends
    - `IPFORM=2`: Results are presented line by line. Moments and curvatures are averaged at internal line nodes. 
    Results at element ends are used at line ends (similar to `OUTMO ` processing)
    - `IPFORM=3`: Results are presented segment by segment. Moments and curvatures are averaged at internal
    segment nodes. Results at element ends are used at segment ends.
- `IPRNOR: integer, default: 1`: Print switch for convergence norms in static `FEM` analysis
    - `IPRNOR=0`: No output of convergence norms
    - `IPRNOR=1`: Print of convergence norms 
- `IFILFM: integer, default: 2`: Option for Matrix Plot file 
    - `IFILFM=0`: No print
    - `IFILFM` $\mathrm{\neq }$ `0`: Matrix Plot file named `<prefix>_stamod.mpf`
    (`IPRFEM` controls how often static key results are written to the Matrix Plot file)
- `IFILCO: integer, default: 0`: Print switch for storing system configuration to ascii files. 
Initial configuration used for FE-analysis and configurations after each load-group during the loading sequence are stored. 
The stored configurations may be used as start configuration for subsequent `STAFEM`-analysis.
    - `IFILCO=0`: No additional files
    - `IFILCO=1`: 
        - Configurations stored to ASCii files:
            - `<prefix>_config-lg<i>`
              where the number `<i>` indicates the load group number. 
        - For configurations after parameter variation the files are named:
            - `<prefix>_config-lg<i>-<n>` where `<n>` is the step number

Note that projection angles will only be printed to `<prefix>_stamod.res` for lines that consist of bar elements.


#### Specification of restart run {#stamod_a_principal_specification}

These input lines are only given for a restart run of `STAMOD` (`IRUNCO=2`
in the previous data group, 'Options and print switches, one input line'), and should
be given subsequent to `STAMOD CONTROL INFORMATION`.

Restart of `STAMOD` makes it possible to continue computation from the
last successful load group.

A restart run of `STAMOD` requires two data files from the previous run:

- `IFNDMP` which contains the entire work array
- `IFNSTA` which contains the results to be processed by `OUTMOD`

During a run of `STAMOD`, the entire work array (all data in core) will be
written to file `IFNDMP` at the end of each completed load group. The file
is overwritten each time, so the content is always related to the last
(successful) load group. Therefore a restart will normally start with
the next load group. In case of restart from parameter variations, the
analysis will continue with the next parameter variation step. This
makes the parameter variation more flexible as the user can choose to
vary one parameter at a time.

It is also possible to carry out several runs with parameter variations
from the same static equilibrium configuration. The procedure to be used
in this case is illustrated through the following example:

1) Run `STAMOD` in a normal way, (`IANAL=1`). A file prefix of SA_ is
inserted for the example.

2) Make a copy of the files SA_IFNDMP.SAM and SA_IFNSTA.FFI to e.g.
BACKUP.SAM and BACKUP.FFI, respectively.

3) Run restart with parameter variations, (`IANAL=2`).

4) Now, a new restart can be made from the original static equilibrium
configuration by copying BACKUP.SAM and BACKUP.FFI to SA_IFNDMP.SAM and
SA_IFNSTA.FFI prior to execution.

The procedure with backup of files can easily be automated in a run
command procedure.

Note that current must be present in the original run if restart with
parameter variation of current data is specified. Otherwise, the
original current will be loaded in the first parameters variation step.

~~~
RESTart PARAmeters STAMod 
~~~

~~~
IDSTA
~~~

- `IDSTA: character(6)`: Identifier for original static analysis results




### Data set identifier for present analysis {#stamod_a_data}




#### Data group identifier, one input line {#stamod_a_data_group}

~~~
RUN IDENtification 
~~~




#### Data set identifier for results, one input line {#stamod_a_data_set}

~~~
IDRES
~~~

- `IDRES: character(6)`: Data set identifier for this run




### Identifier of environment data {#stamod_a_identifier}




#### Data group identifier, one input line {#stamod_a_identifier_data}

~~~
ENVIronment REFErence IDENtifier
~~~




#### Identifier of environment data, one input line {#stamod_a_identifier_identifier}

~~~
IDENV
~~~

- `IDENV: character(6)`: Identifier of environment data given as input to the `INPMOD` module

This data group is dummy for coupled analysis.




### Export of element responses, one input line {#stamod_a_export}

This specification is optional. Specifying export of element responses
enables visualization of the incremental loading configurations by use
of the computer program `SIMVIS` subsequent to static analysis. In present
version it is possible to specify element responses in form of effective
tension, resulting curvature and longitudinal stress (if available).

~~~
STORe VISUalisation RESPonses 
~~~




#### Detailed specification of exported element responses {#stamod_a_export_detailed}

This data group is optional.

By default effective tension for all lines will be exported. This input
line makes it possible to limit or specify response types for selected
lines in the system.

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
    - `= LINE-ID`: Reference to line identifier
    - `= ALL`: All lines




## Data Group B: Static Analysis with Fixed Parameters {#stamod_b}

This section is mandatory, and the analysis must always be carried out
before any type of dynamic analysis is started.




### Definition of subsequent input {#stamod_b_definition}

\latexonly
The below example specifies one nodal load, applies the 1st current profile and
tells that wind is not used. Subsequent sections give further details.

\begin{lstlisting}[language=riflex, numbers=none, frame=LTRB,frameround=tttt,framesep=4pt,
                                    xleftmargin=0cm,  xrightmargin=0cm,
                                    caption={Static condition input.}]
'**********************************************************************
 STATIC CONDITION INPUT
'**********************************************************************
'nlcomp  icurin  curfac  iwindin
 1       1       1.0     0
' static load components, units: kN/kNm
' line-id ilseg ilnode/ilelm ildof rlmag  chicoo
  shaft   2     1            4       1.0  LOCAL
'
'               lcons  = 1 : consistent load and mass formulation
'               isolvr = 2 : sparse matrix storage
' lcons isolvr
  1     2
\end{lstlisting}
\endlatexonly



#### Data group identifier {#stamod_b_definition_data}

~~~
STATic CONDition INPUt
~~~




#### External, static loads {#stamod_b_definition_external1}

~~~
NLCOMP ICURIN CURFAC IWINDIN
~~~

- `NLCOMP: integer, default: 0`: Number of additional load components. Loads to be specified in next data group, 
'Additional, static load components', which is omitted if `NLCOMP=0`.


- `ICURIN: integer, default: 0`: Current indicator
    - `ICURIN = 0`: No current
    - `ICURIN = N`: Current profile no. N on referenced environmental
    description (`IDENV`) is used. The profile may be scaled by `CURFAC`
- `CURFAC: integer, real: 1`: Scaling factor to amplify or reduce the referred current profile $\mathrm{[1\]}$
- `IWINDIN: integer, default: 0`: Wind indicator
    - `IWINDIN = 0`: No wind
    - `IWINDIN = N`: Wind specification no. N on referenced environmental
    description (`IDENV`) is used.

If current loads are applied in `STAMOD`, the current active at the end of
the static analysis will be used in `DYNMOD`. If current loads are not
applied in `STAMOD`, the specified current profile `ICURIN` will be used in
`DYNMOD` with the scaling factor `CURFAC` specified here.

`CURFAC` must be 1.0 for a restart analysis.




#### Additional, static load components {#stamod_b_definition_additional}

This data specification is omitted if `NLCOMP=0`. Otherwise `NLCOMP` input lines are specified.

~~~
LINE-ID ILSEG ILNODE ILDOF RLMAG CHICOO
~~~

- `LINE-ID: character(8)`: Reference to line identifier.
- `ILSEG: integer`: Segment number within the actual line.
- `ILNODE: integer`: Local node (`CHICOO=GLOBAL`) or element number (`CHICOO=LOCAL`).
- `ILDOF: integer`: Degree of freedom within the specified node/element.
    - `ILDOF = 7....12` at end 2 of an element.
- `RLMAG: real, default: 0`: Magnitude of load component (F or FL).
- `CHICOO: character(6), default: GLOBAL`: Reference system for application of nodal load components.
    - `CHICOO = GLOBAL`: Force component refers to global system.
    The force is applied at the specified node.
    - `CHICOO = LOCAL`: Force component refers to local system.
    The force is applied to the specified element.
    - If skew boundaries or vessel boundary are specified at the node `CHICOO=GLOBAL` means that the load component acts in the skew (vessel) system.




#### Load formulation and matrix format {#stamod_b_definition_load}

~~~
LCONS ISOLVR
~~~

- `LCONS: integer, default: 0`: Switch for lumped or consistent load and mass formulation.
    - `LCONS = 0`: Lumped load and mass formulation.
    - `LCONS = 1`: Consistent load and mass formulation.
    - Applies also to DYNMOD
- `ISOLVR: integer, default: 1`: Matrix storage format. Applies also to `DYNMOD`.
    - `ISOLVR = 1`: Skyline, recommended for simple, single line riser models.
    - `ISOLVR = 2`: Sparse, recommended for coupled analysis and complex models with branch points.
    - The free vibration option in `DYNMOD` requires `ISOLVR = 1`

When applying the lumped load and mass formulation (`LCONS=0`), the element nodes are assigned
part of the distributed external element load and mass directly. When using a consistent formulation
(`LCONS=1`), the external element load and mass is distributed to the nodes using the same
interpolation (shape) functions as applied when determining the element stiffness matrix.
See the theory manual for more details.

The numerical solution speed for static and subsequent dynamic analysis depends on the matrix
storage format. For a typical single riser analysis where the resulting stiffness matrix is rather
narrow banded, the skyline matrix storage method is the most efficient, `ISOLVR=1`.

In case of many branch points, or when doing coupled analysis with many mooring lines and/or
risers connected to the same floating vessel, the stiffness matrix may be significantly more
broad banded. In such a case, choosing sparse matrix storage may increase the numerical solution
speed, `ISOLVR=2`.

Note: Since the difference in solution speed could be practically negligible for small models,
sparse matrix storage (`ISOLVR=2`) may be a good initial choice. Later, one could check if
skyline matrix storage gives better numerical performance.



### Computational procedure selection {#stamod_b_computational}




#### Data group identifier, one input line {#stamod_b_computational_data}

~~~
COMPutational PROCedure 
~~~




#### Method for static equilibrium computation {#stamod_b_computational_method}

~~~
 AMETH
~~~


- `AMETH: character(6)`: Code for computation method. The following options are available:
    - `CAT`: Catenary analysis, bending stiffness neglected
    - `CATFEM`: Finite element method based on catenary start configuration
    - `STAFEM`: Finite element method based on start configuration read from file.
    - `FEM`: Finite element method based on stress free start configuration

Selection of options according to system type and whether a subsequent
dynamic analysis is to be carried out or not:

![Available options for static and dynamic analysis](@ref figures/um_sta_fig180.svg)
@image latex figures/um_sta_fig180.pdf "Available options for static and dynamic analysis" width=12cm




### Catenary analysis procedure, CAT {#stamod_b_cat}




#### Data group identifier {#stamod_b_cat_data}

~~~
CATEnary ANALysis PARAmeters 
~~~




#### Parameters for catenary analysis {#stamod_b_cat_parameters}

~~~
XL50 FL10 XU1TOL XU3TOL
~~~

- `XL50: real, default: see below`: Initial estimate of angle from vertical at the point where the catenary
calculation starts $\mathrm{[deg\]}$
- `FL10: real, default: see below`: Initial estimate of axial force at the point where the catenary
calculation starts $\mathrm{[F\]}$
- `XU1TOL: real, default: see below`: Tolerance of X1 coordinate at upper end $\mathrm{[L\]}$
- `XU3TOL: real, default: see below`: Tolerance of X3 coordinate at upper end $\mathrm{[L\]}$

Default values will be computed for the standard riser system
based on geometry and specified weights and forces, if the parameter is
given a "slash"(/). For standard system SA, SB and SD the calculation of
the catenary solution starts at the upper end, for SC it starts at the
lower end.

For `XL50` and `FL10` default values are recommended. The values are printed
out on the result file. For the SC system these parameters are dummy.

The default values of `XU1TOL` and `XU3TOL` are calculated as $\mathrm{10^{-4}}$ (length of the riser).




### Catenary and subsequent finite element analysis, CATFEM {#stamod_b_catfem}




#### Data group identifier {#stamod_b_catfem_data}

~~~
CATFem ANALysis PARAmeters 
~~~




#### Parameters for catenary equilibrium calculation {#stamod_b_catfem_parameters}

~~~
XL50 FL10 XU1TOL XU3TOL
~~~

- `XL50: real, default: see below`: Initial estimate of angle from vertical at the point where the catenary
calculation starts $\mathrm{[deg\]}$
- `FL10: real, default: see below`: Initial estimate of axial force at the point where the catenary
calculation starts $\mathrm{[F\]}$
- `XU1TOL: real, default: see below`: Tolerance of X1 coordinate at upper end $\mathrm{[L\]}$
- `XU3TOL: real, default: see below`: Tolerance of X3 coordinate at upper end $\mathrm{[L\]}$

Default values will be computed for the standard riser system
based on geometry and specified weights and forces, if the parameter is
given a "slash"(/). 

For standard system SA, SB and SD the calculation of
the catenary solution starts at the upper end, for SC it starts at the
lower end.

For `XL50` and `FL10` default values are recommended. The values are printed
out on the result file. For the SC system these parameters are dummy.

The default values of `XU1TOL` and `XU3TOL` are calculated as $\mathrm{10^{-4}}$ (length of the main riser line).

Next data group is [Incremental loading procedure](@ref stamod_b_incremental).




### Finite element analysis from start configuration, STAFEM {#stamod_b_stafem}

Preliminary test version.

In present version it is assumed that the start solution represent a catenary solution.




#### Data group identifier {#stamod_b_stafem_data}

~~~
STAFem ANALysis PARAmeters 
~~~




#### Name of file containing the start solution {#stamod_b_stafem_name}

~~~
CHFSTA KFORM
~~~

- `CHFSTA: character(60)`: File name with specification of start configuration . The content of
this file is described in [Define Start Configuration](@ref stamod_description_define_start).
- `KFORM: integer, default: 1`: Code for file format
    - `KFORM = 1`: Co-ordinates and base vector system given for all FEM-nodes
in increasing node number order.

Next data group is [Incremental loading procedure](@ref stamod_b_incremental).




### Finite element analysis, FEM {#stamod_b_fem}




#### Data group identifier {#stamod_b_fem_data}

~~~
FEM ANALysis PARAmeters 
~~~




### Incremental loading procedure {#stamod_b_incremental}

This data group describes the incremental loading procedure from
catenary solution (`CATFEM`), from a specified start solution (`STAFEM`) or
from stress free configuration (`FEM`) to the final static equilibrium
configuration.

A brief summary of the incremental loading procedure applied, is given
in the following. For a more detailed description including analysis
guidance, see 'Static Finite Element Analysis' in the RIFLEX Theory Manual.

Based on load groups, the user is free to specify an arbitrary load
sequence. Incrementation and iteration parameters are specified
separately for each load group. One or several load types can be applied
within each load group. Simultaneous application of several load types
and user-defined order of the load application is therefore possible.

The incremental loading is normally carried out in the following
sequence:

- Load group 1: Volume forces (weight and buoyancy)
- Load group 2: Specified displacements (i.e. displacements to final
    position of nodal points with specified boundary conditions)
- Load group 3: Specified forces (nodal point loads)
- Load group 4: Position dependent forces (current forces)

All user-defined load types have to be specified within a load group in
order to be applied during the incremental loading of the system.
Examples are roller and tensioner contact forces (elastic contact
surface), initially stressed segments or floater forces.

The user may specify the load group for application of bottom friction
and global linear springs. It is also possible to neglect friction and
springs in normal static analysis and activate friction during static
parameter variation or at the start of dynamic analysis.




##### CATFEM analysis

Volume forces have to be applied within one incremental step in the
first specified load group. This is because volume forces and prescribed
translations from stress free to final positions of terminal points are
included in the catenary start solution. Deviations between the catenary
and the final `FEM` solution are, however, present due to different
mathematical formulations and neglection of bending stiffness in the
catenary analysis. The first load group applying volume forces in one
incremental step, is therefore a simple equilibrium iteration starting
from the catenary solution with weight and buoyancy forces acting. The
equilibrium iteration may fail if there are significant differences
between the catenary solution and the final solution due to bending
stiffness. It is therefore possible to apply the bending stiffness in
several incremental steps to reach the final solution.

The iterative approach on boundary conditions used in the catenary
analysis will give deviations between specified translating boundary
conditions (i.e. x and z co-ordinates) and boundary condition computed
by the catenary analysis. Further, specified boundary conditions for
rotations at the supports will not be satisfied by the catenary analysis
due to neglection of bending stiffness. A load group for prescribed
displacements should therefore be included to account for inaccuracies
in boundary conditions from the catenary analysis.




##### STAFEM analysis

The load types applied for the start configuration have to be indicated
in the first specified load group. These load types will act with full
force while the residual forces will be off-loaded the specified number
of load steps. The residual forces are the unbalanced forces based on
the indicated load types and the internal forces that appear when the
start configuration is described in the finite element formulation.

Note that it is assumed that final boundary conditions are included in the
start configuration. As a consequence the procedure will be indifferent
to specification of prescribed displacements.




#### Load group specification {#stamod_b_incremental_load}

The input lines 'Data group identifier...', 'Load group incrementation...' and 'Load
types to be activated...' have to be given in one block for each load group.




##### Data group identifier, one input line {#stamod_b_incremental_load_data}

~~~
LOAD GROUP DATA 
~~~


##### Load group incrementation and iteration parameters, one input line {#stamod_b_incremental_load_group_incrementation}

~~~
NSTEP MAXIT RACU CHNORM EACU
~~~


- `NSTEP: integer`: Number of load steps
- `MAXIT: integer, default: 10`: Maximum number of iterations during application of load
- `RACU: real, default:` $\mathrm{10^{-6}}$: Required accuracy measured by displacement norm $\mathrm{[1\]}$
- `CHNORM: character(4), default: DISP`: Convergence norm switch
        - `= DISP`: Use the default Euclidean displacement norm only
        - `= BOTH`: Use both the default Euclidean displacement norm and the energy norm  
- `EACU: real, default:` $\mathrm{10^{-6}}$: Required accuracy measured by energy norm
        - Dummy if `CHNORM=DISP`  
 




##### Load types to be activated, one line for each load type to be activated within the load group {#stamod_b_incremental_load_types}

~~~
LOTYPE ISPEC
~~~

- `LOTYPE: character(4)`: Load type to be applied
    - `= VOLU`: Volume forces
    - `= DISP`: Specified displacements
    - `= SFOR`: Specified forces
    - `= CURR`: Current forces
    - `= TENS`: Activate tensioner contact forces
    - `= ROLL`: Activate roller and tubular contact forces
    - `= PIPE`: Activate pipe-in-pipe contact forces
    - `= ISTR`: Initially pre-stressed segments
    - `= FLOA`: Floater forces
    - `= FRIC`: Activate bottom friction forces
    - `= SPRI`: Activate global springs
    - `= BEND`: Bending stiffness
    - `= TEMP`: Temperature variation 
    - `= PRES`: Pressure variation
    - `= MEMO`: Activate material memory formulation (Isotropic/kinematic hardening)
    - `= BOUN`: Activate boundary change
    - `= WINC`: Run winch(es)
    - `= GROW`: Apply cross-section changes from growth profile
    - `= WIND`: Wind forces
- `ISPEC: integer`: Parameter used for further description of applied load type:
    - `LOTYPE = PIPE`:
        - `ISPEC = 0` (default): Possible pipe-in-pipe contact enabled (ENTERED)
        - `= 1`: Specify start condition for pipe-in-pipe contact
    - `LOTYPE = TEMP`:
        - `ISPEC = NLSPEC`: Number of subsequent input lines for specification of temperature variation.
    - `LOTYPE = PRES`;
        - `ISPEC = Nxxx`: Number of subsequent input lines for specification of pressure variation
    - `LOTYPE = BOUN`:
        - `ISPEC = NBOUND`: Number of nodes with change in boundary conditions.
    - `LOTYPE = WINC`:
        - `ISPEC = Nxxx`: Number of subsequent input lines for specification of winch run
    - `LOTYPE = GROW`:
        - `ISPEC = 0` (default): No scaling of growth profile.
        - `ISPEC = 1`: Number of subsequent input lines for specification of growth scaling.
    - `LOTYPE = WIND`:
        - `ISPEC = 0` (default): No wind on turbine blades
        - `ISPEC = 1`: Number of subsequent input lines for specification of wind on turbine blades.
    - `ISPEC` is dummy for other load types

Note that some static loads will be incremented over `NSTEP` load steps while others 
will be activated at the beginning of the load group. For example volume forces and current forces are 
incremented over the specified load steps while element memory and contact forces are activated 
at the beginning of the load group in which they are specified.

Volume forces have to be applied in the first specified load
group in case of `CATFEM` or `STAFEM` analysis. For `CATFEM` analysis the
number of load steps in this load group has to be one (`NSTEP = 1`).



##### Pipe-in-pipe contact; One input line given if LOTYPE=PIPE and ISPEC = 1 {#stamod_b_incremental_load_pipe}

~~~
CHPCNT
~~~

- `CHPCNT: character`: 
    - `= ENTERED`
    - `= NOT ENTERED`


Note that `ENTERED` should be used for analysis of slender structures such as risers, cables and umbilicals. `NOT ENTERED` is intended to be used for marine operations. The master and slave pipe in static free condition should be modelled as close to the final configuration as possible, see illustraion in the figures 'Example: pipe-in-pipe modelled as `ENTERED`' and 'Example: pipe-in-pipe modelled as `NOT ENTERED`' below. 

![Example: pipe-in-pipe modelled as `ENTERED`](@ref figures/um_pipeinpipe_entered.png)
@image latex figures/um_pipeinpipe_entered.pdf "Example: pipe-in-pipe modelled as `ENTERED`" width=12cm

![Example: pipe-in-pipe modelled as `NOT ENTERED`](@ref figures/um_pipeinpipe_notentered.png)
@image latex figures/um_pipeinpipe_notentered.pdf "Example: pipe-in-pipe modelled as `NOT ENTERED`" width=16cm



##### Temperature variation, NLSPEC input lines only given if LOTYPE = TEMP {#stamod_b_incremental_load_temperature}

~~~
LINE-ID ISEG IEC TEMP
~~~


- `LINE-ID: character(8)`: Reference to line identifier
- `ISEG: integer/character`: Segment number
    - `= 0` / "ALL": All segments in specified line
- `IEL: integer/character`: Element number
    - `= 0` / "ALL": All elements in specified line
- `Temp: real`: Temperature at end of temperature variation

The temperature is varied linearly during the load group from the
starting temperature given in the cross-sectional data in `INPMOD` and
ending with the temperature specified here.

A linear variation of temperature over a sequence of elements may be
specified by giving a negative element number at the second end of the
linear variation




##### Pressure variation, NLSPEC input lines if LOTYPE = PRES {#stamod_b_incremental_load_pressure}

~~~
MRL-ID PRESSI DPRESS VVELI
~~~

- `MRL-ID: character(8)`: Reference to Main Riser Line identifier
- `PRESSI: real, default: 0`: Final pressure at inlet end $\mathrm{[F/L^2\]}$
- `DPRESS: real, default: 0`: Final pressure drop $\mathrm{[F/L^3\]}$
- `VVELI: real, default: 0`: Final fluid velocity $\mathrm{[L^3/T\]}$
    - Dummy in present version




##### Boundary changes, 2 x NBOUND input lines if LOTYPE = BOUN {#stamod_b_incremental_load_boundary}

Identification of node for boundary change
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



Status for nodal degrees of freedom. To be given if `IOP = 0`
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


Identification of master node. To be given if `IOP = -1`
~~~
LINE-ID ILSEG ILNODE
~~~

- `LINE-ID: character(8)`: Reference to line identifier
- `ILSEG: integer`: Segment number within the actual line
- `ILNODE: integer`: Local node number within segment




##### Winch run, NLSPEC input lines only given if LOTYPE = WINC {#stamod_b_incremental_load_winch}

~~~
IWINCH WILNG
~~~

- `IWINCH: integer`: Line number
- `WILNG: real`: Total run length $\mathrm{[L\]}$ 

`WILNG > 0`: winching out, i.e. the winch run will increase the active length. 


##### Growth profile, ISPEC=1 input lines only given if LOTYPE = GROW {#stamod_b_incremental_load_growth}

~~~
GFAC
~~~


- `GFAC: real, default: 1.0`: Scaling of growth profile


##### Wind force, ISPEC=1 input lines only given if LOTYPE = WIND {#stamod_b_incremental_load_wind}

~~~
WindOnTurbineBlades
~~~


- `WindOnTurbineBlades: character(8), default: OFF`: Code for wid loads on turbine blades
    - `WindOnTurbineBlades = OFF`: No wind loads on turbine blades in static analysis. 
    - `WindOnTurbineBlades = ON `: Wind loads on turbine blades in static analysis.

Note that wind loads will be applied on turbine blades and the rest of the structure in dynamic analysis.


### Define stressfree configuration {#stamod_b_define}

This data group is optionally available for AR systems. It enables the
user to define an arbitrary stressfree configuration without having to
establish a complex line/supernode system model. The option is useful
for effective modelling of pre-bent sections.

This data group will redefine the stressfree configuration, but will not
affect the coordinates for static equilibrium position given as input to
`INPMOD`, data group [Specification of boundary conditions, stressfree configuration and static equilibrium configuration](@ref inpmod_b_arbitrary_specification).




#### Data group identifier {#stamod_b_define_data}

~~~
DEFIne STREssfree CONFiguration 
~~~




#### File name {#stamod_b_define_file_name}

~~~
CHFCON
~~~

- `CHFCON: character(80)`: File name with definition of stress free configuration




#### File format {#stamod_b_define_file_format}

~~~
KFORM
~~~

- `KFORM: integer, default: 1`: Code for file format
    - `KFORM = 1`: Stress free co-ordinates given for all `FEM`-nodes in increasing node number order




### Bottom geometry file {#stamod_b_bottom}

This data group is given if `IBOT 3D = 1` in the `INPMOD` input file, and
allows the user to define an uneven seabed, using depth data in a
regular grid with equidistant spacing.




#### Data group identifier {#stamod_b_bottom_data}

~~~
BOTTom GEOMetry FILE 
~~~




#### File name {#stamod_b_bottom_file}

~~~
CHFBOT
~~~

- `CHFBOT: character(80)`: File name with seabed geometry data

The content of this file is described in [Define uneven seabed geometry](@ref stamod_description_define_uneven).




#### Coordinates of the seabed file reference system {#stamod_b_bottom_coordinates}

~~~
XOS YOS ZOS ANGOS
~~~

- `XOS: real, default: 0`: x-coordinate of the origin of the seabed file reference system, in the
global reference system $\mathrm{[L\]}$
- `YOS: real, default: 0`: y-coordinate of the origin of the seabed file reference system, in the
global reference system $\mathrm{[L\]}$
- `ZOS: real, default: 0`: z-coordinate of the origin of the seabed file reference system, in the
global reference system $\mathrm{[L\]}$
- `ANGOS: real, default: 0`: Angle between the x-axis of the seabed file reference system and the
x-axis of the global reference system $\mathrm{[deg\]}$




## Data Group C: Static Analysis with Parameter Variation {#stamod_c}




### Parameter variation definition {#stamod_c_parameter}




#### Data group identifier, one input line {#stamod_c_parameter_data_one}

~~~
PARAmeter VARIation DEFInition 
~~~




#### Number of variations and variation codes {#stamod_c_parameter_number}

~~~
NSTVAR IOFPOS ICUVAR IFOVAR MAXIPV RACUPV CHNORM EACUPV
~~~

- `NSTVAR: integer`: Number of steps in parameter variations
- `IOFPOS: integer, default: 0`: Code for static offset variation
    - `IOFPOS = 0`: The parameter is not varied
    - `IOFPOS = 1`: The parameter is varied in `NSTVAR` steps according to
subsequent specification
- `ICUVAR: integer, default: 0`: Code for current variation
    - `ICUVAR = 0`: The parameter is not varied
    - `ICUVAR = 1`: The parameter is varied in `NSTVAR` steps according to
subsequent specification
- `IFOVAR: integer, default: 0`: Code for specified force variation
    - `IFOVAR = 0`: The parameter is not varied
    - `IFOVAR = 1`: The parameter is varied in `NSTVAR` steps according to
subsequent specification
- `MAXIPV: integer, default: 1`: Maximum number of iterations for each variation
- `RACUPV: real, default:`$\mathrm{10^{-5}}$: Required accuracy measured by displacement norm
- `CHNORM: character(4), default: DISP`: Convergence norm switch
        - `= DISP`: Use the default Euclidean displacement norm only
        - `= BOTH`: Use both the default Euclidean displacement norm and the energy norm  
- `EACUPV: real, default:` $\mathrm{10^{-5}}$: Required accuracy measured by energy norm 
        - Dummy if `CHNORM=DISP`  

The total number of load steps in parameter variation is `NSTVAR`.

All parameter for which variations are specified, are varied simultaneously

Information about parameter values are to be specified in the
subsequent data groups. The initial configuration as specified according
to data section B is automatically taken as the first case.

`ICURIN` must be greater than zero and `CURFAC` must be 1.0 (See [External, static loads](@ref stamod_b_definition_external1)).

 See also [Note: Static Analysis with Fixed Parameters and Parameter Variation](@ref stamod_gen_comment).


#### Load types to be activated. One line for each load type. Optional input, maximum 4 specifications. {#stamod_c_parameter_load}

~~~
LOTYPE ISPEC
~~~

- `LOTYPE: character(4)`: Load type to be applied
    - `= FRIC`: Activate bottom friction forces
    - `= SPRI`: Activate global springs
    - `= MEMO`: Activate material memory formulation (Isotropic/kinematic hardening)
    - `= BOUN`: Boundary change
- `ISPEC: integer`: Parameter used for further description of applied load type:
    - `LOTYPE = BOUN`:
        - `ISPEC = NBOUND`; Number of nodes with change in boundary conditions.
    - `ISPEC` is dummy for other load types

If specified load type is activated before, the input given here is disregarded.

Activation of sea floor friction is given by `FRIC`.




##### Specification of boundary change, 2 x NBOUND lines {#stamod_c_parameter_load_specification}



Identification of node for boundary change
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



Status for nodal degrees of freedom. To be given if `IOP = 0`
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



Identification of master node. To be given if `IOP = -1`
~~~
LINE-ID ILSEG ILNODE 
~~~

- `LINE-ID: character(8)`: Reference to line ID
- `ILSEG: integer`: Segment number within the actual line
- `ILNODE: integer`: Local node number within segment




#### Variation of static positions {#stamod_c_parameter_variation}

This data group is relevant only if `IOFPOS=1`.




##### Data group identifier {#stamod_c_parameter_data_2}

~~~
STATic OFFSet INCRements 
~~~




##### Static position increments {#stamod_c_parameter_static}

~~~
CHIREF DXOFF DYOFF DZOFF IROT DROT
~~~

- `CHIREF: character(8)`: Reference to moving point
    - `CHIREF = -IVES`: Support vessel number `IVES`
    - `CHIREF = SNOD_ID`: Supernode identifier. `SNOD_ID` must refer to a supernode with specified position
- `DXOFF: real, default: 0`: Displacement increment, X-direction $\mathrm{[L\]}$
- `DYOFF: real, default: 0`: Displacement increment, Y-direction $\mathrm{[L\]}$
- `DZOFF: real, default: 0`: Displacement increment, Z-direction $\mathrm{[L\]}$
- `IROT: integer, default: 0`: Rotation code
    - `IROT = 0`: No rotation
    - `IROT = 1`: The given rotation is taken about X-axis
    - `IROT = 2`: The given rotation is taken about Y-axis
    - `IROT = 3`: The given rotation is taken about Z-axis
- `DROT: real, default: 0`: Rotation increment $\mathrm{[deg\]}$
    - Dummy if `IROT=0` 

If a support vessel is specified (`IREF=-IVES`) the displacement
increments refer to the support vessel coordinate system. Otherwise the
increments refer to the global coordinate system.

Only rotation around the Z-axis may be given if `IREF = -IVES`

If the supernode has boundary conditions specified in a skew co-ordinate
system or in the vessel system, displacements and the rotation increment
`DROT` take place in the skew / vessel system. It should also be noted
that the orientation of such a skew co-ordinate system is kept constant
during the static position incrementation (relevant for AR systems only).




### Variation of current velocity and direction {#stamod_c_variation_of_current}

This data group is relevant only if `ICUVAR=1`.




#### Data group identifier, one input line {#stamod_c_variation_of_current_data}

~~~
CURRent VARIation INCRements 
~~~




#### Current velocity and direction increments {#stamod_c_variation_of_current_velocity}

~~~
DCUVEL DCUDIR
~~~

- `DCUVEL: real, default: 0`: Current velocity increment $\mathrm{[L/T\]}$
- `DCUDIR: real, default: 0`: Current direction increment $\mathrm{[deg\]}$

In the case of multilayer current specification, these increments are interpreted as follows.

- DCUVEL: This applies directly to the uppermost layer. The lower layers are
incremented in the same proportion, so that the shape of the current
profile is maintained.
- DCUDIR: This applies to all current layers, so that the whole current profile is
rotated the same amount.




### Variation of specified forces {#stamod_c_variation_of_specified}

This data group is relevant only if `IFOVAR=1` and `NLCOMP >= 1` (See [Definition of subsequent input](@ref stamod_b_definition)).




#### Data group identifier, one input line {#stamod_c_variation_of_specified_data}

~~~
SPECified FORCe INCRements 
~~~




#### Force increments, NLCOMP input lines to be given {#stamod_c_variation_of_specified_force}

~~~
DRLMAG
~~~

- `DRLMAG: real, default: 0`: Force increment on specified forces `RLMAG` (F or FL).
    - See [Additional, static load components](@ref stamod_b_definition_additional).




### Control parameters for printing of results {#stamod_c_control}




#### Data group identifier, one input line {#stamod_c_control_data}

~~~
STAMod PRINt CONTrol 
~~~




#### Control parameters for print of results from static parameter variation analysis {#stamod_c_control_parameters}

~~~
ISTEP ISFOR ISPOS
~~~

- `ISTEP: integer, default: 1`: Step interval for print of specified parameters. 
    - Print is given for the following steps: 1, 1+`ISTEP`, 1+2 $\mathrm{\times }$ `ISTEP`, 1+3 $\mathrm{\times }$ `ISTEP, ..., NSTVAR`
    - `ISTEP = 1`: Gives print of results for all variation steps
- `ISFOR: integer, default: 1`: Parameter for print of forces
    - `ISFOR = 0`: No print of external forces
    - `ISFOR = 1`: Print of external force components in global x, y, z
    direction at all supernodes with the following status codes: `TSNFX, TSNFX2, TSNPOSI1`
    - Not yet implemented
- `ISPOS: integer, default: 1`: Parameter for print of position
    - `ISPOS = 0`: No print of positions
    - `ISPOS = 1`: Print of x, y and z coordinates for all free supernodes (i.e. status code `TSNBRA` and `TSNFRE`)




## Static Analysis with Updated Drag Forces {#stamod_sawu}

An important consequence of VIV response is increased in-line current
forces. One of the key results from the `VIVANA` program is therefore
drag amplification factors along the structure. The objective of this
input is to enable static and dynamic analysis using the updated drag
forces.

To use this option the `RIFLEX` program modules must be run in the following order:
-   `INPMOD`
-   `STAMOD`
-   `VIVANA`
-   `STAMOD` with the drag amplification data group specified

Note that drag amplication cannot be used in combination with marine growth profile specification (@ref inpmod_c_growth ).


### Data group identifier, one input line {#stamod_sawu_data}

~~~
DRAG AMPLIFICATION INPUT 
~~~



### Specification of file for input of drag amplification, one input line {#stamod_sawu_load}

~~~
CHFDRG CHIOP
~~~

- `CHFDRG: character(60)`: File with drag amplification coefficient; e.g case22_vivana.mpf
- `CHIOP: character(60)`: Format of file with drag amplification coefficients

The `CHFDRG` file may be generated by running `VIVANA`.

The only file type currently available is the MatrixPlot file
format. Thus; `CHIOP = MPF`.




## Description of Additional Input Files {#stamod_description}




### Define Stressfree Configuration {#stamod_description_define_stressfree}

The file "CHFCON" specified in [Data Group B: Static Analysis with Fixed Parameters](@ref stamod_b), contains
definition of stressfree configuration. The file is a free format sequential ASCII-file.

The file description depends on the parameter "KFORM" specified in 
[Finite element analysis from start configuration, STAFEM](@ref stamod_b_stafem). 

File description: `KFORM = 1`.




#### Number of nodes, one input line {#stamod_description_define_stressfree_number}

~~~
NFSNOD
~~~

- `NFSNOD: integer`: Number of `FEM`-nodes for which coordinates for stressfree configuration
are specified. In this version `NFSNOD` must be equal to the total number of `FEM`-nodes




#### Coordinates for stressfree configuration, NFSNOD input lines {#stamod_description_define_stressfree_coordinates}

~~~
INOD X0 Y0 Z0
~~~

- `INOD: integer`: Node number 1 >= `INOD` >= `NFSNOD`
- `X0: real`: x-coordinate describing stressfree configuration
- `Y0: real`: y-coordinate describing stressfree configuration
- `Z0: real`: z-coordinate describing stressfree configuration

The coordinate must be consistent with the stressfree element length




### Define Start Configuration {#stamod_description_define_start}

The file 'CHFSTA' specified in [Finite element analysis from start configuration, STAFEM](@ref stamod_b_stafem), 
contains definition of start configuration. The file is a free format sequential ASCII-file.

The file description depends on the parameter 'KFORM' specified in 
[Finite element analysis from start configuration, STAFEM](@ref stamod_b_stafem). 

File description: `KFORM = 1`.




#### Number of nodes, one input line {#stamod_description_define_start_number}

~~~
NFSNOD
~~~

- `NFSNOD: integer`: Number of `FEM`-nodes for which coordinates for stressfree configuration
are specified. In this version `NFSNOD` must be equal to the total number of `FEM`-nodes




#### Coordinates for start configuration, NFSNOD input lines {#stamod_description_define_start_coordinates}

~~~
INOD X0 Y0 Z0 T11 T12 T13 T21 T22 T23 T31 T32 T33
~~~

- `INOD: integer`: Node number 1 >= `INOD` >= `NFSNODI`
- `X0: real`: x-coordinate describing stressfree configuration
- `Y0: real`: y-coordinate describing stressfree configuration
- `Z0: real`: z-coordinate describing stressfree configuration

Nodal base vector system:
- x-direction of node system referred to the global system
    - `T11: real, default: 1`: component in global x-direction
    - `T12: real, default: 0`: component in global y-direction
    - `T13: real, default: 0`: component in global z-direction
- y-direction of node system referred to the global system
    - `T21: real, default: 0`: 
    - `T22: real, default: 1`: 
    - `T23: real, default: 0`: 
- z-direction of node system referred to the global system
    - `T31: real, default: 0`: 
    - `T32: real, default: 0`: 
    - `T33: real, default: 1`: 




### Define uneven seabed geometry {#stamod_description_define_uneven}

The seabed geometry data is given on a regularly spaced grid. The grid
can be rotated and translated relatively to the reference system of the
seabed geometry file. (In addition the reference system of the seabed
geometry file can be rotated relatively to the global reference system
ref. [Coordinates of the seabed file reference system](@ref stamod_b_bottom_coordinates)).

A MATLAB script is available, to generate such a file from data given as
a set of x, y, z coordinates

At each step of the static and dynamic analysis, it is checked that
every node of the model has x and y coordinates that are within the
grid. Excursions from the grid will cause the program to terminate.




#### Description text of geometry {#stamod_description_define_uneven_description}

~~~
CHBOTT
~~~

- `CHBOTT: character`: Descriptive text of geometry




#### Grid dimension and extension, one input file {#stamod_description_define_uneven_grid_dimension}

~~~
NGX NGY XSmin XSmax YSmin YSmax DGX DGY
~~~

- `NGX: integer`: Number of points in the grid in the x direction 
- `NGY: integer`: Number of points in the grid in the y direction
- `Xsmin: real`: Coordinate of the first point in the grid in the x direction $\mathrm{[L\]}$
- `Xsmax: real`: Coordinate of the last point in the grid in the x direction $\mathrm{[L\]}$. Used to check consistency of the grid input and whether a node is outside the grid.
- `Ysmin: real`: Coordinate of the first point in the grid in the y direction $\mathrm{[L\]}$
- `Ysmax: real`: Coordinate of the last point in the grid in the y direction $\mathrm{[L\]}$. Used to check consistency of the grid input and whether a node is outside the grid.
- `DGX: real`: Distance between grid points in the x direction $\mathrm{[L\]}$
- `DGY: real`: Distance between grid points in the y direction $\mathrm{[L\]}$

The x and y coordinates of the grid corners and the distances between
grid ponts are converted to integer values with unit
$\mathrm{[L/100\]}$.



#### Grid orientation, one input line {#stamod_description_define_uneven_grid_orientation}

~~~
XOL YOL ANGOL
~~~

- `XOL: real`: x-coordinate of the origin of the grid, in the seabed file reference system $\mathrm{[L\]}$
- `YOL: real`: y-coordinate of the origin of the grid, in the seabed file reference system $\mathrm{[L\]}$
- `ANGOL: real`: Angle between the x axis of the grid and the x axis of the seabed file reference system $\mathrm{[deg\]}$




#### Depths at gridpoint, NGY input lines {#stamod_description_define_uneven_depths}

~~~
IZBOT1 ........ IZBOTngx
~~~

- `IZBOT1: integer`: 100 $\mathrm{\times }$ Depth at first x value $\mathrm{[L/100\]}$
- .
- .
- .
- `IZBOTngx: integer`: 100 $\mathrm{\times }$ Depth at last x value $\mathrm{[L/100\]}$

The input line may be given over several lines of text by using the
continuation character ‘&’.
