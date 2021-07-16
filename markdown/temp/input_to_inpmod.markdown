# Input to INPMOD




## General Information {#inpmod_general_information}

The purpose of the `INPMOD` module is to administer reading/interpretation
of system and environmental data. The following data groups are
included:

-   General Control Data - Data Group A
-   Single Riser Data - Data Group B
-   Component Data - Data Group C
-   Environmental Data - Data Group D
-   Support Vessel Data - Data Group E

An `INPMOD` run may consist of a combination of the data groups, but a
data group included must be complete. Data group A is mandatory, while
data groups B-E normally will be given. All data groups except
data group A can be given more than once. Note that running `INPMOD`
always overwrites old information in the `INPFIL`. That means that all
needed data on `INPFIL` must be generated in one `INPMOD` run.

Within each group, the first two data groups (identification and control
data) must be given first, while the order of the remaning data groups,
to some extent, is arbitrary. Data groups in one section cannot be mixed
with data groups in another section. This means that when the program
finds a data group identifier it will only check the data within the
current section. If one or more errors are found, an error message is
written and an error flag is written to the `INPFIL` file. A run with
`STAMOD` or `DYNMOD` using this file will then be terminated. `INPMOD` will
continue to read data until the `END` input line is found (see [Termination of input data](@ref inpmod_data_group_a_termination_of_input_data))
regardless of the number of errors detected.




## Data Group A: General Control Data {#inpmod_data_group_a_general_control_data}

General inputs include the unit system.




###  INPMOD identification text {#inpmod_data_group_a_inpmod_identification}
An identification text describing the `INPMOD` run may be given. If given, this text is printed on the front page of the `INPMOD` print file.




#### Data group identifier, one input line {#inpmod_data_group_a_data_group_identifier}
Mandatory.
~~~
INPMod IDENtification TEXT CHVERS
~~~
- `CHVERS: character(8)`: `RIFLEX` input file version, e.g. 3.2




#### Identification text, three input lines {#inpmod_data_group_a_identification_text}
Mandatory.
~~~
Heading, line no 1
Heading, line no 2
Heading, line no 3
~~~

Always three input lines, which may all be blank.
Each line may contain up to 60 characters.




###  Selection of unit system physical constant {#inpmod_data_group_a_selection_of_unit_system_physical}
The program applies a set of consistent units. The user is free to select
any combination of unit names for:

-   time $[\mathrm T\]$
-   length $[\mathrm L\]$
-   mass $[\mathrm M\]$
-   force $[\mathrm F\]$




#### Data group identifier, one input line {#inpmod_data_group_a_data_group_identifier_one_input_line}
Mandatory.
~~~
UNIT NAME SPECification
~~~




#### Unit names and gravitational constant {#inpmod_data_group_a_unit_names_and_gravitational}
Mandatory.
~~~
UT UL UM UF GRAV GCONS
~~~

- `UT: character(6), default: "s"`:  Unit name for time
- `UL: character(6), default: "m"`:  Unit name for length
- `UM: character(6), default: "kg"`: Unit name for mass 
- `UF: character(6), default: "kN"`: Unit name for force
- `GRAV: real > 0, default: 9.81`:       Numerical value of gravitational constant $[\mathrm{L/T^2}\]$
- `GCONS: real > 0, default: 0.001`:    Consistency acceleration parameter.
    -    `GCONS` = ACC[UF/UM]/ACC \left[UL/UT^2 \right]
        - where ACC is the numerical value of acceleration with the force and mass units, and with the length and time units, respectively.
        - With a consistent set of units, `GCONS = 1.0`.

Example: For the default units, the acceleration of gravity is
$9.81\times 10^{-3}\,\mathrm{kN/kg}$ or $9.81\,\mathrm{m/s}^2$ and
`GCONS` may be calculated as $\mathrm{9.81\times 10^{-3}/9.81=0.001}$.

In the case of `GCONS` $\mathrm{\neq 1}$, the
calculation of drag force coefficients must be multiplied by `GCONS`,
for example `CDY = GCONS` $\mathrm{(\frac{1}{2}\rho C_DD)}$, see also
[Hydrodynamic force coefficients] (@ref inpmod_c_crs1_hydrodynamic).

The unit names are printed as an output heading as shown below.

~~~
       +--------------------------------------------------------+
       !     CONSISTENT UNITS USED THROUGHOUT THE ANALYSES      !
       !--------------------------------------------------------!
       !     NAME FOR TIME   :  T = s                           !
       !     NAME FOR LENGTH :  L = m                           !
       !     NAME FOR MASS   :  M = kg                          !
       !     NAME FOR FORCE  :  F = kN                          !
       !                                                        !
       !     GRAVITATIONAL CONSTANT :                           !
       !     G     =  9.810     L/T**2                          !
       !     CONSISTENCY ACCELERATION PARAMETER :               !
       !     GCONS = 0.1000E-02 (F/M)/(L/T**2)                  !
       +--------------------------------------------------------+
~~~




###  Termination of input data {#inpmod_data_group_a_termination_of_input_data}

As mentioned an `INPMOD` run consist of some of the data groups A, B, C, D, E and F. No termination
is to be provided between the data groups, but after the last data group is given, the following input
line must be given to terminate the input stream:

~~~
END
~~~




## Data Group B: Single Riser Data {#inpmod_data_group_b_single_riser_data}


The riser description consists of the data group [Riser type specification] (@ref inpmod_data_group_b_riser_type_specification) 
followed by one of [Standard system SA] (@ref inpmod_b_SA), 
[Standard system SB](@ref inpmod_b_SB_standard_system), [Standard system SC](@ref inpmod_b_SC_standard_system), [Standard system SD](@ref inpmod_b_SD_standard)
or [Arbitrary system AR](@ref inpmod_b_arbitrary_arbitrary) with the topology and boundary conditions.

The data group [Line and segment specification](@ref inpmod_b_line_line_and_segment) 
is used for the specification of the line types that are used in topology specification.




###  Riser type specification {#inpmod_data_group_b_riser_type_specification}




#### Data group identifier, one input line {#inpmod_data_group_b_riser_type_specification_data_group_identifier}

~~~
NEW SINGle RISEr
~~~




#### Selection of riser type and identifier {#inpmod_b_riser_type_specification_selection_of_riser}
~~~
ATYPS IDRIS IDCON
~~~

- `ATYPS: character(6)`: Riser code type for single riser. Allowable codes are listed below:
                - SA: Next data in [Standard system SA] (@ref inpmod_b_SA)
                - SB: Next data in [Standard system SB](@ref inpmod_b_SB_standard_system)
                - SC: Next data in [Standard system SC](@ref inpmod_b_SC_standard_system)
                - SD: Next data in [Standard system SD](@ref inpmod_b_SD_standard)
                - AR: Next data in [Arbitrary system AR](@ref inpmod_b_arbitrary_arbitrary)
- `IDRIS: character(6)`: Riser identifier
- `IDCON: character(6), deault: "NONE"`: Normally not used!
    -   =LAYFLX - Roller contact forces are dumped on data files for LAYFLEX post-processing.
    -   Static roller contact forces will be output to the file `prefix_consta.asc`.
    -   For nonlinear dynamic analysis, time series of roller contact results will be stored on the file
    prefix_contts.asc and key results will be stored on the file `prefix_condyn.asc`.

One or several riser specifications may be created and stored by one run of INPMOD. The
identifier IDRIS is used by STAMOD to select one particular riser for analysis.




###  Standard system SA {#inpmod_b_SA}
One-point seafloor contact to (surface) vessel. The frequently used "steep
wave", "steep S" and "jumper" configurations are special cases of the SA system. The initial configuration of this
system is two-dimensional in X-Z plane.




##### Topology 

The only variable topology feature is the option of including vertical buoyancy or weight elements in the
form of branches.

![Topology of system SA](@ref figures/um_ii_fig17.svg)
@image latex figures/um_ii_fig17.eps "Topology of system SA" width=12cm

Introduction of branching points implies that more than one line has to be specified, see the figure 'Topology of system SA' above.
Branches are assumed to be vertical in a still water condition. Seafloor and surface contacts are not
modelled for this system.




#### Data group identifier {#inpmod_b_SA_data_group_identifier}
~~~
SINGle RISEr SA
~~~




#### Topology {#inpmod_b_SA_topology}
~~~
NSNOD
~~~

- `NSNOD: integer`: Number of supernodes

This implies that number of lines to be defined is `NLIN=NSNOD-1`, see the figure 'Topology of system SA' above.




#### Line, line type and supernode connectivity {#inpmod_b_SA_line_line_type_and}
This data group defines the connectivity between lines and supernodes. If the line identifier is missing
the line number implicitly defined by the order in which the lines are specified, will be used as the line
identifier. References to line type IDs and supernode numbers are mandatory.

The lines must be specified in the order indicated in the figure 'Topology of system SA' above. This means that the lines are given
continuously from seafloor to upper riser end.

At each branching point the line defining a branch is specified before the next line in the main riser
configuration. No ball joint components are accepted in branch lines.

`NLIN` input lines.
~~~
LINE-ID LINTYP-ID ISNOD1 ISNOD2
~~~
- `LINE-ID: character(8)`: Line identifier
- `LINTYP-ID: character(8)`: Reference to line type identifier
- `ISNOD1: integer`: Reference to supernode number at end 1
- `ISNOD2: integer`: Reference to supernode number at end 2

If only 1 alphanumeric string and 2 integers are specified, the first string is taken as `LINTYP-ID`.
~~~
LINTYP-ID ISNOD1 ISNOD2
~~~
The `LINE-ID` is taken as the line number as implicitly defined by the order in which the lines are
given.




#### Boundary conditions, coordinates {#inpmod_b_SA_boundary_conditions}
~~~
ZL XU ZU ALFL ALFU
~~~
- `ZL: real`: Z coordinate of lower end $\mathrm{[L\]}$
    -  X and y coordinates of lower end are set equal to zero.
- `XU: real > 0`: X coordinate of upper end $\mathrm{[L\]}$.
- `ZU: real`: Z coordinate of upper end $\mathrm{[L\]}$.
    - Y coordinate of upper end is equal to zero
    - Z coordinate is positive upwards
    - `ZU=0.0` at still water level (see the figure 'Topology of system SA' above).
- `ALFL: real, default: 0.0`: Angle of lower end from vertical $\mathrm{[deg\]}$.
- `ALFU: real, default: 0.0`: Angle of upper end from vertical $\mathrm{[deg\]}$.

If the lower/upper end later in the specification is allowed to rotate freely around the y-direction,
ALFL/ALFU will be dummy.




#### Supernode types {#inpmod_b_SA_supernode_types}
`NSNOD-2` input lines. `ISNOD` must be given in increasing order from 2 to `NSNOD-2`. Only to be given if
`NSNOD>2`.
~~~
ISNOD ITYPSN
~~~
- `ISNOD: integer`: Supernode ISNOD=2,3,....., NSNOD-1
- `ITYPSN: character(6)`: Type of supernode
    - `TSNBRA` - Branch point
    - `TSNFRE` - Free end

Specification of supernodes:
Supernode at lower and upper end are not to be specified. Supernode number at lower end
is automatically set to 1 and the supernode type is fixed (`ITYPSN`=`TSNFIX`). Supernode at
upper end is automatically set to `NSNOD` and the supernode type is specified position 
(`ITYPSN`=`TSNPOS`) indicating that the upper end is connected to the support vessel.




#### Support vessel reference {#inpmod_b_SA_support_vessel_reference}
~~~
IVES IDWFTR XG YG ZG DIRX
~~~
- `IVES: integer, default: 1`: Vessel number (`IVES` = 1)
- `IDWTFR: character (6), default: 'NONE'`: Identifier for WF motion transfer function
    - `IDWFTR = 'NONE'` means no transfer function specified.
- `XG: real`:X position of vessel coordinate system referred in global system $\mathrm{[L\]}$
- `YG: real`:Y position of vessel coordinate system referred in global system $\mathrm{[L\]}$
- `ZG: real`:Z position of vessel coordinate system referred in global system $\mathrm{[L\]}$
    - Confer [Data Group E: Support Vessel Data](@ref inpmod_e).
- `DIRX: real`: Direction of vessel X-axis.
    - See [Location of support vessel coordinate system] (@ref Location_of_support_vessel_coordinate_system).

Next data group is [Line and segment specification](@ref inpmod_b_line_line_and_segment).




###  Standard system SB {#inpmod_b_SB_standard_system}
Multiple seafloor contact points are allowed, with upper end connected to the support vessel. The
frequently used lazy wave, lazy S and free hanging configurations are special cases of the SB system. The initial
configuration of this system is two-dimensional in X-Z plane.


##### Topology
In addition to the branching feature of system SA it is also allowed to specify seafloor tangent and
intermediate seafloor anchor point.

![Topology of system SB](@ref figures/um_ii_fig18.svg)
@image latex figures/um_ii_fig18.pdf "Topology of system SB" width=12cm

-   Vertical branches with free ends are specified as for system SA
-   One anchor point can be specified (in addition to supernode 1)
-   Horizontal seafloor tangent can be specified




#### Data group identifier {#inpmod_b_SB_data_group_identifier}
~~~
SINGle RISEr SB
~~~




#### Definition of topology {#inpmod_b_SB_definition_of_topology}
~~~
NSNOD IBTANG
~~~
- `NSNOD: integer`: Number of supernodes
- `IBTANG: integer, default: 0`: Bottom tangent option
    - `IBTANG=0`: No seafloor contact
    - `IBTANG = 1`: Seafloor contact forces on all nodes that are
      below `Z < ZBOT + R_EXTCNT`. The modified 3D seafloor
      formulation is used. Friction contribution to torsional loading
      is possible.
    - `IBTANG = -1`: Equivalent with setting `IBTANG=1`.
    - `IBTANG = -9`: Seafloor contact forces on all nodes that are
      below `Z < ZBOT` using the original flat bottom formulation. If
      `IBOT3D = 1`, `IBTANG` is set to 1. This option is deprecated.

In the static `CAT`-analysis only contact in the vicinity of supernode 1
is included. Contact forces on all nodes that are below `ZL` are 
considered in static `FEM` analysis and dynamic analysis.

Note that flat bottom topology based on original FORTRAN code is planned to be removed and substituted by
the general 3D seafloor contact formulation FORTRAN code. The old code will be kept for debugging
purposes.




#### Line, line type and supernode connectivity {#inpmod_b_SB_line_line_type}
This data group defines the connectivity between lines and supernodes. If the line identifier is missing
the line number implicitly defined by the order in which the lines are specified, will be used as the line
identifier. References to line type IDs and supernode numbers are mandatory.

The lines must be specified in the order indicated in the figure 'Topology of system SB' above. 
This means that the lines are given continuously from seafloor to upper riser end.

At each branching point the branching line(s) are specified before the next line in the main riser configuration. 
No ball joint components are accepted in branch lines.

`NLIN (=NSNOD-1)` input lines
~~~
LINE-ID LINTYP-ID ISNOD1 ISNOD2
~~~
- `LINE-ID: character(8)`: Line identifier
- `LINTYP-ID: character(8)`: Reference to line type identifier
- `ISNOD1: integer`: Reference to supernode number at end 1
- `ISNOD2: integer`: Reference to supernode number at end 2

If only 1 alphanumeric string and 2 integers are specified, the string is interpreted as `LINTYP-ID`.
~~~
LINTYP-ID ISNOD1 ISNOD2
~~~
The `LINE-ID` is taken as the line number as implicitly defined by the order in which the lines are
given.




#### Boundary conditions {#inpmod_b_SB_boundary_conditions}
~~~
ZL XU ZU ALFL ALFU ZA XA
~~~
- `ZL: real`: Z-coordinate of lower end $\mathrm{[L\]}$
    - ZL will also be used as Z-coordinate of seafloor if `IBTANG>0`
- `XU: real > 0`: X-coordinate of upper end $\mathrm{[L\]}$
- `ZU: real`: Z-coordinate of upper end $\mathrm{[L\]}$
- `ALFL: real`: Angle of lower end from vertical $\mathrm{[deg\]}$
    - Dummy when seafloor contact is specified (i.e. `IBTANG/=0`)
- `ALFU: real`: Angle of upper end from vertical $\mathrm{[deg\]}$
- `ZA: real >= ZL`: Z-coordinate of anchor point $\mathrm{[L\]}$
    - Dummy if no anchor point is specified
- `XA: real`: X-coordinate of anchor point $\mathrm{[L\]}$
    - Required input when static `FEM` analysis is applied. The X-location of
the anchor point is automatically computed so that the anchor line is
vertical if the `CAT` or `CATFEM` analysis is used in `STAMOD` (i.e. `XA` is
dummy). `XA` is also dummy when no anchor point is specified.

If the lower/upper end later in the specification is allowed to rotate freely around the Y-axis,
`ALFL`/`ALFU` will be dummy.




#### Supernode types {#inpmod_b_SB_supernode_types}
`NSNOD-2` input lines. `ISNOD` must be given in increasing order from 2 to `NSNOD-2`. Only to be given if
`NSNOD>2`.

~~~
ISNOD ITYPSN
~~~
- `ISNOD: integer`: Supernode no = 2,3,....., NSNOD-1
- `ITYPSN: character(6)`: Type of supernode
    - `TSNFIX` - Fixed
    - `TSNBRA` - Branch point
    - `TSNFRE` - Free end

Specification of supernodes: 
Supernodes at lower and upper end are not to be specified. The supernode number at lower
end is automatically set to 1 and the supernode type is fixed (`ITYPSN=TSNFIX`). The 
supernode at upper end is automatically set to NSNOD and the supernode type is specified 
position (`ITYPSN=TSNPOS`) indicating the upper end is connected to the support vessel. A
possible additional anchor point is defined by specification of a supernode of type `TSNFIX`.
The additional anchor line must be connected to the first branching point along the main
riser.




#### Seafloor support conditions {#inpmod_b_SB_seafloor_support}
To be given only if `IBTANG`=1, -1 or -9.
~~~
STFBOT STFAXI STFLAT FRIAXI FRILAT DAMBOT DAMAXI DAMLAT ILTOR
~~~
- `STFBOT: real > 0`: Seafloor stiffness normal to the seafloor $[\mathrm{F/L^2}\]$ 
- `STFAXI: real >= 0, default: 0`: In-plane seafloor stiffness for friction in axial direction $[\mathrm{F/L^2}\]$
- `STFLAT: real >= 0, default: 0`: In-plane seafloor stiffness for friction in lateral direction $[\mathrm{F/L^2}\]$
- `FRIAXI: real >= 0, default: 0`: In-plane seafloor friction coefficient in axial direction [1]
- `FRILAT: real >= 0, default: 0`: In-plane seafloor friction coefficient in lateral direction [1]
- `DAMBOT: real >= 0, default: 0`: seafloor damping coefficient normal to the seafloor $[\mathrm{F\times T/L^2}\]$
    - Dummy for IBTANG=-9 
- `DAMAXI: real >= 0, default: 0`: In-plane seafloor damping coefficient in axial direction $[\mathrm{F\times T/L^2}\]$
    - Dummy for IBTANG=-9 
- `DAMLAT: real >= 0, default: 0`: In-plane seafloor damping coefficient in lateral direction $[\mathrm{F\times T/L^2}\]$
    - Dummy for IBTANG=-9 
- `ILTOR: integer, default: 0`: Option for applying lateral contact forces at the external contact radius, giving a torsional moment
    - `= 0`: Lateral loads are applied at the node
    - `= 1`: Lateral loads are applied at the external contact radius if it is specified for the associated beam cross-section.
    - Dummy for IBTANG=-9 


`STFBOT` is used for computing the spring stiffness normal to the seafloor, $\mathrm{k_V}$ , for seafloor contact. $\mathrm{k_V}$ = `STFBOT` $\mathrm{\times L}$ where $\mathrm{L}$ is the element length.

Horizontal contact with the seafloor is modelled independently in the axial and lateral directions.
Contact is initially modelled with linear springs. Sliding will occur when an axial or lateral spring
force reaches the friction force value. Springs will be reinstated if the line starts sliding in the opposite
direction, or if the friction force increases and is greater than the spring force. The spring
stiffness is calculated as $\mathrm{k_s}$ = `STFxxx` $\mathrm{\times L_h}$, where $\mathrm{L_h}$ is the length of the element's horizontal projection. 
The seafloor friction forces are calculated as F = `FRIxxx` $\mathrm{\times F_{vert}}$ and are directed against the
axial or lateral displacements.




#### Support vessel reference {#inpmod_b_SB_support_vessel}
Identification and location of support vessel.
~~~
IVES IDWFTR XG YG ZG DIRX
~~~
- `IVES: integer, default: 1`: Vessel number (`IVES` = 1)
- `IDWTFR: character (6), default: 'NONE'`: Identifier for WF motion transfer function
    - IDWFTR = 'NONE' means no transfer function specified
- `XG: real`: X position of vessel coordinate system referred in global system $\mathrm{[L\]}$
- `YG: real`: Y position of vessel coordinate system referred in global system $\mathrm{[L\]}$
- `ZG: real`: Z position of vessel coordinate system referred in global system $\mathrm{[L\]}$
    - Confer [Data Group E: Support Vessel Data](@ref inpmod_e).
- `DIRX: real`: Direction of vessel X-axis.
    - See [Location of support vessel coordinate system] (@ref Location_of_support_vessel_coordinate_system).

Next data group is [Line and segment specification](@ref inpmod_b_line_line_and_segment).

![Vertical spring stiffness for seafloor contact](@ref figures/um_ii_fig27.svg)
@image latex figures/um_ii_fig27.pdf "Vertical spring stiffness for seafloor contact" width=8cm




###  Standard system SC {#inpmod_b_SC_standard_system}
Free lower end, suspended from surface vessel. This is a topologically simple system, with only two supernodes and one line.




#### Data group identifier {#inpmod_b_SC_data_group}
~~~
SINGle RISEr SC
~~~




#### Boundary conditions {#inpmod_b_SC_boundary}
~~~
ZU ALFU
~~~
- `ZU: real`: Z-coordinate of upper end $\mathrm{[L\]}$
- `ALFU: real`: Angle of upper end from vertical $\mathrm{[deg\]}$

If the upper end later in the specification is allowed to rotate freely around the Y-axis,
ALFU will be dummy.




#### Line and line type {#inpmod_b_SC_line}
~~~
LINE-ID LINTYP-ID
~~~
- `LINE-ID: character(8)`: Line identifier 
- `LINTYP-ID: character(8)`: Reference to line type identifier

If only 1 alphanumeric string is specified, the string is interpreted as `LINTYP-ID`.
~~~
LINTYP-ID
~~~
The `LINE-ID` is taken as the line number (=1)

Numbering of supernodes:
-   `ISNOD = 1` is lower end (free)
-   `ISNOD = 2` is upper end (specified position)




#### Support vessel reference {#inpmod_b_SC_support_vessel}
Identification and location of support vessel.
~~~
IVES IDWFTR XG YG ZG DIRX
~~~
- `IVES: integer, default: 1`: Vessel number (`IVES` = 1)
- `IDWTFR: character (6), default: 'NONE'`: Identifier for WF motion transfer function
    - IDWFTR = 'NONE' means no transfer function specified
- `XG: real`: X position of vessel coordinate system referred in global system $\mathrm{[L\]}$
- `YG: real`: Y position of vessel coordinate system referred in global system $\mathrm{[L\]}$
- `ZG: real`: Z position of vessel coordinate system referred in global system $\mathrm{[L\]}$
    - Confer [Data Group E: Support Vessel Data](@ref inpmod_e).
- `DIRX: real`: Direction of vessel X-axis.
    - See [Location of support vessel coordinate system] (@ref Location_of_support_vessel_coordinate_system).

Next data group is [Line and segment specification](@ref inpmod_b_line_line_and_segment).




###  Standard system SD {#inpmod_b_SD_standard}
Free upper end.




#### Data group identifier {#inpmod_b_SD_data}
~~~
SINGle RISEr SD
~~~




#### Boundary condition {#inpmod_b_SD_boundary}
~~~
ZL ALFL
~~~
- `ZL: real`: Z-coordinate of lower end $\mathrm{[L\]}$
- `ALFU: real`: Angle of lower end from vertical $\mathrm{[deg\]}$

If the lower end later in the specification is allowed to rotate freely around the Y-axis,
`ALFL` will be dummy.




#### Line and line type {#inpmod_b_SD_line}
~~~
LINE-ID LINTYP-ID
~~~
- `LINE-ID: character(8)`: Line identifier 
- `LINTYP-ID: character(8)`: Reference to line type identifier

If only 1 alphanumeric string is specified, the string is interpreted as `LINTYP-ID`.
~~~
LINTYP-ID
~~~
The `LINE-ID` is taken as the line number (=1)

Numbering of supernodes:
-   `ISNOD = 1` is lower end, (fixed)
-   `ISNOD = 2` is upper end, (free)

Next data group is [Line and segment specification](@ref inpmod_b_line_line_and_segment).




###  Arbitrary system AR {#inpmod_b_arbitrary_arbitrary}

This type of specification can be used to model:

-  any of the previously specified systems
-  systems with complex topology not covered by the standard systems
-  systems for which boundary conditions are not covered by SA-SD systems

For this class of systems the topology must be described in detail. Boundary
conditions corresponding to a 1) stress-free configuration, as well as 2)
the wanted static configuration and parameters for a load incrementation
procedure from 1) to 2) must be specified. The load incrementation procedure
is specified as input to the `STAMOD` module.




#### Data group identifier {#inpmod_b_arbitrary_data_group_identifier}

~~~
ARBItrary SYSTem AR
~~~




#### Topology {#inpmod_b_arbitrary_topology}

~~~
NSNOD NLIN NSNFIX NVES NRICON NSPR NAKC
~~~
- `NSNOD: integer`: Total number of supernodes
- `NLIN: integer, default: NSNOD-1`: Number of lines
- `NSNFIX: integer, default: 1`: Number of supernodes having one or more degrees of freedom that are fixed or prescribed
- `NVES: integer, default: 0`: Number of support vessels
- `NRICON: integer, default: 0`: Number of rigid supernode connections. Relevant for modelling of stiff connections between supernodes. The connection is described by specification of a master and a slave (dependent) node, see [Rigid supernode connections](@ref inpmod_b_arbitrary_rigid)
- `NSPR: integer, default: 0`: Number of global springs
- `NAKC: integer, default: 0`: Number of kill and choke lines. Relevant for modelling of tensioned risers only (Deprecated functionality)




#### Seafloor support conditions {#inpmod_b_arbitrary_seafloor_support_conditions}




##### Seafloor contact specification
~~~
IBTANG ZBOT IBOT3D
~~~

- `IBTANG: integer, default: 0`: Bottom tangent option.
    - `IBTANG = 0`: No seafloor contact
    - `IBTANG = 1`: Seafloor contact forces on all nodes that are
      below `Z < ZBOT + R_EXTCNT`. The modified 3D seafloor
      formulation is used. Friction contribution to torsional loading
      is possible.
    - `IBTANG = 2`: `CARISIMA` seafloor interaction model. Restricted option
    - `IBTANG = 3`: Seafloor contact elements will be added according
      to the specification given in the data group SEAFLOOR CONTACT
      SPECIFICATION.
    - `IBTANG = -1`: Equivalent with setting `IBTANG=1`.
    - `IBTANG = -9`: Seafloor contact forces on all nodes that are
      below `Z < ZBOT` using the original flat bottom formulation. If
      `IBOT3D = 1`, `IBTANG` is set to 1. This option is deprecated.
- `ZBOT: real`: Z-coordinate of seafloor (`ZBOT < 0`). $\mathrm{[L\]}$ 
    - Dummy variable if `IBTANG = 0` or `IBOT3D = 1`.
- `IBOT3D: integer, default: 0`: Code for 3D bottom
    - `IBOT3D = 0`: flat bottom at depth `ZBOT`
    - `IBOT3D = 1`: 3D topology, file to be specified in input to STAMOD

Note that flat bottom topology based on original Fortran code is planned to be
removed and substituted by the general 3D seafloor contact formulation
FORTRAN code. The old code will be kept for debugging purposes.




##### Seafloor stiffness, friction and damping 

The following input line must only be given if `IBTANG=1`, `IBTANG=-1` or `IBTANG=-9`
~~~
STFBOT STFAXI STFLAT FRIAXI FRILAT DAMBOT DAMAXI DAMLAT ILTOR
~~~
- `STFBOT: real > 0`: Seafloor stiffness normal to the seafloor $[\mathrm{F/L^2}\]$ 
- `STFAXI: real >= 0, default: 0`: In-plane seafloor stiffness for friction in axial direction $[\mathrm{F/L^2}\]$
- `STFLAT: real >= 0, default: 0`: In-plane seafloor stiffness for friction in lateral direction $[\mathrm{F/L^2}\]$
- `FRIAXI: real >= 0, default: 0`: In-plane seafloor friction coefficient in axial direction [1]
- `FRILAT: real >= 0, default: 0`: In-plane seafloor friction coefficient in lateral direction [1]
- `DAMBOT: real >= 0, default: 0`: seafloor damping coefficient normal to the seafloor $[\mathrm{F\times T/L^2}\]$
    - Dummy for IBTANG=-9 
- `DAMAXI: real >= 0, default: 0`: In-plane seafloor damping coefficient in axial direction $[\mathrm{F\times T/L^2}\]$
    - Dummy for IBTANG=-9 
- `DAMLAT: real >= 0, default: 0`: In-plane seafloor damping coefficient in lateral direction $[\mathrm{F\times T/L^2}\]$
    - Dummy for IBTANG=-9 
- `ILTOR: integer, default: 0`: Option for applying lateral contact forces at the external contact radius, giving a torsional moment
    - `= 0`: Lateral loads are applied at the node
    - `= 1`: Lateral loads are applied at the external contact radius if it is specified for the associated beam cross-section.
    - Dummy for IBTANG=-9 


`STFBOT` is used for computing the vertical spring stiffness, $\mathrm{k_V}$ , for seafloor contact. $\mathrm{k_V}$ = `STFBOT` $\mathrm{\times L}$ where $\mathrm{L}$ is the element length.

Horizontal contact with the seafloor is modelled independently in the axial and lateral directions.
Contact is initially modelled with linear springs. Sliding will occur when an axial or lateral spring
force reaches the friction force value. Springs will be reinstated if the line starts sliding in the opposite
direction, or if the friction force increases and is greater than the spring force. The spring
stiffness is calculated as $k_h=\mathrm{Stalks}\times L_h$, where $\mathrm{L_h}$ is the length of the element's horizontal projection. 
The seafloor friction forces are calculated as $F=\mathrm{FRIxxx}\times F_{vert}$ and are directed against the
axial or lateral displacements, where $\mathrm{F_{vert}}$ is the vertical contact force between the pipe and the bottom.




##### To be given only if `IBTANG = 2` (Restricted option) and `IBOT3D = 0`

~~~
PHIG PHIS ZCUT X0 Y0
~~~

- `PHIG: real, default: 0`: Angle anti-clockwise from X-axis to largest gradient $[\mathrm{deg}\]$
- `PHIS: real, default: 0`: Slope of seafloor $[\mathrm{deg}\]$
- `ZCUT: real, default: 0`: Elements above `ZCUT` ignored in contact analysis $[\mathrm{L}\]$
- `X0: real, default: 0`: X position of seafloor origin with depth `ZBOT` $[\mathrm{L}\]$
- `Y0: real, default: 0`: Y position of seafloor origin with depth `ZBOT` $[\mathrm{L}\]$

Giving a low `ZCUT` increases efficiency, but should not be given lower than the highest position of any point actually in contact with the seafloor.





#### Line, line type and supernode connectivity {#inpmod_b_arbitrary_line}

This data group defines the connectivity between lines and supernodes. If the
line identifier is missing the line number implicitly defined by the order in
which the lines are specified, will be used as the line identifier.
References to line type IDs and supernode IDs are mandatory.

`NLIN` input lines.

~~~
LINE-ID LINTYP-ID SNOD-ID1 SNOD_ID2
~~~
- `LINE-ID: character(8)`: Line identifier
- `LINTYP-ID: character(8)`: Reference to line type identifier
- `SNOD-ID1: character(8)`: Reference to supernode identifier at end 1
- `SNOD-ID2: character(8)`: Reference to supernode identifier at end 2

If only 3 alphanumeric strings are specified, the first string is taken as `LINTYP-ID`, the second as `SNOD-ID1` and the third as `SNOD-ID2`:
~~~
LINTYP-ID SNOD-ID1 SNOD-ID2
~~~
The `LINE-ID` is taken as the line number as implicitly defined by the
order in which the lines are given.

The local element y- and z-axes are found from local x-axis and a
reference vector. 

The local element x-axis goes from end 1 to end 2 of the element. 

The reference vector may be specified using the option 
[LOCAL ELEMENT AXIS](@ref inpmod_af_local).

If the line is a blade in a wind turbine and `LOCAL ELEMENT AXIS` is
not specified, the reference vector will be found as the cross product
between the local X-axis of the shaft and the local X-axis of the
blade element.

If the reference is not given by either of these two methods, the
default method will be used. If the local x-axis is not parallel with
the global z-axis, the reference vector is found as the cross product
between the local x-axis and the global z-axis. If the local x-axis is
parallel with the global z-axis, the global y-axis will be used as the
reference vector if the local x-axis is completely vertical or tilted
slightly in the positive global x-direction. Otherwise the reference
vector will point in the negative global y-direction.

The local z-axis is found as the cross product between the local
x-axis and the reference vector.

The local y-axis is then found as the cross product between the local
z-axis and the local x-axis.

For beam elements, the element axes are found at the stress-free
configuration and will subsequently follow the element.




#### Specification of boundary conditions, stressfree configuration and static equilibrium configuration {#inpmod_b_arbitrary_specification}

Coordinates of all supernodes must be specified to define the initial
stressfree configuration as well as the final static configuration.
If the distance between supernodes in stressfree configuration do not
correspond to the line length as specified in [Type and location of contact point, NCNODE input lines](@ref inpmod_b_elastic_type ), the length of the last
segment in the line is adjusted, and a warning is written.




##### Boundary conditions and coordinates for supernodes with at least one fixed or prescribed degree of freedom {#inpmod_b_arbitrary_boundary_conditions}

The following two or three input lines must be given in blocks for each of the `NSNFIX` supernodes.

Boundary conditions:
~~~
SNOD_ID IPOS IX IY IZ IRX IRY IRZ CHCOO CHUPRO
~~~

- `SNOD_ID: character(8)`: Supernode identifier 
- `IPOS: integer, default: 0`: Boundary condition type
    - `IPOS = 0`: The supernode is not connected to a support vessel
    - `IPOS = IVES`: The supernode is connected to support vessel number `IVES`, `1 <= IVES <= NVES`.
- `IX: integer, default: 1`: Boundary condition code for translation in X-direction
    - `IX = 0`: Free
    - `IX = 1`: Fixed or prescribed
- `IY: integer, default: 1`: Boundary condition code for translation in Y-direction (same
    interpretation as for `IX`)
- `IZ: integer, default: 1`: Boundary condition code for translation in Z-direction (same
    interpretation as for `IX`)
- `IRX: integer, default: 1`: Boundary condition code for rotation about X-axis (same
    interpretation as for `IX`)
- `IRY: integer, default: 1`: Boundary condition code for rotation about Y-axis (same
    interpretation as for `IX`)
- `IRZ: integer, default: 1`: Boundary condition code for rotation about Z-axis (same
    interpretation as for `IX`)
- `CHCOO: character(6)`: Identifier for boundary condition reference coordinate system
    - `CHCOO = GLOBAL`: Boundary conditions are referenced to global coordinate
                    system.
    - `CHCOO = SKEW-G`: Boundary conditions are referenced to a skew coordinate
                    system.
    - `CHCOO = VESSEL`: Boundary conditions are referenced to vessel coordinate
                    system.
    - `CHCOO = SKEW-V`: Boundary conditions are referenced to a skew
                    vessel coordinate system.
- `CHUPRO: character(3), default: NO`: Computational parameter. Boundaries rotate with specified rotation
    - `CHUPRO = YES`
    - `CHUPRO = NO`

A supernode with prescribed motions during dynamic analysis must have `IPOS>0`.

Possible hinges at riser ends connected to fixed supports or to a
support vessel may be modelled by
either choosing the correct boundary condition code (see above) or using
ball-joint connectors. Be careful not to use both these modelling
options at the same time for a given super-node. This will lead to
program abortion.

Note that if some of the translations are not prescribed,
rotation-induced translations may cause drift-off if used in
combination with global boundary conditions at a node attached to a
vessel. 


Coordinates for stress free and static equilibrium position:
~~~
X0 Y0 Z0 X1 Y1 Z1 ROT DIR
~~~

- `X0: real`: Coordinates for stress free configuration specified so that the
    line between any two supernodes are straight and with zero tension. $[\mathrm{L}\]$
- `Y0: real`: As for `X0`
- `Z0: real`: As for `X0`
- `X1: real, default: X0`: 
- `Y1: real, default: Y0`: Coordinates for static equilibrium position $[\mathrm{L}\]$
- `Z1: real, default: Z0`
- `ROT: real, default: 0`: Specified rotation of supernode from stress free position
    to static equilibrium position $\mathrm{[deg\]}$
- `DIR: real, default: 0`: Direction of axis for specified rotation $\mathrm{[deg\]}$

`ROT` is the specified rotation in degrees from stress free position
to equilibrium position and is analogous to `ALFL`/`ALFU` parameters
used for the standard systems. The rotation `ROT` will be around the
local `YREF`-axis as shown in the figure below.
`DIR` is the rotation in degrees from global X-axis to `XREF`-axis.
The local `ZREF`-axis is parallel to global Z-axis.
`DIR=0` signifies that the rotation `ROT` will be around the global
Y-axis. If the line end is allowed to rotate freely around the
local `YREF`-axis, `ROT` will be dummy. Free rotation around global
Y-axis is obtained with `IRY = 0` and `DIR = 0`.

![Definition of rotation axis YREF versus global coordinate system, X, Y. The supernode is located in the origin](@ref figures/um_ii_fig36.svg)
@image latex figures/um_ii_fig36.pdf "Definition of rotation axis YREF versus global coordinate system, X, Y. The supernode is located in the origin" width=8cm

Definition of skew coordinate system
One input line only if `CHCOO` = 'SKEW-G' OR 'SKEW-V'
~~~
XX XY XZ XP YP ZP
~~~

- `XX: real`: Components of the skew X-axis referred to the global system. $[\mathrm{L}\]$. See figure below.
- `XY: real`: As for `XX`.
- `XZ: real`: As for `XX`.
- `XP: real`: Components of a reference vector from the supernode to a point in
the skew XY-plane, referred to global system $[\mathrm{L}\]$
- `YP: real`: As for `XP`
- `ZP: real`: As for `XP`

The skew Z-axis is found by the cross product between the skew X-axis and the reference vector.
The skew Y-axis is found by the cross product between the skew Z-axis and the skew X-axis

![Definition of skew boundary system.](@ref figures/um_ii_fig37.svg)
@image latex figures/um_ii_fig37.pdf "Definition of skew boundary system." width=12cm




##### Coordinates for completely free supernodes {#inpmod_b_arbitrary_coordinates}

This input group consists of `NSNFRE` input lines, where `NSNFRE=NSNOD-NSNFIX` gives the number
of supernodes where all degrees of freedom are free. Skip this group if `NSNFRE=0`.

~~~
SNOD-ID X0 Y0 Z0
~~~

- `SNOD-ID: character(8)`: Supernode identifier 
- `X0: real`: Nodal coordinate in stress free configuration $[\mathrm{L}\]$
- `Y0: real`: Nodal coordinate in stress free configuration $[\mathrm{L}\]$
- `Z0: real`: Nodal coordinate in stress free configuration $[\mathrm{L}\]$




#### Support vessel reference {#inpmod_b_arbitrary_support}
Identification and location of support vessel, `NVES` input lines

~~~
IVES IDWFTR XG YG ZG DIRX
~~~

- `IVES: integer, default: 1`: Vessel number, `1 <= IVES <= NVES`.
- `IDWFTR: character(6), default: 'NONE'`: Identifier for support vessel motion transfer function
    - `IDWFTR = 'NONE'` means no transfer function specified 
- `XG: real`: X position of vessel coordinate system referred in global system $[\mathrm{L}\]$
- `YG: real`: Y position of vessel coordinate system referred in global system $[\mathrm{L}\]$
- `ZG: real`: Z position of vessel coordinate system referred in global system $[\mathrm{L}\]$
    - Confer [Data Group E: Support Vessel Data](@ref inpmod_e)
- `DIRX: real`: Direction of vessel X-axis. 
    - See [Location of support vessel coordinate system](@ref Location_of_support_vessel_coordinate_system).




#### Description of global springs {#inpmod_b_arbitrary_description_of_global}

To be specified if `NSPR>0`
The input lines below ('Spring localization and properties' and 'Nonlinear spring stiffness') must be given in one block for each global spring.




##### Spring location and properties {#inpmod_b_arbitrary_spring}

~~~
LINE-ID ISEG INOD ILDOF STIFF/NPAIR DAMP A2
~~~

- `LINE-ID: character (8)`: Line identifier
- `ISEG: integer`: Local segment number within line 
- `INOD: integer`: Local node number within actual segment 
- `ILDOF: integer`: Local degree of freedom
    - =1 global X-direction
    - =2 global Y-direction
    - =3 global Z-direction
    - =4 rotation around global X-axis
    - =5 rotation around global Y-axis
    - =6 rotation around global Z-axis
    - = 12 or 21 translation in global XY-plane
    - = 13 or 31 translation in global XZ-plane
    - = 23 or 32 translation in global YZ-plane 
- `STIFF/NPAIR` 
    - `STIFF: real >= 0`: Constant spring stiffness $[\mathrm{F/L}\]$ or $[\mathrm{FL/deg}\]$
    - `NPAIR: integer <= -2`: `NPAIR` is number of force-displacement or moment-rotation relations in spring specification
- `DAMP: real, default: 0`: Linear damping coefficient $[\mathrm{FT/L}\]$ or $[\mathrm{FLT/deg}\]$
- `A2: real, default: 0`: Stiffness proportional damping factor




##### Nonlinear spring stiffness {#inpmod_b_arbitrary_nonlinear}

The following input line is to be given if `NPAIR` >= 2

~~~
PON(1) DISPL(1)...............PON(NPAIR) DISPL(NPAIR)
~~~

- `PON(1): real`: Spring force $[\mathrm{F}\]$ or moment $[\mathrm{FL}\]$ corresponding to 
- `DISPL(1): real`: Spring displacement $[\mathrm{L}\]$ or $[\mathrm{deg}\]$

All `NPAIR` pairs of `PON` and `DISPL` values are given on a single
input line. The values of `PON` and `DISPL` must be monotonically
increasing; `PON(1) < PON(2) < ... < PON(NPAIR)` and `DISPL(1) <
DISPL(2) < ... < DISPL(NPAIR)`.

For `ILDOF > 6`, the first pair of values must both be zero; i.e. $\mathrm{\:}$ `PON(1) = DISPL(1) = 0.0`.




#### Description of kill and choke lines (deprecated functionality) {#inpmod_b_arbitrary_description_of_kill}

NAKC input lines.

~~~
IKCTYP DIAAKC MASAKC FLUAKC TENAKC NLINKC LINE-ID(1) ... LINE-ID(nlinkc)
~~~

- `IKCTYP: integer`: Type of kill and choke line
    - `IKCTYP = 1`: Internal line
    - `IKCTYP = 2`: External line
- `DIAAKC: real, default: 0`: Outer diameter of kill and choke line $[\mathrm{L}\]$
- `MASAKC: real, default: 0`: Mass per unit length of kill and choke line excluding contents $[\mathrm{M/L}\]$
- `FLUAKC: real, default: 0`: Mass per unit length of fluid contents of kill and choke line $[\mathrm{M/L}\]$
- `TENAKC: real, default: 0`: Tension of kill and choke line $[\mathrm{F}\]$
- `NLINKC: integer, default: 1`: Number of riser lines this kill and choke line is attached to
- `LINE-ID(1): character(8)`: Reference to line identifiers (Adjacent lines)
- .
- .
- .
- `LINE-ID(nlinkc)`:

LINE-IDs must be given in correct order from lower end to upper end.
Tension will be applied at the supernode at the second end of line
`LINE-ID(nlinkc)`

If tension is zero, an internal line will be fixed at the upper end.




#### Rigid supernode connections {#inpmod_b_arbitrary_rigid}

In present version only to be applied for static and non-linear dynamic analysis.

This option enables the user to model rigid connections between supernodes. A rigid connection is
modelled by specifying a master - and a slave node. Both the master and the slave have initially to be
defined as free nodes. The theoretical formulation is a special application of linear constraints between
degrees of freedom.

NRICON input lines.
~~~
CHMAST CHSLAV
~~~

- `CHMAST: character`: Reference to supernode identifier, `SNOD-ID`, specified as the master node
- `CHSLAV: character`: Reference to supernode identifier, `SNOD-ID`, specified as the slave node

Note that:
- Both the master and the slave node have initially to be defined as free nodes.
- A master node can not be slave of another master node.
- A slave node can only be slave of one master node.
- An arbitrary number of slave nodes can have the same master node.
- The number of DOFs at the slave node must not exceed the number of DOFs at the master
node.




###  Seafloor contact specification {#inpmod_b_seafloor_contact_spec}

This data group must be given for Arbitrary Systems AR-sytems with
`IBTANG = 3`.


#### Data group identifier, one input line {#inpmod_b_seafloor_contact_id}

~~~
SEAFloor CONTact SPECification
~~~


#### Seafloor contact specification {#inpmod_b_seafloor_contact_data}

~~~
NSPEC
~~~

- `NSPEC: integer > 0`: Number of input lines to be given with
  seafloor contact specification


NSPEC input lines
~~~
CMPTYP-ID LINE-ID ISEG1 ISEG2 ... ISEGn
~~~

- `CMPTYP-ID: character(8)`: Reference to a seafloor contact component identifier. Must be of type `SPRI` or `SOIL`.
- `LINE-ID: character(8)`: Reference to a line identifier
- `ISEG1: integer >= 0, default: 0`: Segment for which seafloor contact of type `CMPTYP-ID` is possible.
    - `ISEG1 = 0`: Seafloor contact is possible for all segments in line `LINE-ID`
    - `ISEG1 > 0`: First segment for which seafloor contact is possible.
- `ISEG2: integer != 0`: Segment for which seafloor contact of type `CMPTYP-ID` is possible.
    - `ISEG2 > 0`: Second segment for which seafloor contact is possible.
    - `ISEG2 < 0`: Seafloor contact is possible for all segments from ISEG1 to ABS(ISEG2).
- `ISEGn: integer !=0`: Last segment for which seafloor contact of type `CMPTYP-ID` is possible. 
    - `ISEGn > 0`: Last segment for which seafloor contact is possible.
    - `ISEGn < 0`: Seafloor contact is possible for all segments from the previous specified segment to ABS(ISEGn).


Pairs of a positive and a negative segment number may be given
anywhere in the sequence.

Note that a segment may only have one seafloor contact.


###  Elastic contact surface {#inpmod_b_elastic_elastic}
This data group is optional and is available as additional information for Arbitrary Systems only. It
enables the user to model contact effects between lines. For normal riser systems this data group should not be considered.

The main intention of this data group is to enable modelling of pipelines during laying operations. This
includes contact forces between the pipe and rollers on the lay barge/stinger and applied tension from a tensioner.

Contact between roller and pipe is modelled by a bi-linear or non-linear spring and a bi-linear dash pot
damper. The contact force acts normal to the pipe and the roller. It is treated as a discrete element load acting on the pipe, 
while the contact load acting on the roller is transferred
as a nodal force to the stinger. The last includes possible torsional moment.

The term *contact surface* is introduced to cover stinger modelling. The stinger may be fixed or hinged to
the vessel. Generally it is curved and may consist of a rigid part following the vessel motions and a flexible part.

The term *contact point* is defined as the location of rollers or tensioner on the stinger.

![Elastic contact surface](@ref figures/um_ii_fig41.svg)
@image latex figures/um_ii_fig41.pdf "Elastic contact surface" width=12cm




#### Contact surface modelling 

A complete model of an elastic contact surface includes the following information:

- Number of lines describing the surface
The surface may consist of several adjacent lines. By introducing several adjacent lines it is
possible to model a contact surface which has a curved stress-free initial configuration. In addition 
boundary conditions for the super-nodes at the line intersections can be specified. This is
necessary to model prescribed displacements due to vessel motions.
- Type and location of contact points
Contact points can be of roller and/or tensioner type and have to be located at ends of line segments.
- Identification of lines which may experience contact with the contact surface.
The line identification is used to limit the number of elements that have to be checked for contact during program execution.

Supplementary information is specified in the following data groups:
- [System topology and boundary conditions](@ref inpmod_b_arbitrary_arbitrary)
- [Line and segment specification](@ref inpmod_b_line_line_and_segment)
- [Contact point specification of roller type](@ref inpmod_c_contact)
- [Contact point specification of tensioner type](@ref inpmod_c_tensioner)
- [Tubular contact point specification](@ref inpmod_c_tubular)




#### Data group identifier, one input line {#inpmod_b_elastic_data}

~~~
ELAStic CONTact SURFace
~~~




#### Specification of elastic contact surface(s), one input line {#inpmod_b_elastic_specification_of_elastic}

~~~
NSURFE
~~~

- `NSURFE: integer > 0`: The number of elastic contact surfaces to be specified




#### Description of the contact surface(s) and specification of the line(s) which may experience contact with the surface(s). {#inpmod_b_elastic_description}

The lines below, 'Number of contact points...', 'Type and location of contact point...' and 'Specification of lines to be checked...', must be given in one block for each elastic contact surface. 




##### Number of contact points along the current contact surface and number of lines which may experience contact with the surface, one input line. {#inpmod_b_elastic_number}

~~~
NCNODE NCLINE
~~~

- `NCNODE: integer > 0`: Number of contact points located on the present contact surface
- `NCLINE: integer > 0`: Number of lines to be checked against contact with the present surface




##### Type and location of contact point, NCNODE input lines {#inpmod_b_elastic_type}

~~~
ICNOD LINE-ID ISEG IEND CNTTY TENTY TUBTY
~~~

- `ICNOD: integer`: Contact point number
- `LINE-ID: character(8)`: Reference to line identifier
- `ISEG: integer`: Local segment number
- `IEND: integer`: Local segment end (1 or 2)
- `CNTTY: character(8)`: Reference to roller contact type identifier (`CMPTYP-ID`)
- `TENTY: character(8), default: 'NONE'`: Reference to tensioner contact type identifier (`CMPTYP-ID`)
- `TUBTY: character(8), default: 'NONE'`: Reference to tubular contact identifier (`CMPTYP-ID`)

1< `ICNOD` < `NCNODE`; icnod must be given in increasing order. The line number (`ILIN`)
refers to the line number given implicit in the riser specification.

Note that:
- `CNTTY`, `TENTY` and `TUBTY` refers to `CMPTYP-ID`: New component specification.
- `CNTTY = 'NONE'` or `'0'` means no roller contact at the actual contact point.
- `TENTY = 'NONE'` or `'0'` means no tensioner at the actual contact point.
- `TUBTY = 'NONE'` or `'0'` means no tubular contact at the actual contact point.

Roller and tubular contact are activated by the `'ROLL'` command in the incremental static
loading procedure. Tensioner type of contact is activated by the `'TENS'` command.




##### Specification of lines to be checked for contact with the current contact surface, NCLINE input lines. {#inpmod_b_elastic_specification_of_lines}

~~~
LINCHK ISEGF IELF ISEGL IELL
~~~

- `LINCHK: character(8)`: Reference to line identifier (LINE-ID) to be checked for contact with the current contact surface.
- `ISEGF: integer, default: 1`: First local segment within the line to be checked for contact.
- `IELF: integer, default: 1`: First local element within the segment to be checked for contact.
- `ISEGL: integer, default: 0`: Last local segment within the line to be checked for contact.
- `IELL: integer, default: 0`: Last local element within the segment to be checked for contact.

`IELL = 0` means that the last element which will checked for contact is the last element within the segment `ISEGL`.

`ISEGL = 0` means that the last segment which will be checked for contact is the last
segment within line `ILCHCK`.




###  Pipe-in-pipe contact {#inpmod_b_pipe_pipe-in-pipe_contact}

This data group is optional and is available for Arbitrary Systems
only.

It enables the user to model pipe-in-pipe contact effects where each
of the pipes is defined as a single line or as a main riser line. For
normal riser systems this data group is normally not necessary.

A pipe-in-pipe pair consists of a master pipe and a slave pipe.  Both
the master and the slave pipe may consist of beam or bar types of
elements and must be of cross section types CRS0, CRS1 or CRS3.  The
contact between the master pipe and the slave pipe will be applied
between a node on the master pipe and an element in the slave
pipe. This results in nodal loads along the master pipe and discrete
element loads along the slave pipe. The discretization of the master
pipe must therefore be fine enough to model the contact. 

In the following the input parameters are described. A maximum of 400
pipe-in-pipe specifications may be given. The input lines in this group
must be given in one block for each pipe-in-pipe pair.

See also @ref faq_modelling_pip


#### Data group identifier, one input line {#inpmod_b_pipe_data}

~~~
PIPE IN PIPE
~~~


#### Pipe-in-pipe identifier, one input line {#inpmod_b_pipe_pipe-in-pipe_identifier}

~~~
IDPIPE CHLOAD
~~~

- `IDPIPE: character(16)`: Pipe-in-pipe identifier
- `CHLOAD: character(4), default: EXPO`: Fluid loading on inner pipe
    - `= 'EXPO'`: Exposed. The inner pipe is exposed to external
environmental loading; buoyancy and wave kinematics.
    - `= 'SHCL'`: Sheltered closed. The inner pipe is sheltered from
external loading, but subjected to fluid loads from the inner
fluid. The velocity and acceleration of the inner fluid follows the
local transverse motion of the outer pipe. The inner fluid does not 
extend above the mean water level.


Note that:
- If `CHLOAD = SHCL`, the master and slave pipes may not share supernodes. 



#### Specification of master pipe, one input line {#inpmod_b_pipe_specification_of_master}



###### For master pipe defined by a single line
~~~
CHMAST LINE-ID ISEGF_M ISEGL_M
~~~

- `CHMAST : character(4)`:  `= LINE`
- `LINE-ID: character(8)`: Reference to line identifier
- `ISEGF_M: integer, default: 1`: First local segment in line for master pipe
- `ISEGL_M: integer, default: NSEG`: Last local segment in line for master pipe



###### For master pipe defined by a main riser line
~~~
CHMAST = MRL  MRL-ID
~~~

- `CHMAST: character(4)`: `= MRL `
- `MRL-ID: character(8)`: Reference to main riser line identifier






#### Specification of slave pipe, one input line {#inpmod_b_pipe_specification_of_slave}



###### For slave pipe defined by a single line
~~~
CHSLAV = LINE  LINE-ID ISEGF_S ISEGL_S
~~~

- `CHSLAV : character(4)`: ` = LINE`
- `LINE-ID: character(8)`: Reference to line identifier
- `ISEGF_S: integer, default: 1`: First local segment in line for slave pipe
- `ISEGL_S: integer, default: NSEG`: Last local segment in line for slave pipe

Note that the slave pipe may not contain connectors.



###### For slave pipe defined by a main riser line
~~~
CHSLAV = MRL  MRL-ID
~~~

- `CHMAST: character(4)`: `= MRL `
- `MRL-ID: character(8)`: Reference to main riser line identifier

Note that the slave pipe may not contain connectors.



#### Specification of contact force characteristics, one input line {#inpmod_b_pipe_spesification_of_contact}

~~~
CHPOS IKS RELDAM DAMP STIFFR FRICST FRICDY CHAXI CHROT VELLIM
~~~

- `CHPOS: character`: Position of master pipe
    - `= INNER`
    - `= OUTER`
- `IKS: integer`: Stiffness code for radial contact force
    - `= 1`: Constant contact compression stiffness
    - `= N`: Table with N pairs of contact force - displacement to be
      specified
- `RELDAM: real`: Desired relative damping level at estimated eigen
    period in pipe, pipe and contact spring system (see below) $\mathrm{[1\]}$. Damping is only applied in the radial
    direction. Not used in static analysis. 
- `DAMP: real`: Dash pot damping coefficient per unit length of master
  pipe $\mathrm{[FT/L^2\]}$. Damping is only applied
  in the radial direction. Not used in static analysis. 
- `STIFFR: real`: Spring stiffness associated with the static friction
  coefficient `FRICST`, $\mathrm{[F/L^2\]}$. The
  spring stiffness is applied in the ring and axial directions until
  the spring force exceeds the static friction force. Not used in
  static analysis. Dummy if `CHAXI = OFF`.
- `FRICST: real`: Static friction coefficient $\mathrm{[1\]}$. Not
used in static analysis. Dummy if `CHAXI = OFF`.
- `FRICDY: real`: Dynamic sliding friction coefficient $\mathrm{[1\]}$. `FRICDY <= FRICST`. Not used in static
  analysis. Dummy if `CHAXI = OFF`.
- `CHAXI: character`: Control parameter for friction caused by 
  translational displacements. Not used in static analysis. 
    - `= ON`
    - `= OFF`
- `CHROT: character`: Control parameter for friction caused by
  rotation. Not used in static analysis.
    - `= ON`. Requires `CHAXI = ON`
    - `= OFF`
- `VELLIM: real`: Velocity limit for determining that sliding has
  stopped $\mathrm{[L/T\]}$. If the relative sliding velocity
  between the pipes falls below `VELLIM`, the spring stiffness `STFFR`
  is applied.  Should be small, but not zero. Not used in static
  analysis. Dummy if `CHAXI = OFF`.



Based on specified damping level the stiffness proportional damping
coefficient is calculated by

$a_2=2\times \mathrm{RELDAM}\times \sqrt{\frac{\mathrm{AMS_M+AMS_S}}{\mathrm{STIFF}}}$

where $\mathrm{AMS_M}$ and $\mathrm{AMS_S}$ are structural mass per unit length of the master pipe 
and the slave pipe respectively and $\mathrm{STIFF}$ is contact spring stiffness per unit length.




##### Contact spring stiffness; IKS = 1, one input line {#inpmod_b_pipe_contact_iks_is_1}

~~~
STIFF
~~~

- `STIFF: real`: Spring compression stiffness per unit length $\mathrm{[F/L^2\]}$




##### Contact spring stiffness; IKS > 1, one input line {#inpmod_b_pipe_contact_iks_is_more_than_1}

~~~
FS(1) ZS(1) ........ FS(N) ZS(N)
~~~

- `FS(1): real`: Contact force per unit length corresponding to
  the gap `ZS(1)` $\mathrm{[F/L\]}$. A negative value is a force 
  apposing penetration.
- `ZS(1): real`: Gap between the pipes $\mathrm{[L\]}$, A negative
  values indicates contact. 

`ZS(i)` must be given in increasing order

All `FS` and `ZS` values should be negative, as the `ZS` values are 
understood to be the gap between the two pipes. If no negative values are
given, linear extrapolation will be done from the two smallest `ZS` 
values.

Please note that the sign convention of this input is planned changed
in future versions!



###  Winch specification {#inpmod_b_winch_winch_specification}
This data group is optional and is available as additional information for Arbitrary Systems only.

It enables the user to model winch / winching. Boundary conditions previously defined for nodes attached
to the winch will be substituted by the winch specification. For normal riser systems this data group should not be considered.

In the following the input parameters are described. Several winches may be specified. The lines in this group must be given in one block for each winch.




#### Data group identifier, one input line {#inpmod_b_winch_data}

~~~
WINCh SPECification
~~~




#### Specification of winch(es), one input line {#inpmod_b_winch_specification}

~~~
NWINCH
~~~

- `NWINCH: integer`: Number of winches




##### Winch identifier, one input line {#inpmod_b_winch_winch_identifier}

~~~
IDWINCH
~~~

- `IDWINCH: character(8)`: Winch identifier




##### Initial location of winch point, one input line {#inpmod_b_winch_initial}

~~~
ILIN_W ISEG_WP RLSEG_WP IEND_W
~~~

- `ILIN_W: integer`: Line number attached to winch
- `ISEG_WP: integer`: Local segment number at winch point
- `RSEG_WP: real`: Relative segment length where segment is attached to winch point
- `IEND_W: integer`: End of segment (and line) attached to winch (1 or 2)

figurwinch


##### Final position of winch point, one input line {#inpmod_b_winch_final}

~~~
XW YW ZW ROTW DIRW
~~~

- `XW: real`: Coordinates for static equilibrium position $\mathrm{[L\]}$
- `YW: real`: Coordinates for static equilibrium position $\mathrm{[L\]}$
- `ZW: real`: Coordinates for static equilibrium position $\mathrm{[L\]}$
- `ROTW: real`: Specified rotation of supernode from stress free position to static equilibrium position $\mathrm{[deg\]}$
- `DIRW: real`: Direction of axis for specified rotation $\mathrm{[deg\]}$




##### Boundary condition of winch, one input line {#inpmod_b_winch_boundary}

~~~
CBOUND CIBODY
~~~


- `CBOUND: character(6)`:  Boundary condition for winch (All nodes attached to winch)
    - `= FIXED`: Fixed boundaries
    - `= VESSEL`: Winch attached to support vessel
    - `= FLOATE`: Winch attached to floater force model ('SIMO' body)
- `CIBODY`
    - ` = IVES: integer`: Support vessel number (`CBOUND = VESSEL`)
    - ` = CHBODY: character(8)`: Floater force model identifier (`CBOUND = FLOATE`)
    - (Dummy for `CBOUND=FIXED`)




##### Winch properties, one input line {#inpmod_b_winch_winch_properities}

~~~
VELMAX TIMMAX LDROP RADIUS IZSIGN LELVAR
~~~


- `VELMAX: real`: Maximum winch velocity $\mathrm{[L/T\]}$
- `TIMMAX: real`: Time to reach maximum velocity (from zero) $\mathrm{[T\]}$
- `LDROP: integer`: Line release when no more line on winch (Dynamic analysis)
    - = 0 Not possible
    - = 1 Possible
- `RADIUS: real > 0`: Radius of winch $\mathrm{[L\]}$
- `IZSIGN: integer`: = $\mathrm{\pm1}$  Center of winch in positive or negative local Z-axis
- `LELVAR: integer`: Control parameter for adjusting the length of elements attached to winch.
    - = 0 No justification
    - = 1 Justification

The parameters `RADIUS`, `IZSIGN` and `LELVAR` specify how the elements attached to the winch are visualized.

For `LELVAR=0`: $\mathrm{RADIUS>=(EL)/\sqrt{2}}$, where $\mathrm{EL}$ is length of shortest element attached to the winch.

Note that Final position for winch is dummy for coupled analysis. 

The RIFLEX winch formulation is intended for vertical winching and may be unstable when deviating from vertical in dynamic analysis. 

It is recommended to apply some numerical damping when using the winch functionality, for example `BETIN = 3.9`and `GAMMA = 0.505`, see @ref dynmod_e_method.

The Winch rotations follow the same conventions as prescribed rotations of nodes, see @ref inpmod_b_arbitrary_boundary_conditions. The coordinate system is rotated first using `DIRW`, 
followed by `ROTW`. For example: if Rotation direction `DIRW` is set to `0.0`, the winch will rotate `ROTW` degrees around the local y-axis. It is important to note that
the coordinate system is rotated first relative to the global system using `DIRW`, the winch is then rotated `ROTW` degrees around the y-axis in the updated coordinate system. 

![Sketch of a winch model](@ref figures/um_ii_fig47_winch.svg)
@image latex figures/um_ii_fig47_winch.pdf "Sketch of a winch model" width=12cm


###  Wind turbine specification {#inpmod_b_wind_wind_turbine_specification}

This data group is optional and is only available for Arbitrary
Systems. It enables the user to model wind turbines considering wind
load acting on the blades and control system for blade pitch and
electrical power extraction. For normal riser systems this data group
should not be considered.

The wind turbine is modelled by a group of lines that constitute the blades and the shaft,
see figure 'Outline of a wind turbine model' below.
In addition, references to the air foil library file and to control data for electrical torque and blade pitch must be given.

A shared supernode at the hub connects the blades and the shaft. Each blade must consist of two lines. The
inner line represents eccentricity and the outer line the actual foil blade. A rigid supernode connection is used 
to represent connection between the two lines. The constant term, c0, in the linear constraint equation is subsequently used for blade pitch control.

The wind turbine blades have to be identical with regard to the element distribution, foil profile description and aerodynamic
coefficients along the blades. The mass and stiffness distribution may be different.

The wind loads on the blades are computed based on the load coefficient description in the air foil library
file and together with a blade element momentum (BEM) method. The applied BEM code includes dynamic inflow, 
i.e. a time delay on changes of induced velocity related to the time it takes to convect vorticity in the wake downstream, 
away from the rotor. With dynamic inflow, the BEM method will give correct time series of rotor and blade loads under conditions of changing blade
pitch angle, wind speed and direction, and tower motion. The main features of the BEM theory are:

- Induced velocity is calculated assuming momentum balance for a ring-shaped control volume.
- Blade sections are treated as independent.
- Aerodynamic coefficients from wind tunnel tests are used for the blades.
- Empirical corrections are used for tip-vortices and cascade effects / lift amplification.

The BEM theory is a proven, simple and CPU efficient method to simulate rotor aerodynamics and the method
represents the industry standard. Additional information regarding the coordinate systems for the wind turbine results can be found in [Wind Turbine Results](@ref wind_turbine_results). 

![Outline of a wind turbine model](@ref figures/um_ii_fig48.svg)
@image latex figures/um_ii_fig48.pdf "Outline of a wind turbine model" width=12cm




#### Data group identifier, one input line {#inpmod_b_wind_data1}

~~~
WIND TURBine SPECification
~~~




#### Specification of windturbine(s), one input line {#inpmod_b_wind_data2}

~~~
NWITURB
~~~

- `NWITURB: integer`: Number of wind turbines to be specified

In present version of RIFLEX only one wind turbine may be modelled.




#### Component type identifier {#inpmod_b_wind_component}

~~~
FILE_NAME
~~~

- `FILE_NAME: character`: Name of the airfoil coefficient library
    - `= 'NONE'`: No file

The next input lines are given in one block for each wind turbine.




#### Wind turbine identifier, one input line {#inpmod_b_wind_wind_turbine_identifier}

~~~
WIND-TURBINE-ID
~~~

- `WIND-TURBINE-ID: character(8)`: Wind turbine identifier. The value 'NONE' is not allowed.




#### Wind references for wind velocity, one input line {#inpmod_b_wind_wind_references}

~~~
WIND_REF AERO_DLL
~~~

- `WIND_REF: character`: Coupled analysis: Reference to floater force model (`SIMO` body) for wind
velocity. Must be given for coupled analysis, dummy if not coupled analysis. 
- `AERO_DLL: character, default: 'NONE'`: Code for AERODYN DLL (Educational feature)
    - `AERO_DLL = NONE` : Official RIFLEX version
    - `AERO_DLL = EXTE` : Restricted option only available for selected academic users


For coupled analyses with `SIMO` wind type `IWITYP >= 10`, the
incoming wind is calculated at the updated nodal coordinates of the
nodes along the blades.

For coupled analyses with `SIMO` wind type `IWITYP < 10`, the wind at
the `SIMO` body `WIND_REF` is reported. Note that this wind is
calculated at the wind force coefficient height `ZCOEFF`. This wind is
also used as the incoming wind along the blades .



#### Wind load options, one input line {#inpmod_b_wind_wind_load}

~~~
CLMOM    CUPWN   IWTADV
~~~

- `CLMOM: character, default: 'ON'`: ON-OFF switch for inclusion of wind moment around longitudinal axis of the blades.
    - `CLMOM = ON`: Include wind moment
    - `CLMOM = OFF`: Exclude wind moment and disregard distance between foil center and pitch axis
- `CUPWN: character, default: 'UPWN'`: switch for upwind or downwind turbine
    - `CUPWN = UPWN`: Upwind turbine
    - `CUPWN = DNWN`: Downwind turbine
- `IWTADV: integer, default: 0`: switch for advanced wind turbine aerodynamic options
    - `IWTADV = 0`: Default wind turbine aerodynamic options
    - `IWTADV = N`: Number of lines with advanced wind turbine aerodynamic options 
	

#### Advanced wind turbine aerodynamic load options, IWTADV>0, IWTADV input lines {#inpmod_b_wind_wind_adv_load}

~~~
CHID    CHSW
~~~

- `CHID: character(4)` : identifier for switch to be given

- `CHSW: character(3)` : on-off switch

Legal combinations of `CHID` and `CHSW` include:

- `CHID == INDU`: induction calculation
	- `CHSW = OFF`: No induction calculation (parked turbine)
    - `CHSW = ON`: Induction calculation included (default)

- `CHID == PRTI`: Prandtl tip correction
	- `CHSW = OFF`: No Prandtl correction applied at the blade tip
    - `CHSW = ON`: Prandtl correction applied at the blade tip (default)

- `CHID == PRRO`: Prandtl root correction
	- `CHSW = OFF`: No Prandtl correction applied at the blade root (default)
    - `CHSW = ON`: Prandtl correction applied at the blade root 

- `CHID == PRYA`: Prandtl factor correction for yaw
	- `CHSW = OFF`: Keep angle $\mathrm{\phi }$ constant regardless of yawed inflow
    - `CHSW = ON`: Correct angle $\mathrm{\phi }$ in the Prandtl factor for yawed inflow (default)	
	



#### Specification of internal or external control system for blade pitch, electrical power and nacelle yaw, one input line {#inpmod_b_wind_specification_of_internal}

Specification of internal or external blade pitch and electrical power control system, [internal] (@ref inpmod_b_wind_specification_internal) and [external](@ref inpmod_b_wind_specification_external). 
Specification of internal or external nacelle yaw controller, [Nacelle yaw controller](@ref inpmod_b_wind_specification_int_ext_yaw).

~~~
CHCODE  YAWCCODE
~~~

- `CHCODE: character(4)`: 
    - `CHCODE = INTC`: Internal control system
    - `CHCODE = EXTC`: External control system
- `YAWCCODE:  character(4)`, default: `NONE`: Control system used for yaw
    - `YAWCCODE = NONE`: No yaw control system
    - `YAWCCODE = YCIN`: Internal yaw control system
    - `YAWCCODE = YCEX`: External yaw control system  (not implemented)



##### Internal control system input for blade pitch and electrical power, CHCODE = INTC, one input line {#inpmod_b_wind_specification_internal}

~~~
FILE_NAME
~~~

Descriptions of the internal control system and file format are found
in 
[Specification of internal control system for blade pitch and electrical power](@ref inpmod_aif_specification).




##### External control system input for blade pitch and electrical power, CHCODE = EXTC, 3 input lines {#inpmod_b_wind_specification_external}

~~~
JarName
~~~

~~~
ClassName
~~~

~~~
Config
~~~

Additional information about the interface for the external control
system is given in 
[Interface for external wind turbine control system](@ref inpmod_extWTcontrol_specification).



##### Specification of nodes and elements  for additional measurements, CHCODE = EXTC  {#inpmod_b_wind_specification_nodes_elemen}

~~~
NNOD_MEAS  NEL_MEAS
~~~

- `NNOD_MEAS: integer, default: 0`: Number of nodes for which additional measurements will be sent to the external control system. `NNOD_MEAS = 0` for the internal control system.
- `NEL_MEAS: integer, default: 0`: Number of elements for which additional measurements will be sent to the external control system. `NEL_MEAS = 0` for the internal control system.



###### Specification of nodes for additional measurements, NNOD_MEAS input lines  {#inpmod_b_wind_specification_nnod_meas}

~~~
LINE-ID ISEG INOD SYSTEM
~~~

- `LINE-ID: character(8)`: Line identifier
- `ISEG: integer > 0`: Local segment number in specified line
- `INOD: integer > 0`: Local node number in specified segment
- `SYSTEM: character(6), default: 'GLOBAL'`: switch for reference system for the nodal measurements exported to the external controller.
    - `SYSTEM = GLOBAL`: Displacement, velocity and acceleration in the global coordinate system 
    - `SYSTEM = SHAFT0`: Displacement, velocity and acceleration in the initial shaft system


###### Specification of elements for additional measurements, NEL_MEAS input lines {#inpmod_b_wind_specification_nel_meas}

~~~
LINE-ID ISEG IEL SYSTEM
~~~

- `LINE-ID: character(8)`: Line identifier
- `ISEG: integer > 0`: Local segment number in specified line
- `IEL: integer > 0`: Local node number in specified segment
- `SYSTEM: character(6), default: 'LOCAL'`: switch for reference system for the element measurements exported to the external controller.
    - `SYSTEM = LOCAL`: Element forces and moments in the local element system




#### Shaft and tower specification, one input line {#inpmod_b_wind_shaft}

~~~
LINE-IDSFT LINE-IDTWR  BAK  ICDCOR
~~~

- `LINE-IDSFT: character(8)`: Reference to the line that is used for shaft modelling.
- `LINE-IDTWR: character(8), default: 'NONE'`: Reference to the line that is used for tower modelling.
    - If specified the incoming wind acting on the blades will be modified
    due to the presence of the tower.
- `BAK: real, default: 0`: Bak modification factor for tower shadow. May be applied to up- or down-wind turbines.
- `ICDCOR: integer, default: 0`: Option for modification of the tower shadow based on the tower drag. 
May be applied to up- or down-wind turbines.

One and only one flex-joint has to be specified within the shaft line
(line type). The flex-joint has to be fixed in the bending degrees of
freedom and be given a specified stiffness in the torsional degree of
freedom.  The specified torsion stiffness will be used during static
analysis. During dynamic analysis, the torsion will be controlled be
the regulator.




#### Number of blades in the rotor, one input line {#inpmod_b_wind_number}

~~~
NBLADE
~~~

- `NBLADE: integer`: Number of blades




#### Blade identification, NBLADE input lines {#inpmod_b_wind_blade}

~~~
LINE1-ID LINE2-ID
~~~

- `LINE1-ID: character(8)`: Reference to the inner line of the blade (eccentricity).
- `LINE2-ID: character(8)`: Reference to the outer line of the blade (foils).

The supernode at the eccentricity has to be master node and the supernode at the blade the slave
node in the the rigid supernode connection between the eccentricity and the blade.


#### Specification of internal or external control system for nacelle yaw, one input line {#inpmod_b_wind_specification_int_ext_yaw}



##### Internal yaw control system input, YAWCCODE=YCIN, 1 input lines {#inpmod_b_wind_specification_yaw_int}

~~~
FILE_NAME
~~~

Descriptions of the internal yaw control system and file format are found 
in ....



##### External yaw control system input, YAWCCODE=YCEX, 3 input lines 

~~~
JarName
~~~

~~~
ClassName
~~~

~~~
Config
~~~



##### Yaw element identification, YAWCCODE=YCEX or YAWCCODE=YCIN, 1 input line  {#inpmod_b_wind_specification_yaw_ext}

~~~
REFLINE-ID YAWLINE-ID
~~~
- `REFLINE-ID: character(8)`: Reference to the line that connected to the yaw element.
- `YAWLINE-ID: character(8)`: Reference to the yaw element.


###  Airfoil coefficient library specification {#inpmod_b_airfoil_coeff_lib}

This data group is optional and is only available for Arbitrary Systems. Only one airfoil coefficient library may be specified. This data group is not permitted for systems which include a wind turbine specification. 

The airfoil lift, drag, and moment coefficients on elements that are not part of a wind turbine are applied via lookup table (no induction). 



#### Data group identifier, one input line {#inpmod_b_data_airfoil_coeff_lib}

~~~
AIRFoil COEFficient LIBRary
~~~


#### File name specification, one input line {#inpmod_b_file_airfoil_coeff_lib}

~~~
FILE_NAME
~~~

- `FILE_NAME: character(256)`: Path to the airfoil coefficient library


###  Potential flow library specification {#inpmod_b_poten_lib}

This functionality is currently under testing.

This data group is optional. Only one potential flow library may be specified. 

For cross-sections with POTN loading, this file provides the frequency-dependent 
radiation and diffraction data. If cross-sections with POTN loading are used in the 
analysis, this input is required (checked in stamod). 


#### Data group identifier, one input line {#inpmod_b_data_poten_lib}

~~~
POTEntial FLOW LIBRary
~~~


#### File name specification, one input line {#inpmod_b_file_poten_lib}

~~~
FILE_NAME
~~~

- `FILE_NAME: character(256)`: Path to the potential flow library


#### Connection between FE-elements and data in the pontential flow library


##### Number of elements with POTN loading, one input line {#inpmod_b_nopotelem}


Note that the number of elements with POTN loading and wich are located below
sea level has to be equal to the number of sections in the potential flow
library!


~~~
NOPOTELEM
~~~

- `NOPOTELEM: integer`: Number of elements with POTN loading



##### Connections between elements and sections in the potential flow library, NOPOTELEM input lines {#inpmod_b_elemrel_potflow}

Note that the sequence of element specifications  has to coincide with the sequence of sections in the library.

~~~
LINE-ID ISEG IEL
~~~

- `LINE-ID: character(8)`: Line identifier
- `ISEG: integer`: Local segment number within the line `LINE-ID`
- `IEL: integer`: Local element number within the segment `ISEG`








###  Main riser line specification {#inpmod_b_main_main_riser_line_specification}




#### Data group identifier, one input line {#inpmod_b_main_data}

The main riser line (MRL) may be used to define continuous contents of several lines.

This data group may be given for AR-systems only. Only one riser system may be defined on
the INPMOD input file.


~~~
MAIN RISEr LINE
~~~




##### Main riser line definition, one input line {#inpmod_b_main_main_riser_line_definition}

~~~
MRL-ID LINE-ID1 ... LINE-IDn
~~~

- `MRL-ID: character(8)`: Main riser line identifier
- `LINE-ID1: character(8)`: Reference to line identifier
    - `LINE-ID1` = First line in MRL
    - By default the MRL is defined from end 1 to end 2 of this line
    - If the line ID is given subsequent to a minus sign, `-LINE-ID1`, the MRL is defined from end 2 to end 1 of this line
- ...
- `LINE-IDn: integer`:

A MRL may consist of up to 200 lines.
A maximum of 5 MRLs may be defined.




##### Main riser line flow, one input line {#inpmod_b_main_main_riser_line_flow}

~~~
RHOI IEND PRESSI DPRESS VVELI
~~~

- `RHOI: real, default: 0`: Density of contents $\mathrm{[M/L^3\]}$
- `IEND: integer`:
    - `IEND=1`: Pressure specified at end 1
    - `IEND=2`: Pressure specified at end 2
- `PRESSI: real, default: 0`: Pressure at end `IEND` $\mathrm{[F/L^2\]}$
- `DPRESS: real, default: 0`: Pressure drop $\mathrm{[F/L^3\]}$
- `VVELI: real, default: 0`: Fluid velocity $\mathrm{[L^3/T\]}$
    - Dummy in present version

The pressure drop is assumed to be uniform over the line length starting at end `IEND`.
The values given here will replace values given in the `FLUID` specification.

An illustration is shown the figure 'Main riser line concept' below with corresponding input data.

\anchor Main_riser_line_concept
![Main riser line concept](@ref figures/um_MRL_definition.png)
@image latex figures/um_MRL_definition.pdf "Main riser line concept" width=16cm

\latexonly
%### Main riser line input {#inpmod_mrl_example}

Input using the main riser line concept is shown below.

\begin{lstlisting}[language=riflex, numbers=none, frame=LTRB,frameround=tttt,framesep=4pt,
                                    xleftmargin=0cm,  xrightmargin=0cm,
                                    caption={Main riser line concept}]
'**********************************************************************
 ARBITRARY SYSTEM AR
'**********************************************************************
'nsnod nlin nsnfix nves nricon nspr nakc 
 3     2    3      0    0      0    0    
'ibtang zbot             ibot3d 
 0      -1.000000000e+03 0      
'B 6.5: LINE TOPOLOGY DEFINITION
'lineid lintyp-id snod1-id snod2-id 
 line1  ltyp1     node1    node2    
 line2  ltyp1     node3    node2    
'FIXED NODES
'
..
.
...
.
'**********************************************************************
 MAIN RISER LINE
'**********************************************************************
'IMRL LINE-ID(i)
 MRL1 line1 -line2
'rhoi            iend pressi          dpress          
 5.000000000e-01 1    1.000000000e+03 0.000000000e+00 
'**********************************************************************
 NEW COMPONENT CRS0
'**********************************************************************
.
..
...

\end{lstlisting}
\endlatexonly
 




### Geotechnical spring specification {#inpmod_b_geotechnical_geotechnical}

Additional to the Arbitrary system data group.

This data group is used to specify geotechnical springs in the global
X-Y plane suitable for modeling cyclic geotechnical data with
degradation. The stiffness of the spring is degraded based on the
secant stiffness to ultimate resultant displacement from initial
position.

The applied damping calculates damping force based on the following
model

$\mathrm{F=C(d)\times |\dot {d}|^P\times sign(\dot {d})}$

where
- $\mathrm{F}$: damping force
- $\mathrm{C}$: damping coefficient (strain / displacement dependent)
- $\mathrm{d}$: spring displacement
- $\mathrm{\dot {d}}$: velocity of attached node
- $\mathrm{P}$: exponent for strain velocity (P >= 1)

Note that the degradation of the geotechnical spring will dissipate
some energy in the cycles where the spring is updated.




#### Data group identifier, one input line {#inpmod_b_geotechnical_data}

~~~
GEO SPRINg SPECification
~~~




#### Number of geotechnical springs, one input line {#inpmod_b_geotechnical_number}

~~~
NGEOSPR
~~~

- `NGEOSPR: integer > 0`: Number of geotechnical springs


The following input lines are repeared `NGEOSPR` times.



#### Spring ID  {#inpmod_b_geotechnical_spring_id}

~~~
SPRING-ID
~~~

- `SPRING-ID: character(8)`: Spring ID. Must be unique.



#### Spring localization and properties {#inpmod_b_geotechnical_spring}

4 or 5 input lines, depending on the damping model selected,

~~~
LINE-ID ISEG INOD
~~~

- `LINE-ID: character(8)`: Line identifier 
- `ISEG: integer`: Local segment number within line
- `INOD: integer`: Local node number within segment


~~~
RLEN
~~~

- `RLEN: real, default: 0`: Relative length, for scaling of results only


~~~
FORCE1 DISP1 .... FORCEn DISPn
~~~

- `FORCE1: real`: Force corresponding to DISP1. First value must be zwero. $[\mathrm{F}\]$ 
- `DISP1: real`: Displacement correcponding to FORCE1. First value must be zwero.  $[\mathrm{L}\]$ 
- `FORCEi: real > 0`: Force corresponding to DISPi. $[\mathrm{F}\]$ 
- `DISPi: real > DISP_i-1`: Displacement correcponding to FORCEi. $[\mathrm{L}\]$ 

~~~
IDMP EXPDMP
~~~

- `IDMP: integer >= 0`: Damping coefficient code
    - `= 1`: Constant damping coefficient
    - `= N`: Table with N pairs of damping coefficient / Displacement to be specified.
- `EXPDMP: real >= 0`: Exponent for displacement velocity (Z = 1). Dummy if IDMP = 0.


No more input in this data group if `IDMP = 0`


1 line of input if `IDSP = 1`:

~~~
DAMPGEO
~~~

- `DMPGEO: real > 0`: Displacement independent damping coefficient


1 line of input with IDMP pairs of damping values if `IDMP > 1`:

~~~
DAMPGEO1 DISP1 ... DAMPGEOidmp DISPidmp
~~~

- `DMPGEO1: real`: Damping coefficient corresponding to DISPL1
- `DISPL1: real`: Displacement corresponding to damping coefficient DMPGEO1. $[\mathrm{L}\]$ 
- `DMPGEOi: real`: Damping coefficient corresponding to DISPLi
- `DISPLi: real`: Displacement corresponding to damping coefficient DMPGEOi. $[\mathrm{L}\]$ 


![Spring degradation model](@ref figures/um_ii_fig49.png)
@image latex figures/um_ii_fig49.pdf "Spring degradation model" width=12cm

The figure shows the initial stiffness $\mathrm{K_i}$ and updated secant stiffness $\mathrm{K_s}$ 
after displacement $\mathrm{d_u}$ in Geotechnical spring.




###  Line and segment specification {#inpmod_b_line_line_and_segment}




#### Data group identifier, one input line {#inpmod_b_line_data}

Lines which represent stress joints are specified in data group [Stress joint line specification](@ref inpmod_b_stress_joint_line).

The total number of line types and stress joints has to be less or
equal to 500 in the present version.


~~~
NEW LINE DATA
~~~



#### Line type specification, one input line {#inpmod_b_line_line_type}

~~~
LINTYP-ID NSEG NCMPTY2 FLUTYP IADDTWI IADDBEND
~~~

- `LINTYP-ID: character(8)`: Line type identifier.
- `NSEG: integer`: The number of segments the line type consists of.
- `NCMPTY2: character/integer, default: 0`: Reference to nodal component type, `CMPTYP-ID`, attached to end 2 of segment `NSEG`.
    - Must be type `BODY`, `CONB`, `FLEX` or `DRAG`.
    - `NCMPTY = 'NONE'` or `'0'` means that no nodal component is attached at end 2 of segment NSEG.
- `FLUTYP: character/integer, default: 0`: Reference to internal fluid component type identifier. Must be of type `FLUID`.
    - `FLUTYP = 'NONE'` or `'0'` means no fluid in the line.
- `IADDTWI: integer, default: 0`: Indicator for twist information (Relative rotation around the line type length axis).
    - `IADDTWI = 0`: No extra specification to be given.
    - `IADDTWI = 1`: Extra specification to be given.
- `IADDBEND: integer, default: 0`: Indicator for pre-curved line type, i.e. offsets transverse to the straight line between the line ends.
    - `IADDBEND = 0`: No extra specification to be given.
    - `IADDBEND = 1`: Extra specification to be given at the second end of all but the last segment within the line type
    - `IADDBEND = 2`: Extra specification to be given at the second end of all segments




#### Segment specification. NSEG input lines. {#inpmod_b_line_segment}

~~~
CRSTYP NCMPTY1 EXWTYP NELSEG SLGTH NSTRPS NSTRPD SLGTH0 SOITYP
~~~

                    
- `CRSTYP: character`: Reference to cross-sectional component type identifier `CMPTYP-ID`
    - Must be of type `CRS0` ... `CRS7` or `FIBR`
- `NCMPTY1: character/integer, default: 0`: Reference to nodal component type identifier, `CMPTYP-ID`, attached to end 1 of segment.
    - Must be type `BODY`, `CONB`, `FLEX` or `DRAG`.
    - `NCMPTY1 = 'NONE'` or `'0'` means that no nodal component is attached at end 1 of segment.
- `EXWTYP: character/integer`: Reference to external wrapping (distributed weight or buoyancy) component type identifier `CMPTYP-ID`. 
    - Must be of type `EXT1`.
    - `EXWTYP = 'NONE'` or `'0'` means no external wrapping.
- `NELSEG: integer`: Number of elements for FEM analysis
- `SLGTH: real > 0`: Segment length $\mathrm{[L\]}$
- `NSTRPS: integer, default: 3`: Number of sections each element is divided into for hydro-dynamic calculation; static analysis.
- `NSTRPD: integer, default: 5`: Number of sections each element is divided into for hydro-dynamic load calculation; dynamic analysis.
- `SLGTH0: real, default: SLGTH`: Actual stress free segment length
- `SOITYP: character/integer, default: '0'`: Reference to seafloor contact component type identifier `CMPTYP-ID`.
    - Must be a `SEAF` component of type `CARI` (restricted option).
    - Only to be specified if `IBTANG = 2`
    - `SOITYP = 'NONE'` or `'0'` means that the segment has no seafloor contact.
    - Restricted option.

`NSTRPS` and `NSTRPD` are used only for cross-section types: `CRS3`, `CRS4`, `CRS5` and `CRS6`. Dummy for
`CRS0`, `CRS1`, `CRS2` and `CRS7`.

If the stress free length of the line (sum of the segment `SLGTH`) is not equal to the distance
between the stress free coordinates of the supernodes that the line is attached to, the stress free line length will be modified according to the following rules:

Length modification will always be done on the last segment within the line. Therefore the
first task is to check if it is possible to modify this segment to obtain a line length equal the to the distance. 
If this is not possible the program will terminate with error
message. Then the difference between the length and the distance is within the preset length tolerance:
- Difference larger than 1% gives error termination.
- Difference between 0.1% and 1% gives modification and written warning.
- Difference less than 0.1% gives modification but no warning.

Specifying `SLGTH0` $\mathrm{\neq }$ `SLGTH` enables the user to use initially stressed segments at the start of the static analysis. 
This feature is useful for modelling elastic springs between element nodes. `SLGTH`
will be interpreted as stressed segment length by the program.




#### Relative twist specification {#inpmod_b_line_relative}

The following NSEG input lines is to be given if `IADDTWI = 1`.

~~~
TWEND1 TWEND2
~~~

- `TWEND1: real`: Relative twist segment end 1 $\mathrm{[deg\]}$
- `TWEND2: real, default: TWEND1`: Relative twist segment end 2 $\mathrm{[deg\]}$

The relative twist for elements within the segment is calculated by
use of linear interpolation. The twist angle is constant over the
element length.  The twist angle of the actual line will relate to the
line local Y-axis.

The local Y-axis may be set using the data group
[LOCAL ELEMENT AXIS](@ref inpmod_af_local),
be determined by shaft and blade orientation for a wind turbine blade
or the default procedure may be used. See
[Line, line type and supernode connectivity](@ref inpmod_b_arbitrary_line)
for details.




#### Transverse offset specification {#inpmod_b_line_transverse}

If `IADDBEND = 1` the following NSEG-1 input lines are to be given. Offsets at
the last node of the last segment are set to zero.

If `IADDBEND = 2` the following NSEG input lines are to be given. 

~~~
DY DZ
~~~

- `DY: real, default: 0`: Offset in line local Y-axis segment end 2 $\mathrm{[L\]}$
- `DZ: real, default: 0`: Offset in line local Z-axis segment end 2 $\mathrm{[L\]}$

This feature enables the user to model a curved stress-free 
configuration of a line type by specifying transverse offsets at
end 2 of all line segments, i.e. transverse offsets from the
straight line between the line ends. The offsets `DY` and `DZ`
refer to the initial local line Y and Z axes, disregarding any
specified relative twist.

**Note!** If only NSEG-1 input lines are given, the offsets are set to zero for the second end of the last segment.

Specified twist will be applied around the
updated local element X-axis after the offsets have been
accounted for.

The stressfree segment lengths `SLGTH` will be modified according to
the specified offsets. If a segment consist of more than one element,
the intermediate nodes will be placed along the straight line
between the segment nodes.

The cross-section properties will not be changed, e.g. the specified mass
per unit length will be used together with the modified segment length.

**Note!**
If non-zero offset is specified at the second end of the last segment, no
other line may be connected to this supernode

The local Y-axis may be set using the data group
[LOCAL ELEMENT AXIS](@ref inpmod_af_local),
be determined by shaft and blade orientation for a wind turbine blade
or the default procedure may be used. See
[Line, line type and supernode connectivity](@ref inpmod_b_arbitrary_line)
for details.




###  Stress joint line specification {#inpmod_b_stress_joint_line}




#### Data group identifier, one input line {#inpmod_b_stress_data}

The stress joint lines are labelled with an unique line type
identifier, `LINTYP-ID`. The total number of line types and stress
joints has to be less or equal to 500 in the present version.

~~~
STREss JOINt DATA
~~~




#### Stress joint specification, one input line {#inpmod_b_stress_stress_joint_specification}

~~~
LINTYP-ID CDSJ CMASJ NSJSEC FLUTYP
~~~

- `LINTYP-ID: character(8)`: Line type identifier
- `CDSJ: real`: Non-dimensional quadratic drag coefficient in normal direction
- `CMASJ: real`: Non-dimensional added mass coefficient in normal direction
- `NSJSEC: integer`: Number of conical sections in stress joint
- `FLUTYP: character/integer`: Reference to internal fluid component type identifier, `CMPTYP-ID`.
    - Must be of type `FLUID`.
    - `FLUTYP = 'NONE'` or `'0'` means no fluid in the line.




#### Initial cross-section parameters, one input line {#inpmod_b_stress_initial}

~~~
DESJS THSJS
~~~

- `DESJS: real`: External diameter at first end of first conical section in stress joint $\mathrm{[L\]}$
- `THSJS: real`: Wall thickness at first end of first conical section in stress joint $\mathrm{[L\]}$




#### Parameters to define the conical stress joint sections, NSJSEC input lines {#inpmod_b_stress_parameters}

~~~
NSJS DESJ THSJ SJSL NELSJ EMOD RHO
~~~

- `NSJS: integer`: Stress joint section number. To be given in increasing order starting with #1
- `DESJ: real`: External diameter at second end of the section $\mathrm{[L\]}$
- `THSJ: real`: Wall thickness at second end of the section $\mathrm{[L\]}$
- `SJSL: real`: Length of the section $\mathrm{[L\]}$
- `NELSJ: integer`: Number of segments within the section
- `EMOD: real`: Young's modulus of elasticity $\mathrm{[F/L^2\]}$
- `RHO: real`: Density of pipe material $\mathrm{[M/L^3\]}$

Each segment will consist of one element. `CRS0` cross-sections will be generated automatically
for each segment in the stress joint.

![Stress joint description](@ref figures/um_ii_fig50.svg)
@image latex figures/um_ii_fig50.pdf "Stress joint description" width=12cm




## Data Group C: Component Data {#inpmod_c_component_data_data_group_c}

This section includes specification of all elementary components to be
used for the riser modelling. It is possible to specify more components
than are actually used.

The components are labelled with an identifier called “component type
identifier: `CMPTYP-ID`. The maximum number of component types is 500 in
the present version.

For each component a list of data “attributes” have to be specified.
This list depends on the TYPE CODE given in the data group identifier.

The following component types are included:

- `CRS0`:      [Thin-walled pipe cross section](@ref inpmod_c_crs0 )
- `CRS1`:      [Axisymmetric cross section](@ref inpmod_c_crs1_crs1 )
- `CRS2`:      [Double symmetric cross section](@ref inpmod_c_crs2_cross_section )
- `BODY`:      [Body attached at one point. Mass point](@ref inpmod_c_body )
- `CONB`:      [Connector. Ball-joint type](@ref inpmod_c_CONB )
- `FLEX`:      [Flex joint (supressed translations)](@ref inpmod_c_FLEX )
- `FLUID`:     [Internal fluid flow](@ref inpmod_c_fluid )
- `EXT1`:      [External wrapping, rotation symmetry](@ref inpmod_c_ext1 )
- `CRS3`:      [Partly submerged axisymmetric cross section](@ref inpmod_c_crs3 )
- `CRS4`:      [Partly submerged double symmetric cross section](@ref inpmod_c_crs4 )
- `CRS5`:      [Partly submerged general shaped cross section](@ref inpmod_c_crs5 )
- `CONT`:      [Contact point of roller type](@ref inpmod_c_contact )
- `TENS`:      [Tensioner](@ref inpmod_c_tensioner )
- `TUBU`:      [Tubular contact point](@ref inpmod_c_tubular )
- `SEAF`:      [Seafloor contact](@ref inpmod_c_seafloor )
- `DRAG`:      [Drag chain element](@ref inpmod_c_drag )
- `FIBR`:      [Fibre rope cross section](@ref inpmod_c_fibre )
- `GROW`:      [Marine growth](@ref inpmod_c_growth )
- `CRS6`:      [Fish net cross section](@ref inpmod_af_fish )
- `CRS7`:      [General cross section](@ref inpmod_c_crs7_cross_section )

Practical aspects of modelling:

- Bending stiffeners are assumed to be modelled by one or more
segments with average mass, drag and stiffness properties from the
riser and bending stiffener within each segment.
- External buoyancy of weight elements that are clamped to the pipe
are specified as external wrapping.
- The mass of `EXT1` type component is added to the line properties.
Drag and mass coefficients are added to those of the line.
- Body and external wrapping can not be specified for segments
consisting of the cross section types: `CRS3`, `CRS4`, `CRS5`, or `CRS6`




###  CRS0 - Thin-walled pipe cross section {#inpmod_c_crs0}

This cross-section allows for simplified input of circular, homogenous
cross-sections. The input format is convenient for metallic pipe cross
sections.

\latexonly
%### Example input {#inpmod_c_crs0_example}

A thin-walled pipe cross section example is shown below.
Subsequent sections give details and further options.

\begin{lstlisting}[language=riflex, numbers=none, frame=LTRB,frameround=tttt,framesep=4pt,
                                    xleftmargin=0cm,  xrightmargin=0cm,
                                    caption={CRS0 - Thin-walled cross section.}]
'**********************************************************************
        NEW COMPONENT CRS0
'**********************************************************************
'                            units: Mg kN m C
'       icmpty  temp
        pipe500 20.
'
'       diast   thst   densst  thex     densex
        0.5     0.015  7.85    0.15      0.4
'       metkind emod       gmod
        1       206000E3   79000E3
'
'       dh is the hydrodynamic diameter
'       icode=2 => dimensionless hydrodynamic force coefficients
'       cqx      cqy      cax     cay     clx   cly    icode   dh
        0.0      0.8      0.      0.60    0.    0.     2       0.9
'
'       tb       ycurmx
        14380.   0.4329
\end{lstlisting}
\endlatexonly



#### Data group identifier {#inpmod_c_crs0_data}

~~~
NEW COMPonent CRS0
~~~





#### Component type identifier {#inpmod_c_crs0_component}

~~~
CMPTYP-ID TEMP ALPHA BETA
~~~

- `CMPTYP-ID: character(8)`: Component type identifier
- `TEMP: real, default: 0`: Temperature at which the specification applies $\mathrm{[Temp\]}$
- `ALPHA: character/real, default: 0`: Thermal expansion coefficient $\mathrm{[Temp^{-1}\]}$
    - `= STEE`: The value $\mathrm{1.2\times 10^{-5}}$ is used
    - `= TI23`: The value $\mathrm{9.0\times 10^{-6}}$ is used
    - These values are applicable for temperatures in Celcius or Kelvin
- `BETA: character/real, default: 0`: Pressure expansion coefficient $\mathrm{[1/(F/L^2)\]}$
    - `BETA` gives the expansion of an element with zero effective tension from the difference between
    the internal and the external pressure.
    - `= PIPE`: thin walled pipe assumption.
    `BETA` is calculated from the parameters given in [Cross-section parameters](@ref inpmod_c_crs0_cross) (below) as:
    $\mathrm{\frac{DIAST(1-2\nu)}{4THST\times EMOD}}$ where $\mathrm{\nu=\frac{EMOD}{2GMOD}}-1$

![Axis symmetric pipe cross section](@ref figures/um_ii_fig56.svg )
@image latex figures/um_ii_fig56.pdf "Axis symmetric pipe cross section" width=12cm




#### Cross-section parameters {#inpmod_c_crs0_cross}

~~~
DIAST THST DENSST THEX DENSEX R_EXTCNT R_INTCNT
~~~

- `DIAST: real`: Diameter of pipe $\mathrm{[L\]}$
    - `DIAST > 0`: Outer diameter of pipe
    - `DIAST < 0`: Inner diameter of pipe
- `THST: real`: Thickness of pipe $\mathrm{[L\]}$
- `DENSST: real`: Density of pipe material $\mathrm{[M/L^3\]}$
- `THEX: real, default: 0`: Thickness of external coating $\mathrm{[L\]}$
- `DENSEX: real, default: 0`: Density of external coating $\mathrm{[M/L^3\]}$
- `R_EXTCNT: real, default: 0`: Outer contact radius $\mathrm{[L\]}$
- `R_INTCNT: real, default: 0`: Inner contact radius $\mathrm{[L\]}$

Buoyancy is calculated from the total external diameter $\mathrm{DIAST+2\times THEX}$ (For `DIAST > 0`)
or $\mathrm{|DIAST|+2\times THST+2\times THEX}$ (For `DIAST < 0`).

The outer and inner contact radii of the cross section, `R_EXTCNT` and
`R_INTCNT`, are used for
- seafloor contact (unless `IBTANG = -9`; original flat bottom formulation)
- [pipe-in-pipe contact](@ref inpmod_b_pipe_pipe-in-pipe_contact)
- [tubular component contact](@ref inpmod_c_tubular)

The default values of `R_EXTCNT` and `R_INTCNT` are zero in the
present version.




#### Material properties {#inpmod_c_crs0_material_properties}




##### Material constants {#inpmod_c_crs0_material_constants}

~~~
MATKIND EMOD GMOD SIGY EMODY/NPAIR HARPAR NCIRC
~~~

- `MATKIND: integer`: Type of material model 
    - `MATKIND = 1`: linear material
    - `MATKIND = 2`: elastic-plastic
    - `MATKIND = 3`: strain-stress curve
    - `MATKIND = 4`: linear material including shear deformation
- `EMOD: real > 0`: Modulus of elasticity $\mathrm{[F/L^2\]}$
- `GMOD: real > 0`: Shear modulus $\mathrm{[F/L^2\]}$
- `SIGY: real`: Yield stress $\mathrm{[F/L^2\]}$
- `EMODY/NPAIR: real/integer`: 
    - `MATKIND = 2`: Slope of strain-stress curve for plastic region $\mathrm{[F/L^2\]}$.
        - `EMODY` < `EMOD`
    - `MATKIND = 3`: Number of user specified strain-stress relations
        - `2 <= NPAIR <= 99`
- `HARPAR: real, default: 1`: Hardening parameter for material
    - `0 <= HARPAR <= 1`
    - `HARPAR = 1`: Kinematic hardening
    - `HARPAR = 0`: Isotropic hardening
- `NCIRC: integer >= 8, default: 16`: Number of integration points along circumference

For `MATKIND = 1` or `4`: Only `EMOD` and `GMOD` are used

For `MATKIND = 4`: The shear stiffness is calculated as:
$\mathrm{GMOD\frac{\pi (D_e^2-D_i^2)}{4}0.5}$


For `MATKIND = 3`: `NPAIR` input lines of the strain-stress curve must be given 
(@ref inpmod_c_crs0_strain).




##### Strain-stress curve (NPAIR input lines to be specified for MATKIND=3) {#inpmod_c_crs0_strain}

~~~
EPS(I) SIG(I)
~~~

- `EPS(i): real`: Strain for point i on strain-stress curve $\mathrm{[1\]}$
- `SIG(i): real`: Stress for point i on strain-stress curve $\mathrm{[F/L^2\]}$

The first point in the stress-strain curve is automatically deduced: `EPS(0) = SIGY/EMOD, SIG(0) = SIGY`.
This point is taken as the proportionality limit of the material, at which the yield/hardening process
starts.
`EPS(i)` and `SIG(i)` are to be given in increasing order. The gradient of the curve must decrease with increasing strain.


#### Bending-torsion geometric coupling specification for `MATKIND = 1` or `4` {#inpmod_c_crs0_bendtors}

This data group is optional, and can only be applied for `MATKIND = 1` or `4`. 

~~~
BTGC
~~~

- `BTGC: character(4)`: bending-torsion coupling identifier. 

If the `BTGC` identifier is present, geometric coupling between torsion and bending is accounted for. 



#### Damping specification {#inpmod_c_crs0_damping}

Identical to input for cross-section type CRS1 except that the local
axial friction model, `AXFRC`, is illegal for CRS0, see 
[Damping specification](@ref inpmod_c_crs1_damping_specification).




#### Hydrodynamic force coefficients {#inpmod_c_crs0_hydrodynamic}

Identical to input for cross-section type CRS1, see [Hydrodynamic load type](@ref inpmod_c_crs1_load_type_hydr).



#### Aerodynamic force coefficients {#inpmod_c_crs0_aerodynamic}

Identical to input for cross-section type CRS1, see [Aerodynamic load type identification](@ref inpmod_c_crs1_load_type).



#### Capacity parameter {#inpmod_c_crs0_capacity}

Identical to input for cross-section type CRS1, see [Capacity parameter](@ref inpmod_c_crs1_capacity).




### CRS1 - Axisymmetric cross section {#inpmod_c_crs1_crs1}




\latexonly

%### Example input {#inpmod_c_crs1_example}

The following is a CRS1 cross section example.
Subsequent sections provide details and further options.

\begin{lstlisting}[language=riflex, numbers=none, frame=LTRB,frameround=tttt,framesep=4pt,
                                    xleftmargin=0cm,  xrightmargin=0cm,
                                    caption={CRS1 - Axisymmetric cross section, non-linear axial force and axial damping.}]
'**********************************************************************
 NEW COMPONENT CRS1
'**********************************************************************
'                             units:  Mg kN m C
'cmptyp-id temp alpha beta
 Xaxdmp    /    /     /
'ams         ae        ai   rgyr   ast wst dst thst rextcnt rintcnt
 0.3         0.0415    0    0.080  /   /   /   /    /       /
'iea  iej  igt ipress imf harpar
 3    1    1   0      0   0
'
' Axial force/strain of tensioner
' Fx     eps=L/L0-1=x/L0   (L0=1 m, x is tensioner stroke)
  1000    0.0   &
  1100    5.0   &
  1400   10.0
'ei              gas
 2.84E8          0
'gtminus
 2.19E8
'DAMP chtype1 [chtype2 chtype3 chtype4]
 DAMP  AXDMP
'idmpaxi expdmp
 1       1.737
'dmpaxi
 30.00
' icode=2 => dimensionless hydrodynamic force coefficients
'cqx  cqy    cax  cay    clx  cly    icode  d       scfkn  scfkt
 0    1.0    0    1.0      0    0    2      230E-3  1.0    1.0
'tb              ycurmx
 1600            0.1
\end{lstlisting}
\endlatexonly
 

#### Data group identifier {#inpmod_c_crs1_data}

~~~
NEW COMPonent CRS1
~~~




#### Component type identifier {#inpmod_c_crs1_component_type_identifier}

~~~
CMPTYP-ID TEMP ALPHA BETA
~~~

- `CMPTYP-ID: character(8)`: Component type identifier
- `TEMP: real, default: 0`: Temperature at which the specification applies $\mathrm{[Temp\]}$
- `ALPHA: real, default: 0`: Thermal expansion coefficient $\mathrm{[Temp^{-1}\]}$
- `BETA: real, default: 0`: Pressure expansion coefficient $\mathrm{[1/(F/L^2)\]}$
    - `BETA` gives the expansion of an element with zero effective tension from the difference between
    the internal and the external pressure.

![Axis symmetric cross section](@ref figures/um_ii_fig62.svg)
@image latex figures/um_ii_fig62.pdf "Axis symmetric cross section" width=12cm




#### Mass and volume {#inpmod_c_crs1_mass_and_volume}

~~~
AMS AE AI RGYR AST WST DST THST R_EXTCNT R_INTCNT
~~~

- `AMS: real`: Mass/unit length $\mathrm{[M/L\]}$
- `AE: real`: External cross-sectional area $\mathrm{[L^2\]}$
- `AI: real`: Internal cross-sectional area $\mathrm{[L^2\]}$
- `RGYR: real`: Radius of gyration about local x-axis $\mathrm{[L\]}$
- `AST: real`: Cross-section area for stress calculations $\mathrm{[L^2\]}$
    - The default value is calculated as seen below
- `WST: real`: Cross-section modulus for stress calculations $\mathrm{[L^3\]}$
    - The default value is calculated as seen below
- `DST: real`: Diameter for stress calculations $\mathrm{[L\]}$
    - The default value is calculated as seen below
- `THST: real`: Thickness for stress calculations $\mathrm{[L\]}$
    - The default value is calculated as seen below
- `R_EXTCNT: real, default: 0`: External contact radius $\mathrm{[L\]}$
- `R_INTCNT: real, default: 0`: Inner contact radius $\mathrm{[L\]}$

`AI` is used to calculate additional mass of internal fluid if present.
Otherwise `AI` is dummy or see below.

Default values of the stress calculation parameters will be calculated from `AE` and `AI` if `AE > AI `. A
homogenous cylinder shaped cross-section is assumed:
- `AST` $\mathrm{=AE-AI}$
- `WST` $\mathrm{=\pi (D_e^4-D_i^4)/(32D_e)}$
- `DST` $\mathrm{=D_e}$
- `THST` $\mathrm{=(D_e-D_i)/2}$
- where $\mathrm{D_e=\sqrt{\frac{4AE}{\pi }}}$ and $\mathrm{D_i=\sqrt{\frac{4AI}{\pi }}}$

The outer and inner contact radii of the cross section, `R_EXTCNT` and
`R_INTCNT`, are used for
- seafloor contact (unless `IBTANG = -9`; original flat bottom formulation)
- [pipe-in-pipe contact](@ref inpmod_b_pipe_pipe-in-pipe_contact)
- [tubular component contact](@ref inpmod_c_tubular)

The default values of `R_EXTCNT` and `R_INTCNT` are zero in the
present version.




#### Stiffness properties classification {#inpmod_c_crs1_stiffness_properties}

~~~
IEA IEJ IGT IPRESS IMF HARPAR
~~~

- `IEA: integer, default: 1`: Axial stiffness code
    - 1 - constant stiffness
    - N - table with N pairs of tension-elongation to be specified
    - N >= 2
- `IEJ: integer, default: 0`:
    - `0` - zero bending stiffness
    - 1 - constant stiffness
    - N - table with N pairs of bending moment - curvature to be specified
    - N >= 2
- `IGT: integer, default: 0`: Torsion stiffness code
    - `0` - zero torsional stiffness
    - 1 - constant stiffness
    - -1- non-symmetric "constant" stiffness
    - N - symmetric, (N positive) pairs specified
    - -N- general torsion/relation (non-symmetric) N pairs specified
    - N >= 2
- `IPRESS: integer, default: 0`: Pressure dependency parameter related to bending moment
    - `0` - no pressure dependency
    - 1 - linear dependency (not implemented)
    - NP - NP sets of stiffness properties to be given, corresponding to a table of NP pressure values (not implemented)
        - 2 <= NP <= 10
- `IMF: integer, default: 0`: Hysteresis option in bending moment/curvature relation
    - `0` - no hysteresis
    - 1 - hysteresis generated by an internal friction moment at reversed curvature
- `HARPAR: real, default: 0`: Hardening parameter for kinematic/isotropic hardening
    - `0 <= HARPAR <= 1`
    - Only to be given if `IEJ > 1` and `IMF = 1`

`IEJ` and `IGT` must both be zero or both greater than zero to assure stability in the `FEM` analysis.

Note that:
- `IPRESS=0` in this version.
- `IMF=0`, `IMF=1` is implemented in present version.
- `IMF` $\mathrm{\neq }$  `0` should be used with care as the analysis can become unstable.


#### Bending-torsion geometric coupling specification {#inpmod_c_crs1_bendtors_1}

This data group is optional, and will only be applied for `IEJ=1`, `IGT=1`, and `IMF=0`. 

~~~
BTGC
~~~

- `BTGC: character(4)`: bending-torsion coupling identifier. 

If the `BTGC` identifier is present, geometric coupling between torsion and bending is accounted for. 


#### Axial stiffness. Case 1, IEA=1 {#inpmod_c_crs1_axial_stiffness_case_1}

~~~
EA
~~~

- `EA: real > 0`: Axial stiffness $\mathrm{[F\]}$




#### Axial stiffness. Case 2, IEA=N {#inpmod_c_crs1_axial_stiffness_case_2}

~~~
EAF(1) ELONG(1) . . . EAF(N) ELONG(N)
~~~

- `EAF(1): real`: Axial force corresponding to relative elongation `ELONG(1)` $\mathrm{[F\]}$
- `ELONG(1): real`: Relative elongation ()
- .
- .
- .

The pairs of `EAF` and `ELONG` must be given in increasing order on a single input line.

\anchor Axial_force_corresponding_to_relative_elongation
![Axial force corresponding to relative elongation](@ref figures/um_ii_fig70.svg)
@image latex figures/um_ii_fig70.pdf "Axial force corresponding to relative elongation" width=8cm




#### Bending stiffness properties {#inpmod_c_crs1_bending_stiffness_properties}

The amount of input depends upon the parameters `IEJ`, `IPRESS` and `IMF` according to the table below:
- Case: 0, `IEJ`: 0, `IPRESS`: 0, Allowed IMF-values: 0, Data required: None.
- Case: 1a, `IEJ`: 1, `IPRESS`: 0, Allowed IMF-values: 0, Data required: `EI, GAs`.
- Case: 1b, `IEJ`: 1, `IPRESS`: 0, Allowed IMF-values: 1, Data required: `EI, MF`.
- Case: 2, `IEJ`: 1, `IPRESS`: 1, Allowed IMF-values: 0, Data required: Not implemented.
- Case: 3, `IEJ`: N, `IPRESS`: 0, Allowed IMF-values: 0, 1, Data required: `CURV(I): I=1,N. BMOM(I): I=1,N`.
- Case: 4, `IEJ`: N1, `IPRESS`: N2, Allowed IMF-values: 0, Data required: Not implemented.




#### Bending stiffness. Case 1a, IEJ=1 IPRESS=0 IMF=0 {#inpmod_c_crs1_bending_stiffness_case_1a}

~~~
EI GAs
~~~

- `EI: real > 0`: Bending stiffness $\mathrm{[FL^2\]}$
- `GAs: real`: Shear stiffness $\mathrm{[F\]}$

The shear stiffness, `GAs`, is an optional input parameter.
Specified `GAs > 0` will include shear deformation. This requires that all stiffness properties
are constant, i.e. `IEA = 1`, `IEJ = 1`, `IGT = 1`




#### Bending stiffness. Case 1b, IEJ=1 IPRESS=0 IMF=1 {#inpmod_c_crs1_bending_stiffness_case_1b}

~~~
EI MF SF
~~~

- `EI: real`: Bending stiffness $\mathrm{[FL^2\]}$
- `MF: real`: Internal friction moment, see figure below. $\mathrm{[FL\]}$
- `SF: real, default: 10.`: Internal friction moment stiffness factor. $\mathrm{[1\]}$

The default value of `SF` corresponds to the earlier fixed value of 10.0.

![Internal friction moment description](@ref figures/um_ii_fig71.svg)
@image latex figures/um_ii_fig71.pdf "Internal friction moment description" width=8cm




#### Bending stiffness. Case 2, IEJ=1 IPRESS=1 (Not implemented) {#inpmod_c_crs1_bending_stiffness_case_2}

~~~
EI(1) PRESS(1) EI(2) PRESS(2) MF(1) MF(2)
~~~

- `EI(1): real`: Bending stiffness $\mathrm{[FL^2\]}$
- `PRESS(1): real`: Pressure at which the above values apply $\mathrm{[F/L^2\]}$
- `EI(2): real`: See description above
- `PRESS(2):`
- `MF(1): real`: Internal friction moment for pressure PRESS(1)
- `MF(2): real`: Internal friction moment for pressure PRESS(2)

`PRESS(1) < PRESS(2)`

`MF(1) and MF(2) dummy for IMF = 0`

![Bending stiffness around y-axis as function of pressure](@ref figures/um_ii_fig72.svg)
@image latex figures/um_ii_fig72.pdf "Bending stiffness around y-axis as function of pressure" width=12cm

Values at other pressure levels than `PRESS(1)` and `PRESS(2)` are obtained by linear interpolation/
extrapolation.




#### Bending stiffness description. Case 3 IEJ=N IPRESS=0 {#inpmod_c_crs1_bending_stiffness_case_3}

Tabulated curvature/bending moment relation. This specification consists of two different input lines.
For `IMF` $\mathrm{\neq }$ `0` cfr. [Bending stiffness. Case 4...](@ref inpmod_c_crs1_bending_stiffness_case_4)




##### Curvature {#inpmod_c_crs1_bending_stiffness_case_3_curvature}

~~~
CURV(1) ... CURV(N)
~~~

- `CURV(1): real`: Curvature values for which bending moment is specified $\mathrm{[1/L\]}$
- .
- .
- .
- `CURV(N)`: To be specified in increasing order

`CURV=1/CURVATURE RADIUS`




##### Bending moment, y-axis {#inpmod_c_crs1_bending_stiffness_case_3_moment}

~~~
BMOMY(1) BMOMY(N)
~~~

- `BMOMY(1): real`: Bending moment around y-axis $\mathrm{[FL\]}$ corresponding to curvature values given above in 'Curvature'.
- `BMOMY(N)`

`CURV(1), BMOMY(1)` have to be zero.
Positive slope required, i.e.: `BMOMY(I+1) > BMOMY(I)`.

\anchor Bending_moment_around_y-axis_as_function_of_curvature
![Bending moment around y-axis as function of curvature](@ref figures/um_ii_fig74.svg)
@image latex figures/um_ii_fig74.pdf "Bending moment around y-axis as function of curvature" width=12cm




#### Bending stiffness. Case 4 IEJ=N1, IPRESS=N2 (Not implemented) {#inpmod_c_crs1_bending_stiffness_case_4}
This specification consists of three different input lines.




##### Curvature {#inpmod_c_crs1_bending_stiffness_case_4_curvature}

~~~
CURV(1) ... CURV(N)
~~~

- `CURV(1): real`: Curvature values for which bending moment is specified $\mathrm{[1/L\]}$
- .
- .
- .
- `CURV(N)`: To be specified in increasing order

`CURV=1/CURVATURE RADIUS`

CURV(1) has to be zero




##### Pressure {#inpmod_c_crs1_bending_stiffness_case_4_pressure}

~~~
PRESS(1) ... PRESS(N)
~~~

- `PRESS(1): real`: Pressure levels for which bending moment is specified $\mathrm{[F/L^2\]}$
- `PRESS(N)`:




##### Bending moment, y-axis {#inpmod_c_crs1_bending_stiffness_case_4_moment}

~~~
BMOMY(1,1) BMOMY(N1,N2)
~~~

- `BMOMY(1,1): real`: Bending moment at curvature I and pressure J $\mathrm{[FL\]}$.
- `BMOMY(N1,N2)`

`BMOMY(1,J), J=1,N2` have to be zero, see also the figure below. 
Positive slope with increasing curvature is required, i.e.: `BMOMY(I+1,J) > BMOMY(I,J)`.

\anchor Bending_moment_around_y-axis_as_function_of_curvature_and_pressure
![Bending moment around y-axis as function of curvature and pressure](@ref figures/um_ii_fig75.svg)
@image latex figures/um_ii_fig75.pdf "Bending moment around y-axis as function of curvature and pressure" width=12cm




#### Torsion stiffness {#inpmod_c_crs1_torsion_stiffness}

No data required for `IGT=0`.




##### Constant torsion stiffness. Case 1 |IGT|=1 {#inpmod_c_crs1_torsion_constant}

~~~
GT- GT+
~~~

- `GT-: real > 0`: Torsion stiffness $\mathrm{[FL^2/Radian\]}$
- `GT+: real`: D.o. for positive twist. Dummy if `IGT=1`




##### Nonlinear torsion stiffness. Case 2 |IGT|=N {#inpmod_c_crs1_torsion_nonlinear}

~~~
TMOM(1) TROT(1) . . . TMOM(N) TROT(N)
~~~

- `TMOM(1): real`: Torsion moment $\mathrm{[FL\]}$
- `TROT(1): real`: Torsion angle/length $\mathrm{[Radian/L\]}$
- .
- .
- . 
- `TMOM(N)`:
- `TROT(N): real`:

If `IGT` is positive `TMOM(1)` and `TROT(1)` have to be zero. `TROT` must be given in increasing order.




#### Damping specification {#inpmod_c_crs1_damping_specification}

This data group is optional. It enables the user to specify cross sectional damping properties of the following types:
- mass proportional damping
- stiffness proportional damping
- axial damping properties

Specification of mass and stiffness proportional damping specification will overrule corresponding
damping specification given on global level as input to Dynmod data group [Time integration and damping parameters](@ref dynmod_e_method_time).




##### Data group identifier and selection of damping types {#inpmod_c_crs1_damping_data}

~~~
DAMP CHTYPE1 CHTYPE2 CHTYPE3 CHTYPE4
~~~

- `DAMP: character(4)`: Data group identifier (the text "DAMP")
- `CHTYPE1: character(5)`: 
    - `=MASPR: Mass proportional damping
    - `=STFPR: Stiffness proportional damping
    - `=AXDMP: Local axial damping model
    - `=AXFRC: Local axial friction model
- `CHTYPE2: character(5)`: Similar to CHTYPE1
- `CHTYPE3: character(5)`: Similar to CHTYPE1
- `CHTYPE4: character(5)`: Similar to CHTYPE1

Between one and four damping types may be selected. The order of the
damping type selection is arbitrary.

In the following the damping parameters for the selected damping types
is described. The input lines have to be given in one block and in the
order described below. Skip input for damping types which are not
selected.



##### Parameters for mass proportional damping, if MASPR is specified {#inpmod_c_crs1_damping_parameters_mass}

~~~
A1T A1TO A1B
~~~

- `A1T: real`: Factor for mass proportional damping in axial dofs.
- `A1TO: real, default: A1T`: Factor for mass proportional damping in torsional dofs.
- `A1B: real, default: A1TO`: Factor for mass proportional damping in bending dofs.

The element stiffness proportional damping matrix is computed by:

$\mathrm{\boldsymbol{\mathrm{c_m}}=a_{1t}\boldsymbol{\mathrm{m}}_t+a_{1to}\boldsymbol{\mathrm{m}}_{to}+a_{1b}\boldsymbol{\mathrm{m}}_b}$

where $\boldsymbol{\mathrm{m}}$ is the local stiffness matrix and the subscripts “t”, “to” and “b” refer to axial, torsional and
bending contributions, respectively.




##### Parameters for stiffness proportional damping, if STFPR is specified {#inpmod_c_crs1_damping_parameters_stiffness}

~~~
A2T A2TO A2B  DAMP_OPT
~~~

- `A2T: real`: Factor for stiffness proportional damping in axial dofs.
- `A2TO: real, default: A2T`: Factor for stiffness proportional damping in torsional dofs.
- `A2B: real, default: A2TO`: Factor for stiffness proportional damping in bending dofs.
- `DAMP_OPT: character(4), default: TOTA`: Option for stiffness contribution to Rayleigh damping
    - = TOTA: Stiffness proportional damping is applied using total stiffness, i.e. both material and geometric stiffness
    - = MATE: Stiffness proportional damping is applied using material stiffness only
    
The element stiffness proportional damping matrix is computed by:

$\mathrm{\boldsymbol{\mathrm{c_k}}=a_{2t}\boldsymbol{\mathrm{k}}_t+a_{2to}\boldsymbol{\mathrm{k}}_{to}+a_{2b}\boldsymbol{\mathrm{k}}_b}$

where $\boldsymbol{\mathrm{k}}$ is the local stiffness matrix and the subscripts “t”, “to” and “b” refer to axial, torsional and
bending contributions, respectively.




##### Parameters for local axial damping, if AXDMP is specified {#inpmod_c_crs1_damping_parameters_damping}

The local axial damping model is written:

$\mathrm{F=C(\varepsilon )\times |\dot {\varepsilon }|^P\times sign(\dot {\varepsilon })}$

where:
- $\mathrm{F}$: damping force
- $\mathrm{C}$: damping coefficient (strain dependent)
- $\mathrm{\varepsilon }$: relative elongation
- $\mathrm{\dot {\varepsilon }}$: strain velocity
- $\mathrm{P}$: exponent for strain velocity (P >= 1)


~~~
IDMPAXI EXPDMP
~~~

- `IDMPAXI: integer`: Damping coefficient code
    - = 1: Constant damping coefficient
    - = N: Table with N pairs of damping coefficient - elongation to be specified. 
    - N >= 2
- `EXPDMP: real`: Exponent for strain velocity


IDMPAXI = 1
~~~
DMPAXI
~~~

- `DMPAXI: real`: Damping coefficient (constant)


IDMPAXI >1
~~~
DMPAXI(1) ELONG(1) . . . . . . . . DMPAXI(IDMPAXI) ELONG(IDMPAXI) 
~~~

- `DMPAXI(1): real`: Damping coefficient corresponding to relative elongation `ELONG(1)`
- `ELONG(1): real`: Relative elongation ( )

`ELONG` must be given in increasing order for the pairs of `DMPAXI`
and `ELONG` . All pairs are given on a single input line




##### Parameters for local axial friction, if AXFRC is specified {#inpmod_c_crs1_damping_parameters_friction}

~~~
FRCAXI(1) ELONG(1) FRCAXI(2) ELONG(2)
~~~

- `FRCAXI(1): real`: Static friction force corresponding to elongation `ELONG(1)`
- `ELONG(1): real`: Relative elongation ( )
- `FRCAXI(2): real, default: FRCAXI(1)`: Dynamic friction force corresponding to elongation `ELONG(2)`
- `ELONG(2): real, default: 1.1 x ELONG(1)`: Relative elongation ( )

`ELONG(2) > ELONG(1)`



#### Hydrodynamic load type identification, One optional input line {#inpmod_c_crs1_load_type_hydr}

~~~
CHLOAD 
~~~

- `CHLOAD: character`: `= HYDR` - Text to identify hydrodynamic coefficients

Note: Required if non-Morison loads are to be specified


##### Load type identification if CHLOAD=HYDR, One input line {#inpmod_c_crs1_hydro_load}

~~~
CHTYPE
~~~

- `CHTYPE: character`: Type of load coefficients
    - `= NONE`: No hydrodynamic load coefficients
    - `= MORI`: Slender element hydrodynamic coefficients
    - `= MACF`: MacCamy-Fuchs with quadratic drag load coefficients
    - `= POTN`: Potential flow with quadratic drag load coefficients
    - `= TVIV`: Time domain VIV load coefficients. Restricted option.

Note that the option `POTN` currently is under testing. Potential flow
forces are only available for irregular time domain analysis.

Note that the option `TVIV` is currently under development.


##### Hydrodynamic force coefficients if CHTYPE=MORI {#inpmod_c_crs1_hydrodynamic}

Interpretation of hydrodynamic coefficients are dependent on the input parameter `ICODE`. Input of
dimensional hydrodynamic coefficient is specified giving `ICODE=1` while input of nondimensional of
hydrodynamic coefficients for circular cross sections is specified giving `ICODE=2`.

Definitions of dimensional/nondimensional hydrodynamic force coefficients are given below.

~~~
CQX CQY CAX CAY CLX CLY ICODE D SCFKN SCFKT
~~~

- `CQX: real`: Quadratic drag coefficient in tangential direction
    - `ICODE=1: CQX=CDX`: dimensional drag force coefficient $\mathrm{[F/((L/T)^2\times L)\]}$
    - `ICODE=2: CQX=Cdt`: nondimensional drag force coefficient
- `CQY: real`: Quadratic drag coefficient in normal direction
    - `ICODE=1: CQY=CDY`: dimensional drag force coefficient $\mathrm{[F/((L/T)^2\times L)\]}$
    - `ICODE=2: CQY=Cdn`: nondimensional drag force coefficient
- `CAX: real`: Added mass per unit length in tangential direction
    - `ICODE=1: CAX=AMX`: added mass $\mathrm{[M/L\]}$
    - `ICODE=2: CAX=Cmt`: nondimensional added mass coefficient
- `CAY: real`: Added mass per unit length in normal direction
    - `ICODE=1: CAY=AMY`: added mass $\mathrm{[M/L\]}$
    - `ICODE=2: CAY=Cmn`: nondimensional added mass coefficient
- `CLX: real`: Linear drag force coefficient in tangential direction
    - `ICODE=1: CLX=CDLX`: dimensional linear drag coefficient  $\mathrm{[F/((L/T)\times L)\]}$
    - `ICODE=2: CLX=CdtL`: nondimensional linear drag force coefficient
- `CLY: real`: Linear drag force coefficient in normal direction
    - `ICODE=1: CLY=CDLY`: dimensional linear drag force coefficient $\mathrm{[F/((L/T)\times L)\]}$
    - `ICODE=2:CLY=CdnL`: nondimensional linear drag force coefficient
- `ICODE: integer, default: 1`: `ICODE` Code for input of hydrodynamic force coefficients
    - `ICODE=1`: Dimensional coefficients
    - `ICODE=2`: Nondimensional coefficients
- `D: real, default:`$\sqrt{\mathrm{\frac{4}{\pi }(AE)}}$: Hydrodynamic diameter of the pipe $\mathrm{[L\]}$.
    - Default value is calculated from external cross-sectional area given as input
    in data section [Mass and volume](@ref inpmod_c_crs1_mass_and_volume)
    - Note that the hydrodynamic diameter is a key parameter in `VIVANA`. 
      `D` is dummy in the other modules for `ICODE=1` unless marine growthis apploed.
- `SCFKN: real, default: 1`: Scaling factor for the Froude-Krylov term in Morison’s equation in 
    normal direction
- `SCFKT: real, default: 1`: Scaling factor for the Froude-Krylov term in Morison’s equation in 
    tangential direction. Only the values 0.0 and 1.0 are permitted.


##### Definition of hydrodynamic force coefficients

The tangential force which is a friction force per unit length acting in local x-axis, $\mathrm{Ft}$ is computed by:

$\mathrm{Ft=CDX\times VRELX\times |VRELX|+CDLX\times VRELX}$

The drag force per unit length acting normal to the local x-axis, $\mathrm{F_n}$, is computed by assuming that
the instantaneous drag force direction is parallel to the instantaneous transverse relative velocity component:

$\mathrm{F_n=CDY(VRELY^2+VRELZ^2)+CDLY\times \sqrt{VRELY^2+VRELZ^2}}$


where:
- $\mathrm{CDX,CDY}$: are the dimensional quadratic drag force coefficients in local x- and y-directions (i.e. tangential and normal directions)
- $\mathrm{CDLX,CDLY}$: are the dimensional linear drag force coefficients in local x- and y-directions
- $\mathrm{VRELX,VRELY,VRELZ}$: are relative water velocities in local x,y and z-directions

The nondimensional hydrodynamic force coefficients for a circular cross section are defined according to the following expressions:
- $\mathrm{CDX=\frac{1}{2}\rho S_WC_{dt}}$
- $\mathrm{CDY=\frac{1}{2}\rho DC_{dn}}$
- $\mathrm{CDLX=\rho \sqrt{gS_W}\times S_W^2C^L_{dt}}$
- $\mathrm{CDLY=\rho \sqrt{gD}\times D^2C^L_{dt}}$
- $\mathrm{AMX=\rho \frac{\pi D^2}{4}C_{mt}}$
- $\mathrm{AMY=\rho \frac{\pi D^2}{4}C_{mn}}$

where:

- $\mathrm{\rho }$: water density
- $\mathrm{g}$: acceleration of gravity
- $\mathrm{S_W}$: cross sectional wetted surface $\mathrm{(=\pi D)}$
- $\mathrm{D}$: hydrodynamic diameter of the pipe
- $\mathrm{C_{dt}}$: nondimensional quadratic tangential drag coefficient
- $\mathrm{C_{dn}}$: nondimensional quadratic normal drag coefficient
- $\mathrm{C^L_{dt}}$: nondimensional linear tangential drag coefficient
- $\mathrm{C^L_{dn}}$: nondimensional linear normal drag coefficient
- $\mathrm{C_{mt}}$: nondimensional tangential added mass coefficient
- $\mathrm{C_{mn}}$: normal added mass coefficient
    - ($\mathrm{C_{mn}}$ is normally equal to 1.0 for a circular cross section)


##### Hydrodynamic force coefficients if CHTYPE=MACF {#inpmod_c_crs1_hydrodynamic_macf}

MacCamy-Fuchs frequency-dependent hydrodynamic loads on a stationary
vertical circular cylinder will be applied for
`CHTYPE=MACF`. MacCamy-Fuchs forces are pre-computed based on the
element position after static calculation. MacCamy-Fuchs forces are
only available for irregular time domain analysis.

Quadratic drag may also be applied on cross-sections with
MacCamy-Fuchs loading.


###### Hydrodynamic force coefficients
~~~
CQX CQY CAX ICODE D
~~~

- `CQX: real`: Quadratic drag coefficient in tangential direction
    - `ICODE=1: CQX=CDX`: dimensional drag force coefficient $\mathrm{[F/((L/T)^2\times L)\]}$
    - `ICODE=2: CQX=Cdt`: nondimensional drag force coefficient
- `CQY: real`: Quadratic drag coefficient in normal direction
    - `ICODE=1: CQY=CDY`: dimensional drag force coefficient $\mathrm{[F/((L/T)^2\times L)\]}$
    - `ICODE=2: CQY=Cdn`: nondimensional drag force coefficient
- `CAX: real, default: 0.0`: Added mass per unit length in tangential direction
    - `ICODE=1: CAX=AMX`: added mass $\mathrm{[M/L\]}$
    - `ICODE=2: CAX=Cmt`: nondimensional added mass coefficient
- `ICODE: integer`: Code for input of hydrodynamic drag coefficients
    - `ICODE=1`: Dimensional coefficients
    - `ICODE=2`: Nondimensional coefficients
- `D: real, default:`$\sqrt{\mathrm{\frac{4}{\pi }(AE)}}$: Hydrodynamic diameter of the pipe $\mathrm{[L\]}$.
    - Default value is calculated from external cross-sectional area given as input in data
      section [Mass and volume](@ref inpmod_c_crs1_mass_and_volume)


###### Simplified radiation force

The horizontal radiation loads is based on an added mass coefficient and a damping coefficient. 
~~~
AMY DAMP
~~~
	
- `AMY: real, default: 0.0`: Added mass per unit length in normal direction $\mathrm{[M/L\]}$
- `DAMP: real, default: 0.0`: Damping in normal direction

Note: The input CHTYPE=MACF is extended in Riflex 4.13 and is not
compatible with earlier versions of Riflex.


##### Hydrodynamic force coefficients if CHTYPE=POTN {#inpmod_c_crs1_hydrodynamic_potn}

Frequency-dependent added mass, radiation damping, and excitation
forces based on the first order potential flow solution will be
applied for `CHTYPE=POTN`. The radiation and diffraction coefficients
are to be given by a separate input file specified under the data
group 
[Potential flow library specification] (@ref inpmod_b_poten_lib).

Quadratic drag may also be applied on cross-sections with potential
flow loading.

~~~
CQX CQY ICODE D SCFKT
~~~

- `CQX: real`: Quadratic drag coefficient in tangential direction
    - `ICODE=1: CQX=CDX`: dimensional drag force coefficient $\mathrm{[F/((L/T)^2\times L)\]}$
    - `ICODE=2: CQX=Cdt`: nondimensional drag force coefficient
- `CQY: real`: Quadratic drag coefficient in normal direction
    - `ICODE=1: CQY=CDY`: dimensional drag force coefficient $\mathrm{[F/((L/T)^2\times L)\]}$
    - `ICODE=2: CQY=Cdn`: nondimensional drag force coefficient
- `ICODE: integer, default: 1`: `ICODE` Code for input of hydrodynamic force coefficients
    - `ICODE=1`: Dimensional coefficients
    - `ICODE=2`: Nondimensional coefficients
- `D: real, default:`$\sqrt{\mathrm{\frac{4}{\pi }(AE)}}$: Hydrodynamic diameter of the pipe $\mathrm{[L\]}$.
    - Default value is calculated from external cross-sectional area given as input
    in data section [Mass and volume](@ref inpmod_c_crs1_mass_and_volume)
- `SCFKT: real, default: 1`: Scaling factor for the Froude-Krylov term in Morison’s equation in 
    tangential direction. Only the values 0.0 and 1.0 are permitted.



##### Hydrodynamic force coefficients if CHTYPE=TVIV {#inpmod_c_crs1_hydrodynamic_tviv}

Restricted option. Under implementation.

~~~
CQX CQY CAX CAY CLX CLY ICODE D SCFKN SCFKT
~~~

See the description above for 
[Morison coefficients](@ref inpmod_c_crs1_hydrodynamic ).


~~~
CV FNULL FMIN FMAX NMEM CVIL ALPHIL CHH
~~~

- `CV: real > 0`: Vortex shedding force coefficient for the (instantaneous) cross-flow load term (nondimensional)
- `FNULL: real > 0`: Natural vortex shedding frequency (nondimensional)
- `FMIN: real > 0`: Minimum vortex shedding frequency (nondimensional)
- `FMAX: real > FMIN`: Maximum vortex shedding frequency (nondimensional)
- `NMEM: integer > 0`: Number of time steps used in calculation of standard deviation
- `CVIL: real >= 0, default: 0.0`: Vortex shedding force coefficient for (instantaneous) in-line load term  (nondimensional)
- `ALPHIL: real >= 0, default: 0.0`: Nondimensional parameter giving freedom to in-line excitation frequency
- `CHH: real >= 0, default: 0.0`: Higher harmonic load coefficient (nondimensional)

Specifying `CVIL`, `ALPHIL` and `CHH` as zero will give excitation only
in the updated cross-flow direction.




#### Aerodynamic load type identification, One optional input line {#inpmod_c_crs1_load_type}

~~~
CHLOAD 
~~~

- `CHLOAD: character`: `= WIND` - Text to identify wind coefficients


##### Load type identification if CHLOAD=WIND, One input line {#inpmod_c_crs1_load_mori}

~~~
CHTYPE
~~~

- `CHTYPE: character`: Type of load coefficients
    - `= MORI`: Morison-like loading, Drag term 


##### Drag coefficients if CHTYPE=MORI, One input line {#inpmod_c_crs1_airmori}

~~~
CDXAERO CDYAERO ICODE D 
~~~

- `CDXAERO: real`: Quadratic drag coefficient in tangential direction
    - `ICODE=1: CDXAERO=CDXa`: dimensional drag force coefficient $\mathrm{[F/((L/T)^2\times L)\]}$
    - `ICODE=2: CDXAERO=Cdta`: non-dimensional drag force coefficient
- `CDYAERO: real`: Quadratic drag coefficient in normal direction
    - `ICODE=1: CDYAERO=CDYa`: dimensional drag force coefficient $\mathrm{[F/((L/T)^2\times L)\]}$
    - `ICODE=2: CDYAERO=Cdna`: non-dimensional drag force coefficient
- `ICODE: integer, default: 1`: Code for input of aerodynamic force coefficients
    - `ICODE=1`: Dimensional coefficients
    - `ICODE=2`: Nondimensional coefficients
- `D: real, default:`$\sqrt{\mathrm{\frac{4}{\pi }(AE)}}$: Aerodynamic diameter of the pipe $\mathrm{[L\]}$.
    - Default value is calculated from external cross-sectional area given as input
    in data section [Mass and volume](@ref inpmod_c_crs1_mass_and_volume)
    - Dummy for `ICODE=1`


The tangential force which is a friction force per unit length acting in local x-axis,
 $\mathrm{F_t}$ is computed by:

$\mathrm{F_t=CDXa\times VRELX\times |VRELX|}$

The drag force per unit length acting normal to the local x-axis, $\mathrm{F_n}$, 
is computed by assuming that the instantaneous drag force direction is parallel to 
the instantaneous transverse relative velocity component:

$\mathrm{F_n=CDYa(VRELY^2+VRELZ^2)}$

where:
- $\mathrm{CDXa,CDYa}$: are the dimensional quadratic drag force coefficients in local x- and y-directions (i.e. tangential and normal directions)
- $\mathrm{VRELX,VRELY,VRELZ}$: are relative wind velocities in local x,y and z-directions

The nondimensional aerodynamic force coefficients for a circular cross section are defined according to the following expressions:
- $\mathrm{CDXa=\frac{1}{2}\rho _aS_WC_{dta}}$
- $\mathrm{CDYa=\frac{1}{2}\rho _aDC_{dna}}$

where:

- $\mathrm{\rho _a}$: air density
- $\mathrm{S_W}$: cross sectional perimeter $\mathrm{(=\pi D)}$
- $\mathrm{D}$: aerodynamic diameter of the pipe
- $\mathrm{C_{dta}}$: nondimensional quadratic tangential drag coefficient
- $\mathrm{C_{dna}}$: nondimensional quadratic normal drag coefficient



#### Capacity parameter {#inpmod_c_crs1_capacity}

~~~
TB YCURMX
~~~

- `TB: real`: Tension capacity $\mathrm{[F\]}$
- `YCURMX: real`: Maximum curvature $\mathrm{[1/L\]}$

These parameters are dummy in the present version




###  CRS2 - Double symmetric cross section {#inpmod_c_crs2_cross_section}




#### Data group identifier {#inpmod_c_crs2_data}

~~~
NEW COMPonent CRS2
~~~




#### Component type identifier {#inpmod_c_crs2_component}

~~~
CMPTYP-ID TEMP
~~~

- `CMPTYP-ID: character(8)`: Component type identifier
- `TEMP: real`: Temperature at which the specification applies 
    - Dummy in present version

![Cross section with 2 symmetry planes](@ref figures/um_ii_fig89.svg)
@image latex figures/um_ii_fig89.pdf "Cross section with 2 symmetry planes" width=12cm




#### Mass and volume {#inpmod_c_crs2_mass}

~~~
AMS AE AI RGYR
~~~

- `AMS: real`: Mass per unit length $\mathrm{[M/L\]}$
- `AE: real`: External cross-sectional area $\mathrm{[L^2\]}$
- `AI: real`: Internal cross-sectional area $\mathrm{[L^2\]}$
- `RGYR: real`: Radius of gyration about local x-axis $\mathrm{[L\]}$

`AI` is used to calculate additional mass of internal fluid if present. Otherwise `AI` is dummy.

Note that the mass center is located along the local X-axis, i.e. at the origin of the local Y- and Z-axes.




#### Stiffness properties classification {#inpmod_c_crs2_stiffness_properties}

~~~
IEA IEJ IGT IPRESS
~~~

- `IEA: integer, default: 0`: Axial stiffness code
    - 1 - constant stiffness
    - N - table with N pairs of tension-elongation to be specified 
    - N >= 2
- `IEJ: integer, default: 0`:
    - `0` - zero bending stiffness
    - 1 - constant stiffness
    - N - table with N pairs of bending moment - curvature to be specified. 
    - N >= 2
- `IGT: integer, default: 0`: Torsion stiffness code
    - `0` - zero torsional stiffness
    - 1 - constant stiffness
    - -1- non-symmetric "constant" stiffness
    - N - symmetric, N (positive) pairs specified
    - -N- general torsion/relation (non-symmetric) N pairs specified
    - N >= 2
- `IPRESS: integer, default: 0`: Pressure dependency parameter related to bending moment
    - `0` - no pressure dependency
    - 1 - linear dependency (not implemented)
    - NP - NP sets of stiffness properties to be given, corresponding to a table of NP pressure values  (not implemented)
        - 2 <= NP <= 10

Normally `IEJ` and `IGT` should both be zero or both greater than zero to assure stability in the `FEM` analysis.

`IPRESS=0` in this version of the program.


#### Bending-torsion geometric coupling specification {#inpmod_c_crs1_bendtors_2}

This data group is optional, and will only be applied for `IEJ=1` and `IGT=1`. 

~~~
BTGC
~~~

- `BTGC: character(4)`: bending-torsion coupling identifier. 

If the `BTGC` identifier is present, geometric coupling between torsion and bending is accounted for. 


#### Axial stiffness. Case 1 IEA=1  {#inpmod_c_crs2_axial_stiffness_case1}

~~~
EA
~~~

- `EA: real > 0`: Axial stiffness $\mathrm{[F\]}$




#### Axial stiffness. Case 2 IEA=N {#inpmod_c_crs2_axial_stiffness_case2}

~~~
EAF(1) ELONG(1) . . . EAF(N) ELONG(N)
~~~

- `EAF(1): real`: Axial force corresponding to relative elongation `ELONG(1)` $\mathrm{[F\]}$
- `ELONG(1): real`: Relative elongation ()
- .
- .
- .
- `EAF(N): real`:
- `ELONG(N): real`:

The pairs of `EAF` and `ELONG` must be given in increasing order. 
See also the figure [Axial force corresponding to relative elongation](@ref Axial_force_corresponding_to_relative_elongation).




#### Bending stiffness properties {#inpmod_c_crs2_bending_stiffness_properties}

The amount of input depends upon the parameters `IEJ` and `IPRESS` according to the table below:
- Case: 0, `IEJ`: 0, `IPRESS`: 0, Data required: None.
- Case: 1, `IEJ`: 1, `IPRESS`: 0, Data required: `EJY, EZJ, MFY, MF2`.
- Case: 2, `IEJ`: 1, `IPRESS`: 1, Data required: Not implemented.
- Case: 3, `IEJ`: N, `IPRESS`: 0, Data required: `CURV(I): I=1,N. BMOMY(I): I=1,N. BMOMZ(I)`
- Case: 4, `IEJ`: N1, `IPRESS`: N2, Data required: Not implemented.

Thus, the following data are required for the respective cases:




#### Bending stiffness. Case 1, IEJ=1 IPRESS=0 {#inpmod_c_crs2_bending_stiffness_case1}

~~~
EJY EJZ GAsZ GAsY
~~~

- `EJY: real > 0`: Bending stiffness around local y-axis $\mathrm{[FL^2\]}$
- `EJZ: real > 0`: Bending stiffness around z-axis $\mathrm{[FL^2\]}$
- `GAsZ: real`: Shear stiffness in Z-direction $\mathrm{[F\]}$
- `GAsY: real`: Shear stiffness in Y-direction $\mathrm{[F\]}$

The shear stiffness, `GAsZ` and `GAsY`, are optional input parameters. 

Specified `GAsZ>0` and `GAsY>0` will include shear deformation. This requires that all stiffness properties
are constant, i.e. `IEA = 1`, `IEJ = 1`, `IGT = 1`.

Note that the shear center is located along the local X-axis, i.e. at the origin of the local Y- and Z-axes.




#### Bending stiffness. Case 2, IEJ=1 IPRESS=1 (Not implemented) {#inpmod_c_crs2_bending_stiffness_case2}

~~~
EJY(1) EJZ(1) PRESS(1) EJY(2) EJZ(2) PRESS (2)
~~~

- `EJY(1): real`: Bending stiffness around local y-axis $\mathrm{[FL^2\]}$
- `EJZ(1): real`: Bending stiffness around local z-axis $\mathrm{[FL^2\]}$
- `PRESS(1): real`: Pressure at which the above values apply $\mathrm{[F/L^2\]}$
- `EJY(2): real`: Bending moments corresponding to 2nd pressure level, see description above
- `EJZ(2): real`:
- `PRESS(2): real`:

`PRESS(1) < PRESS(2)`

![Bending stiffness around y-axis as function of pressure.](@ref figures/um_ii_fig93.svg)
@image latex figures/um_ii_fig93.pdf "Bending stiffness around y-axis as function of pressure." width=12cm

Values at other pressure levels than `PRESS(1)` and `PRESS(2)` are obtained by linear interpolation/
extrapolation.




#### Bending stiffness description. Case 3 IEJ=N IPRESS=0 {#inpmod_c_crs2_bending_stiffness_description}

This specification consists of three different input lines. 



##### Curvature {#inpmod_c_crs2_bending_stiffness_description_curvature}

~~~
CURV(1) ... CURV(N)
~~~

- `CURV(1): real`: Curvature values for which bending moment is specified $\mathrm{[1/L\]}$
- .
- .
- .
- `CURV(N): real`: To be specified in increasing order

`CURV=1/CURVATURE RADIUS`




##### Bending moment, y-axis {#inpmod_c_crs2_bending_stiffness_description_bending_y}

~~~
BMOMY(1) . . . BMOMY(N)
~~~

- `BMOMY(1): real`: Bending moment around local y-axis $\mathrm{[FL\]}$
- .
- .
- .
- `BMOMY(N): real`




##### Bending moment, z-axis {#inpmod_c_crs2_bending_stiffness_description_bending_z}

~~~
BMOMZ(1) . . . BMOMZ(N)
~~~

- `BMOMZ(1): real`: Bending moment around local z-axis $\mathrm{[FL\]}$
- .
- .
- .
- `BMOMZ(N): real`

`CURV(1), BMOMY(1)` and `BMOMZ(1)` have to be zero. 
See also the figure [Bending moment around y-axis as function of curvature](@ref Bending_moment_around_y-axis_as_function_of_curvature).




#### Bending stiffness. Case 4 IEJ=N1, IPRESS=N2 (Not implemented) {#inpmod_c_crs2_bending_stiffness_case4}

This specification consists of four different input lines.




##### Curvature {#inpmod_c_crs2_bending_stiffness_case4_curvature}
~~~
CURV(1) ... CURV(N)
~~~

- `CURV(1): real`: Curvature values for which bending moments are specified $\mathrm{[1/L\]}$
- .
- .
- .
- `CURV(N): real`: To be specified in increasing order

`CURV=1/CURVATURE RADIUS`

CURV(1) has to be zero. 
See also the figure [Bending moment around y-axis as function of curvature and pressure](@ref Bending_moment_around_y-axis_as_function_of_curvature_and_pressure).




##### Pressure  {#inpmod_c_crs2_bending_stiffness_case4_pressure}

~~~
PRESS(1) ... PRESS(N)
~~~

- `PRESS(1): real`: Pressure levels for which bending moments are specified $\mathrm{[F/L^2\]}$
- .
- .
- .
- `PRESS(N): real`:




##### Bending moment, y-axis  {#inpmod_c_crs2_bending_stiffness_case4_bending_y}

~~~
BMOMY(1,1) . . . BMOMY(N1,N2)
~~~

- `BMOMY(I,J): real`: Bending moment about local y-axis at curvature I and pressure J $\mathrm{[FL\]}$.
- .
- .
- .
- `BMOMY(N1,N2):real`:

`BMOMY(1,J), J=1, N2` have to be zero.




##### Bending moment, z-axis  {#inpmod_c_crs2_bending_stiffness_case4_bending_z}

~~~
BMOMZ(1,1) . . . BMOMZ(N1,N2)
~~~

- `BMOMZ(I,J): real`: Bending moment about local Z-axis at curvature I and pressure J $\mathrm{[FL\]}$.
- .
- .
- .
- `BMOMZ(N1,N2):real`:

`BMOMZ(1,J), J=1, N2` have to be zero.




#### Torsion stiffness {#inpmod_c_crs2_torsion_stiffness}




##### Constant torsion stiffness. Case 1 |IGT|=1  {#inpmod_c_crs2_bending_stiffness_case4_constant}

~~~
GT- GT+
~~~

- `GT-: real > 0`: Torsion stiffness (negative twist) $\mathrm{[FL^2/Radian\]}$
- `GT+: real`: D.o. for positive twist. Dummy for `IGT=1`




##### Nonlinear torsion stiffness. Case 2 |IGT|= N  {#inpmod_c_crs2_bending_stiffness_case4_nonlinear}

~~~
TMOM(1) TROT(1) . . . TMOM(N) TROT(N)
~~~

- `TMOM(1): real`: Torsion moment $\mathrm{[FL\]}$
- `TROT(1): real`: Torsion angle/length $\mathrm{[Radian/L\]}$

If `IGT` is positive `TMOM(1)` and `TROT(1)` have to be zero. `TROT` must be given in increasing order.




#### Damping specification {#inpmod_c_crs2_damping}

Identical to input for cross-section type CRS1, see data group 
[Damping specification] (@ref inpmod_c_crs1_damping_specification).



#### Hydrodynamic load type identification, One input line {#inpmod_c_crs2_load_type_hydr}

~~~
CHLOAD 
~~~

- `CHLOAD: character`: `= HYDR` - Text to identify hydrodynamic coefficients

Note: Required if non-Morison loads are to be specified


##### Load type identification for CHLOAD=HYDR, One input line {#inpmod_c_crs2_hydro_load}

~~~
CHTYPE
~~~

- `CHTYPE: character`: Type of load coefficients
    - `= NONE`: No hydrodynamic load coefficients
    - `= MORI`: Slender element hydrodynamic coefficients
    - `= MACF`: MacCamy-Fuchs with quadratic drag load coefficients
    - `= POTN`: Potential flow with quadratic drag load coefficients

Note that the option `POTN` currently is under testing. Potential flow
forces are only available for irregular time domain analysis.



##### Hydrodynamic force coefficients if CHTYPE=MORI {#inpmod_c_crs2_hydrodynamic}

~~~
CDX CDY CDZ CDTMOM AMX AMY AMZ AMTOR CDLX CDLY CDLZ SCFKN SCFKT
~~~

- `CDX: real`: Drag force coefficient for local x-direction $\mathrm{[F/((L/T)^2\times L)\]}$
- `CDY: real`: Drag force coefficient for local y-direction $\mathrm{[F/((L/T)^2\times L)\]}$
- `CDZ: real`: Drag force coefficient for local z-direction $\mathrm{[F/((L/T)^2\times L)\]}$
- `CDTMOM: real`: Drag force coefficient for local x-rotation. Not used in present version.
- `AMX: real`: Added mass per length in x-direction $\mathrm{[M/L\]}$
- `AMY: real`: Added mass per length in y-direction $\mathrm{[M/L\]}$
- `AMZ: real`: Added mass per length in z-direction $\mathrm{[M/L\]}$
- `AMTOR: real`: Added mass for local x-rotation $\mathrm{[ML^2/L\]}$ Not used in present version.
- `CDLX: real, default: 0`: Linear drag force coefficients in local x-direction $\mathrm{[F/((L/T)\times L)\]}$
- `CDLY: real, default: 0`: Linear drag force coefficients in local y-direction $\mathrm{[F/((L/T)\times L)\]}$
- `CDLZ: real, default: 0`: Linear drag force coefficients in local z-direction $\mathrm{[F/((L/T)\times L)\]}$
- `SCFKN: real, default: 1`: Scaling factor for the Froude-Krylov term in Morison’s equation in normal direction
- `SCFKT: real, default: 1`: Scaling factor for the Froude-Krylov term in Morison’s equation in 
    tangential direction. Only the values 0.0 and 1.0 are permitted.

The drag forces per unit length acting in the local coordinate system are computed as:
- $\mathrm{F_x=CDX\times VRELX\times VRELX+CDLX\times VRELX}$
- $\mathrm{F_y=CDY\times \sqrt{VRELY^2+VRELZ^2}\times VRELY+CDLY\times VRELY}$
- $\mathrm{F_z=CDZ\times \sqrt{VRELY^2+VRELZ^2}\times VRELZ+CDLZ\times VRELZ}$

where:
- $\mathrm{CDX,CDY,CDZ}$: are the input quadratic drag force coefficients in local x, y and z-directions
- $\mathrm{CDLX,CDLY,CDLZ}$: are the input linear drag force coefficients in local x, y and z-directions
- $\mathrm{VRELX,VRELY,VRELZ}$: are relative water velocities in local x, y and z-directions

The input quadratic drag force coefficients $\mathrm{CDX}$, $\mathrm{CDY}$ and $\mathrm{CDZ}$ will normally be calculated as:
- $\mathrm{CDX=\frac{1}{2}\rho S_{2D}C_{dx}}$
- $\mathrm{CDY=\frac{1}{2}\rho B_yC_{dy}}$
- $\mathrm{CDZ=\frac{1}{2}\rho B_zC_{dz}}$

where:
- $\mathrm{\rho }$: water density
- $\mathrm{S_{2D}}$: cross sectional wetted surface
- $\mathrm{B_y,B_z}$: projected area per. unit length for flow in local y and z-direction, respectively
- $\mathrm{C_{dx},C_{dy},C_{dz}}$: nondimensional drag coefficients in local x, y and z-directions, respectively

The input added mass per. unit length $\mathrm{AMX}$, $\mathrm{AMY}$ and $\mathrm{AMZ}$ can be calculated as:
- $\mathrm{AMX=\rho AC_{mx}}$
- $\mathrm{AMY=\rho AC_{my}}$
- $\mathrm{AMZ=\rho AC_{mz}}$

where:
- $\mathrm{\rho }$: water density
- $\mathrm{A}$: cross sectional area
- $\mathrm{C_{mx},C_{my},C_{mz}}$: nondimensional added mass coefficients in local x, y and z-directions, respectively


##### Hydrodynamic force coefficients if CHTYPE=MACF {#inpmod_c_crs2_hydrodynamic_macf}

MacCamy-Fuchs frequency-dependent hydrodynamic loads on a stationary
vertical circular cylinder will be applied for
`CHTYPE=MACF`. MacCamy-Fuchs forces are pre-computed based on the
element position after static calculation. MacCamy-Fuchs forces are
only available for irregular time domain analysis.

Quadratic drag may also be applied on elements with MacCamy-Fuchs
loading. McCamy Fuchs assumes that the cross-section is circular, so a
single transverse quadratic drag coefficient is given (CDZ will be set
to CDY).

~~~
CQX CQY ICODE D
~~~

- `CQX: real`: Quadratic drag coefficient in tangential direction
    - `ICODE=1: CQX=CDX`: dimensional drag force coefficient $\mathrm{[F/((L/T)^2\times L)\]}$
    - `ICODE=2: CQX=Cdt`: nondimensional drag force coefficient
- `CQY: real`: Quadratic drag coefficient in normal direction
    - `ICODE=1: CQY=CDY`: dimensional drag force coefficient $\mathrm{[F/((L/T)^2\times L)\]}$
    - `ICODE=2: CQY=Cdn`: nondimensional drag force coefficient
- `ICODE: integer`: Code for input of hydrodynamic drag coefficients
    - `ICODE=1`: Dimensional coefficients
    - `ICODE=2`: Nondimensional coefficients
- `D: real, default:`$\sqrt{\mathrm{\frac{4}{\pi }(AE)}}$: Hydrodynamic diameter of the pipe $\mathrm{[L\]}$.
    - Default value is calculated from external cross-sectional area given as input in data
      section [Mass and volume](@ref inpmod_c_crs1_mass_and_volume)
	

##### Hydrodynamic force coefficients if CHTYPE=POTN {#inpmod_c_crs2_hydrodynamic_potn}

Frequency-dependent added mass, radiation damping, and excitation forces based on the 
first order potential flow solution will be applied for `CHTYPE=POTN`.  The radiation and
diffraction coefficients are to be given by a separate input file specified under the
data group [Potential flow library specification] (@ref inpmod_b_poten_lib). 

Quadratic drag may also be applied on cross-sections with potential flow loading. 

~~~
CQX CQY CQZ ICODE D SCFKT
~~~

- `CQX: real`: Quadratic drag coefficient in local x-direction 
    - `ICODE=1: CQX=CDX`: dimensional drag force coefficient $\mathrm{[F/((L/T)^2\times L)\]}$
    - `ICODE=2: CQX=Cdt`: nondimensional drag force coefficient
- `CQY: real`: Quadratic drag coefficient in local y-direction 
    - `ICODE=1: CQY=CDY`: dimensional drag force coefficient $\mathrm{[F/((L/T)^2\times L)\]}$
    - `ICODE=2: CQY=Cdn`: nondimensional drag force coefficient
- `CQZ: real`: Quadratic drag coefficient in local z-direction 
    - `ICODE=1: CQZ=CDZ`: dimensional drag force coefficient $\mathrm{[F/((L/T)^2\times L)\]}$
    - `ICODE=2: CQZ=Cdn`: nondimensional drag force coefficient
- `ICODE: integer, default: 1`: `ICODE` Code for input of hydrodynamic force coefficients
    - `ICODE=1`: Dimensional coefficients
    - `ICODE=2`: Nondimensional coefficients
- `D: real, default:`$\sqrt{\mathrm{\frac{4}{\pi }(AE)}}$: Hydrodynamic diameter $\mathrm{[L\]}$.
    - Default value is calculated from external cross-sectional area given as input 
      in data section [Mass and volume](@ref inpmod_c_crs2_mass)
- `SCFKT: real, default: 1`: Scaling factor for the Froude-Krylov term in Morison’s equation in 
    tangential direction. Only the values 0.0 and 1.0 are permitted.




#### Aerodynamic load type identification, One optional input line {#inpmod_c_crs2_aeroloadspec_type_1}

~~~
CHLOAD
~~~

- `CHLOAD: character`: `= WIND` - Text to identify wind coefficients
- `CHTYPE: character`: Type of wind load coefficients
    - `= MORI`: Morison-like loading, Drag term 
    - `= AIRC`: Air foil cross section to be specified (Not implemented)
    - `= AIRF`: Air foil cross section, Refers to a air foil library file



#### Load type identification, One optional input line {#inpmod_c_crs2_aeroloadspec_type_2}


~~~
CHTYPE
~~~

- `CHTYPE: character`: Type of wind load coefficients
    - `= MORI`: Morison-like loading, Drag term 
    - `= AIRC`: Air foil cross section to be specified (Not implemented)
    - `= AIRF`: Air foil cross section, Refers to a air foil library file



##### CHTYPE=MORI: Morison-like aerodynamic drag, One input line {#inpmod_c_crs2_airmori}

~~~
CDXAERO CDYAERO CDZAERO 
~~~

- `CDXAERO: real`: Dimensional quadratic drag coefficient for local x-direction $\mathrm{[F/((L/T)^2\times L)\]}$
- `CDYAERO: real`: Dimensional quadratic drag coefficient for local y-direction $\mathrm{[F/((L/T)^2\times L)\]}$
- `CDZAERO: real`: Dimensional quadratic drag coefficient for local z-direction $\mathrm{[F/((L/T)^2\times L)\]}$

The drag forces per unit length acting in the local coordinate system are computed as:
- $\mathrm{F_x=CDXAERO\times VRELX\times |VRELX|}$
- $\mathrm{F_y=CDYAERO\times VRELY\times \sqrt{VRELY^2+VRELZ^2}}$
- $\mathrm{F_z=CDZAERO\times VRELZ\times \sqrt{VRELY^2+VRELZ^2}}$

where:
- $\mathrm{CDXAERO,CDYAERO,CDZAERO}$: are the input quadratic drag force coefficients in local x, y and z-directions
- $\mathrm{VRELX,VRELY,VRELZ}$: are relative wind velocities in local x, y and z-directions

The input quadratic drag force coefficients $\mathrm{CDX}$, $\mathrm{CDY}$ and $\mathrm{CDZ}$ will normally be calculated as:
- $\mathrm{CDXAERO=\frac{1}{2}\rho _{air}S_{2D}C_{dx}}$
- $\mathrm{CDYAERO=\frac{1}{2}\rho _{air}B_yC_{dy}}$
- $\mathrm{CDZAERO=\frac{1}{2}\rho _{air}B_zC_{dz}}$

where:
- $\mathrm{\rho _{air}}$: air density
- $\mathrm{S_{2D}}$: cross sectional surface area
- $\mathrm{B_y,B_z}$: projected area per. unit length for flow in local y and z-direction, respectively
- $\mathrm{C_{dx},C_{dy},C_{dz}}$: nondimensional drag coefficients in local x, y and z-directions, respectively

If the component is part of a wind turbine tower line, only the `CDY` component is used for tower
shadow computation. 



##### CHTYPE=AIRF: Coefficients on file. ID and chord length, One input line {#inpmod_c_crs2_coefficients}

~~~
CHCOEF CHORDL YFC ZFC ROTFAX
~~~

- `CHCOEF: character`: Air foil coefficient identifier. Must be found on the air foil library file
- `CHORDL: real`: Chord length of foil section. $\mathrm{[L\]}$
    - It is used to scale the air foil load coefficients.
- `YFC: real, default: 0`: Y-coordinate of foil origin $\mathrm{[L\]}$
- `ZFC: real, default: 0`: Z-coordinate of foil origin $\mathrm{[L\]}$
- `ROTFAX: real, default: 0`: Inclination of foil system $\mathrm{[deg\]}$

The blade coordinate system and origin coincides with the elastic (local) $\mathrm{(X_L,Y_L,Z_L)}$  coordinate system. 
The aerodynamic coordinate system $\mathrm{(X_{AF},Y_{AF})}$ is located at (YFC,ZFC) referred to the local coordinate system, 
and is rotated about the blade x axis by the angle ROTFAX, as indicated in the figure below. The  $\mathrm{X_L}$ axis is 
pointing into the paper plane, while the  $\mathrm{Z_{AF}}$ is pointing out of plane. Note that the air foil coefficients 
has to be referred to the aerodynamic coordinate system as indicated by the corresponding angle of attack in the figure. For airfoil 
elements that are part of a wind turbine blade, the local $\mathrm{X_L}$-axis is pointing towards the blade tip.


Note that suppliers of wind turbine blades normally give the foil twist relative to the the areodynamic 
coordinate system, i.e. as twist around the $\mathrm{Z_{AF}}$ -axis.

![Definition of foil center and inclination of foil system in the local cross section (strength) system.](@ref figures/riflex_um_foil.svg)
@image latex figures/riflex_um_foil.pdf "Definition of foil center and inclination of foil system in the local cross section (strength) system." width =15cm


In coupled analysis, a `SIMO` wind type with `IWITYP >= 10` must be
used if the case contains elements with wind force coefficients that
are not on the blades of a wind turbine.



#### Capacity parameter {#inpmod_c_crs2_capacity}

~~~
TB YCURMX ZCURMX
~~~

- `TB: real`: Tension capacity $\mathrm{[F\]}$
- `YCYRMX: real`: Maximum curvature around local y-axis $\mathrm{[1/L\]}$
- `ZCURMX: real`: Maximum curvature around local z-axis $\mathrm{[1/L\]}$

These parameters are dummy in the present version











###  CRS7 - General cross section {#inpmod_c_crs7_cross_section}




#### Data group identifier {#inpmod_c_crs7_data}

~~~
NEW COMPonent CRS7
~~~




#### Component type identifier {#inpmod_c_crs7_component}

~~~
CMPTYP-ID TEMP ALFA
~~~

- `CMPTYP-ID: character(8)`: Component type identifier
- `TEMP : real`: Temperature at which the specification applies 
    - Dummy in present version
- `ALPHA: real`: Thermal expansion coefficient $\mathrm{[Temp^{-1}\]}$
	- Dummy in present version


\anchor gen_nonsym_crossec	
![General cross-section](@ref figures/CRS7_allecc.svg)
@image latex figures/CRS7_allecc.pdf "General cross-section" width=12cm





#### Mass {#inpmod_c_crs7_mass}

~~~
YECC_MASS ZECC_MASS
~~~

- `YECC_MASS: real`: Mass center coordinate $\mathrm{Y_m}$ in beam element system $\mathrm{[L\]}$
- `ZECC_MASS: real`: Mass center coordinate $\mathrm{Z_m}$ in beam element system $\mathrm{[L\]}$


~~~
AMS RGYR
~~~

- `AMS : real`: Mass per unit length $\mathrm{[M/L\]}$
- `RGYR: real`: Radius of gyration about mass center $\mathrm{(Y_m,Z_m)}$ $\mathrm{[L\]}$





#### Buoyancy {#inpmod_c_crs7_buoyancy}

~~~
YECC_BUOY ZECC_BUOY
~~~

- `YECC_BUOY: real`: Buoyancy center Y-coordinate in beam element system $\mathrm{[L\]}$
	- Dummy in present version. Bouyancy center set equal to mass center.
- `ZECC_BUOY: real`: Buoyancy center Z-coordinate in beam element system $\mathrm{[L\]}$
	- Dummy in present version. Bouyancy center set equal to mass center.


~~~
AE AI
~~~

- `AE: real`: External cross-sectional area $\mathrm{[L^2\]}$
	- Basis for calculation of buoyancy
- `AI: real`: Internal cross-sectional area $\mathrm{[L^2\]}$
	- Dummy in present version







#### Stiffness properties {#inpmod_c_crs7_stiffness_properties}


Only constant stiffness properties are allowed.




#### Area center and principal axes {#inpmod_c_crs7_areacent_princaxes}

The area center is the cross-section point where the axial force acts through. The principal axes are formally determined 
from the requirement $\int_AV\,W\,\,\mathrm{d}A=0$, where $\mathrm{V}$ and $\mathrm{W}$ denote the principal coordinates 
and $\mathrm{A}$ is the cross-section area. The orientation of the principal axes is defined in terms of a positive X-rotation 
$\mathrm{\theta}$ relative to the beam element YZ-coordinate system as shown in the figure [General cross-section](@ref gen_nonsym_crossec)
~~~
YECC_AREACENT ZECC_AREACENT THETA
~~~

- `YECC_AREACENT: real`: Area center coordinate $\mathrm{Y_a}$ in beam element system $\mathrm{[L\]}$
- `ZECC_AREACENT: real`: Area center coordinate $\mathrm{Z_a}$ in beam element system $\mathrm{[L\]}$
- `THETA: real`: Orientation $\mathrm{\theta}$ of principal axes V and W [deg.]. See figure [General cross-section](@ref gen_nonsym_crossec).



#### Shear center {#inpmod_c_crs7_shearcent_princaxes}

The shear center represents the attack point of the shear forces.


~~~
YECC_SHEARCENT ZECC_SHEARCENT
~~~

- `YECC_SHEARCENT: real`: Shear center coordinate $\mathrm{Y_s}$ in beam element system $\mathrm{[L\]}$
- `ZECC_SHEARCENT: real`: Shear center coordinate $\mathrm{Z_s}$ in beam element system $\mathrm{[L\]}$




#### Axial stiffness {#inpmod_c_crs7_axial_stiffness}

~~~
EA
~~~

- `EA: real > 0`: Axial stiffness $\mathrm{[F\]}$





#### Bending stiffness {#inpmod_c_crs7_bending_stiffnesses}

The bending stiffness refers to the principal axes V and W, see figure [General cross-section](@ref gen_nonsym_crossec).

~~~
EJV EJW
~~~

- `EJV: real > 0`: Bending stiffness about principal V-axis $\mathrm{[FL^2\]}$
- `EJW: real > 0`: Bending stiffness about principal W-axis $\mathrm{[FL^2\]}$





#### Shear stiffness {#inpmod_c_crs7_shear_stiffness}

The shear stiffness refers to the principal axes V and W, see figure [General cross-section](@ref gen_nonsym_crossec).


~~~
GAsW GAsV
~~~

- `GAsW: real`: Shear stiffness in principal W-direction $\mathrm{[F\]}$
- `GAsV: real`: Shear stiffness in principal V-direction $\mathrm{[F\]}$

The shear stiffness, `GAsW` and `GAsV`, are optional input parameters. 

Specified `GAsW>0` and `GAsV>0` will include shear deformation.








#### Torsion stiffness {#inpmod_c_crs7_torsion_stiffness}


~~~
GT
~~~

- `GT: real > 0`: Torsion stiffness $\mathrm{[FL^2/Radian\]}$

For a circular cross-section the torsion stiffness is given by the polar moment of inertia. Note that this is not the case for non-circular cross-sections.




#### Bending-torsion geometric coupling {#inpmod_c_crs7_bendtors}

This data group is optional. 

~~~
BTGC
~~~

- `BTGC: character(4)`: bending-torsion coupling identifier. 

If the `BTGC` identifier is present, geometric coupling between torsion and bending is accounted for. 







#### Damping specification {#inpmod_c_crs7_damping}

Identical to input for cross-section type CRS1, see data group 
[Damping specification] (@ref inpmod_c_crs1_damping_specification).

The stiffness matrix used as basis for the Rayleigh damping includes
only the material stiffness matrix. The geometric stiffness matrix is
not included as this would introduce damping of the rigid body motion
for CRS7.






#### Hydrodynamic load type identification, One input line {#inpmod_c_crs7_load_type_hydr}

~~~
CHLOAD 
~~~

- `CHLOAD: character`: `= HYDR` - Text to identify hydrodynamic coefficients

Note: Required if non-Morison loads are to be specified




##### Load type identification for CHLOAD=HYDR, One input line {#inpmod_c_crs7_hydro_load}

~~~
CHTYPE
~~~

- `CHTYPE: character`: Type of load coefficients
   - `= NONE`: No hydrodynamic load coefficients
   - `= MORI`: Slender element hydrodynamic coefficients





##### Hydrodynamic force coefficients if CHTYPE=MORI {#inpmod_c_crs7_hydrodynamic}

~~~
CDX CDY CDZ CDTMOM AMX AMY AMZ AMTOR CDLX CDLY CDLZ SCFKN SCFKT
~~~

- `CDX: real`: Drag force coefficient for local x-direction $\mathrm{[F/((L/T)^2\times L)\]}$
- `CDY: real`: Drag force coefficient for local y-direction $\mathrm{[F/((L/T)^2\times L)\]}$
- `CDZ: real`: Drag force coefficient for local z-direction $\mathrm{[F/((L/T)^2\times L)\]}$
- `CDTMOM: real`: Drag force coefficient for local x-rotation. Not used in present version.
- `AMX: real`: Added mass per length in x-direction $\mathrm{[M/L\]}$
- `AMY: real`: Added mass per length in y-direction $\mathrm{[M/L\]}$
- `AMZ: real`: Added mass per length in z-direction $\mathrm{[M/L\]}$
- `AMTOR: real`: Added mass for local x-rotation $\mathrm{[ML^2/L\]}$
- `CDLX: real, default: 0`: Linear drag force coefficients in local x-direction $\mathrm{[F/((L/T)\times L)\]}$
- `CDLY: real, default: 0`: Linear drag force coefficients in local y-direction $\mathrm{[F/((L/T)\times L)\]}$
- `CDLZ: real, default: 0`: Linear drag force coefficients in local z-direction $\mathrm{[F/((L/T)\times L)\]}$
- `SCFKN: real, default: 1`: Scaling factor for the Froude-Krylov term in Morison’s equation in normal direction
- `SCFKT: real, default: 1`: Scaling factor for the Froude-Krylov term in Morison’s equation in 
    tangential direction. Only the values 0.0 and 1.0 are permitted.

The drag forces per unit length acting in the local coordinate system are computed as:
- $\mathrm{F_x=CDX\times VRELX\times VRELX+CDLX\times VRELX}$
- $\mathrm{F_y=CDY\times VRELY\times VRELY+CDLY\times VRELY}$
- $\mathrm{F_z=CDZ\times VRELZ\times VRELZ+CDLZ\times VRELZ}$

where:
- $\mathrm{CDX,CDY,CDZ}$: are the input quadratic drag force coefficients in local x, y and z-directions
- $\mathrm{CDLX,CDLY,CDLZ}$: are the input linear drag force coefficients in local x, y and z-directions
- $\mathrm{VRELX,VRELY,VRELZ}$: are relative water velocities in local x, y and z-directions

The input quadratic drag force coefficients $\mathrm{CDX}$, $\mathrm{CDY}$ and $\mathrm{CDZ}$ will normally be calculated as:
- $\mathrm{CDX=\frac{1}{2}\rho S_{2D}C_{dx}}$
- $\mathrm{CDY=\frac{1}{2}\rho B_yC_{dy}}$
- $\mathrm{CDZ=\frac{1}{2}\rho B_zC_{dz}}$

where:
- $\mathrm{\rho }$: water density
- $\mathrm{S_{2D}}$: cross sectional wetted surface
- $\mathrm{B_y,B_z}$: projected area per. unit length for flow in local y and z-direction, respectively
- $\mathrm{C_{dx},C_{dy},C_{dz}}$: nondimensional drag coefficients in local x, y and z-directions, respectively

The input added mass per. unit length $\mathrm{AMX}$, $\mathrm{AMY}$ and $\mathrm{AMZ}$ can be calculated as:
- $\mathrm{AMX=\rho AC_{mx}}$
- $\mathrm{AMY=\rho AC_{my}}$
- $\mathrm{AMZ=\rho AC_{mz}}$

where:
- $\mathrm{\rho }$: water density
- $\mathrm{A}$: cross sectional area
- $\mathrm{C_{mx},C_{my},C_{mz}}$: nondimensional added mass coefficients in local x, y and z-directions, respectively






#### Aerodynamic load type identification, One optional input line {#inpmod_c_crs7_aeroloadspec_type}

~~~
CHLOAD
~~~

- `CHLOAD: character`: `= WIND` - Text to identify wind coefficients



#### Load type identification, One optional input line {#inpmod_c_crs7_aeroload_type}


~~~
CHTYPE
~~~

- `CHTYPE: character`: Type of wind load coefficients
    - `= MORI`: Morison-like loading, Drag term 
    - `= AIRC`: Air foil cross section to be specified (Not implemented)
    - `= AIRF`: Air foil cross section, Refers to a air foil library file





##### CHTYPE=MORI: Morison-like aerodynamic drag, One input line {#inpmod_c_crs7_airmori}

~~~
CDXAERO CDYAERO CDZAERO 
~~~

- `CDXAERO: real`: Dimensional quadratic drag coefficient for local x-direction $\mathrm{[F/((L/T)^2\times L)\]}$
- `CDYAERO: real`: Dimensional quadratic drag coefficient for local y-direction $\mathrm{[F/((L/T)^2\times L)\]}$
- `CDZAERO: real`: Dimensional quadratic drag coefficient for local z-direction $\mathrm{[F/((L/T)^2\times L)\]}$

The drag forces per unit length acting in the local coordinate system are computed as:
- $\mathrm{F_x=CDXAERO\times VRELX\times |VRELX|}$
- $\mathrm{F_y=CDYAERO\times VRELY\times \sqrt{VRELY^2+VRELZ^2}}$
- $\mathrm{F_z=CDZAERO\times VRELZ\times \sqrt{VRELY^2+VRELZ^2}}$

where:
- $\mathrm{CDXAERO,CDYAERO,CDZAERO}$: are the input quadratic drag force coefficients in local x, y and z-directions
- $\mathrm{VRELX,VRELY,VRELZ}$: are relative wind velocities in local x, y and z-directions

The input quadratic drag force coefficients $\mathrm{CDX}$, $\mathrm{CDY}$ and $\mathrm{CDZ}$ will normally be calculated as:
- $\mathrm{CDXAERO=\frac{1}{2}\rho _{air}S_{2D}C_{dx}}$
- $\mathrm{CDYAERO=\frac{1}{2}\rho _{air}B_yC_{dy}}$
- $\mathrm{CDZAERO=\frac{1}{2}\rho _{air}B_zC_{dz}}$

where:
- $\mathrm{\rho _{air}}$: air density
- $\mathrm{S_{2D}}$: cross sectional surface area
- $\mathrm{B_y,B_z}$: projected area per. unit length for flow in local y and z-direction, respectively
- $\mathrm{C_{dx},C_{dy},C_{dz}}$: nondimensional drag coefficients in local x, y and z-directions, respectively

If the component is part of a wind turbine tower line, only the `CDY` component is used for tower
shadow computation. 



##### CHTYPE=AIRF: Coefficients on file. ID and chord length, One input line {#inpmod_c_crs7_coefficients}

~~~
CHCOEF CHORDL YFC ZFC ROTFAX
~~~

- `CHCOEF: character`: Air foil coefficient identifier. Must be found on the air foil library file
- `CHORDL: real`: Chord length of foil section. $\mathrm{[L\]}$
    - It is used to scale the air foil load coefficients.
- `YFC: real, default: 0`: Y-coordinate of foil origin $\mathrm{[L\]}$
- `ZFC: real, default: 0`: Z-coordinate of foil origin $\mathrm{[L\]}$
- `ROTFAX: real, default: 0`: Inclination of foil system $\mathrm{[deg\]}$

The blade coordinate system and origin coincides with the elastic (local) $\mathrm{(X_L,Y_L,Z_L)}$  coordinate system. 
The aerodynamic coordinate system $\mathrm{(X_{AF},Y_{AF})}$ is located at (YFC,ZFC) referred to the local coordinate system, 
and is rotated about the blade x axis by the angle ROTFAX, as indicated in the figure below. The  $\mathrm{X_L}$ axis is 
pointing into the paper plane, while the  $\mathrm{Z_{AF}}$ is pointing out of plane. Note that the air foil coefficients 
has to be referred to the aerodynamic coordinate system as indicated by the corresponding angle of attack in the figure. For airfoil 
elements that are part of a wind turbine blade, the local $\mathrm{X_L}$-axis is pointing towards the blade tip.


Note that suppliers of wind turbine blades normally give the foil twist relative to the the areodynamic 
coordinate system, i.e. as twist around the $\mathrm{Z_{AF}}$ -axis.

![Definition of foil center and inclination of foil system in the local cross section (strength) system.](@ref figures/riflex_um_foil.svg)
@image latex figures/riflex_um_foil.pdf "Definition of foil center and inclination of foil system in the local cross section (strength) system." width =15cm


In coupled analysis, a `SIMO` wind type with `IWITYP >= 10` must be
used if the case contains elements with wind force coefficients that
are not on the blades of a wind turbine.





#### Capacity parameter {#inpmod_c_crs7_capacity}

~~~
TB YCURMX ZCURMX
~~~

- `TB: real`: Tension capacity $\mathrm{[F\]}$
- `YCYRMX: real`: Maximum curvature around local y-axis $\mathrm{[1/L\]}$
- `ZCURMX: real`: Maximum curvature around local z-axis $\mathrm{[1/L\]}$

These parameters are dummy in the present version











###  BODY - Description of attached bodies {#inpmod_c_body}




#### Data group identifier {#inpmod_c_body_data}

~~~
NEW COMPonent BODY
~~~




#### Component type identifier {#inpmod_c_body_component}

~~~
CMPTYP-ID
~~~

- `CMPTYP-ID: character(8)`: Component type identifier

A body is a component that may be attached at supernodes and segment interconnection points. The following
essential properties should be observed:
- The `BODY` is directly attached to a nodal point and has no motion degrees of freedom by itself.
- The `BODY` component serves to add concentrated masses (inertia force), weight or buoyancy forces to the system.




#### Mass and volume {#inpmod_c_body_mass}

~~~
AM AE
~~~

- `AM: real`: Mass $\mathrm{[M\]}$
- `AE: real`: Displacement volume $\mathrm{[L^3\]}$




#### Hydrodynamic coefficients {#inpmod_c_body_hydrodynamic}

~~~
ICOO CDX CDY CDZ AMX AMY AMZ
~~~

- `ICOO: character(5)`: Coordinate system code
    - `ICOO=GLOBAL`: Coefficients refer to global coordinate system
    - `ICOO=LOCAL`: Coefficients refer to local coordinate system of neighbour elements in the actual line
- `CDX: real`: Drag force coefficient in X-direction $\mathrm{[F/(L/T)^2)\]}$
- `CDY: real`: Drag force coefficient in Y-direction $\mathrm{[F/(L/T)^2)\]}$
- `CDZ: real`: Drag force coefficient in Z-direction $\mathrm{[F/(L/T)^2)\]}$
- `AMX: real`: Added mass in X-direction $\mathrm{[M\]}$
- `AMY: real`: Added mass in Y-direction $\mathrm{[M\]}$
- `AMZ: real`: Added mass in Z-direction $\mathrm{[M\]}$

The drag forces acting in the global/local coordinate system are computed as:
- $\mathrm{F_x=CDX\times VRELX\times VRELX}$
- $\mathrm{F_y=CDY\times VRELY\times VRELY}$
- $\mathrm{F_z=CDZ\times VRELZ\times VRELZ}$

where:
- $\mathrm{CDX,CDY,CDZ}$: are the input drag force coefficients in global/local x, y and z-directions, respectively
- $\mathrm{VRELX,VRELY,VRELZ}$: are relative water velocities in global/local x, y and z-directions respectively

The input quadratic drag force coefficients $\mathrm{CDX}$, $\mathrm{CDY}$ and $\mathrm{CDZ}$ will normally be calculated as:
- $\mathrm{CDX=\frac{1}{2}\rho B_xC_{dx}}$
- $\mathrm{CDY=\frac{1}{2}\rho B_yC_{dy}}$
- $\mathrm{CDZ=\frac{1}{2}\rho B_zC_{dz}}$

where:
- $\mathrm{\rho }$: water density
- $\mathrm{B_x,B_y,B_z}$: projected area for flow in global/local y and z-direction
- $\mathrm{C_{dx},C_{dy},C_{dz}}$: nondimensional drag coefficients in global/local x, y and z-directions




###  CONB - Description of ball joint connectors {#inpmod_c_CONB}

This component can be used to model balljoint, hinges and universal joints. The component has zero length,
and adds 6 degrees of freedom to the system model. The forces due to mass and weight are assumed to act at 
the nodal point at which the component is specified. Note that this component can
not be used in branch lines in standard systems, or in combination with bar elements. 
Should also be used with care at supernodes with user defined boundary conditions for rotations in `AR`
system to avoid singularities in the `FEM` solution procedure.




#### Data group identifier {#inpmod_c_CONB_data}

~~~
NEW COMPonent CONB
~~~




#### Component type identifier {#inpmod_c_CONB_component}

~~~
CMPTYP-ID
~~~

- `CMPTYP-ID: character(8)`: Component type identifier




#### Mass and volume {#inpmod_c_CONB_mass}

~~~
AM AE
~~~

- `AM: real`: Mass $\mathrm{[M\]}$
- `AE: real`: Displacement volume $\mathrm{[L^3\]}$




#### Hydrodynamic coefficients {#inpmod_c_CONB_hydrodynamic}

~~~
ICOO CDX CDY CDZ AMX AMY AMZ
~~~

- `ICOO: character`: Coordinate system code
    - `ICOO=GLOBAL`: Coefficients refer to global coordinate system
    - `ICOO=LOCAL`: Coefficients refer to local coordinate system of neighbour elements in the actual line
- `CDX: real`: Drag force coefficient in X-direction $\mathrm{[F/(L/T)^2)\]}$
- `CDY: real`: Drag force coefficient in Y-direction $\mathrm{[F/(L/T)^2)\]}$
- `CDZ: real`: Drag force coefficient in Z-direction $\mathrm{[F/(L/T)^2)\]}$
- `AMX: real`: Added mass in X-direction $\mathrm{[M\]}$
- `AMY: real`: Added mass in Y-direction $\mathrm{[M\]}$
- `AMZ: real`: Added mass in Z-direction $\mathrm{[M\]}$

The drag forces acting in the global/local coordinate system are computed as:
- $\mathrm{F_x=CDX\times VRELX\times VRELX}$
- $\mathrm{F_y=CDY\times VRELY\times VRELY}$
- $\mathrm{F_z=CDZ\times VRELZ\times VRELZ}$

where:
- $\mathrm{CDX,CDY,CDZ}$: are the input drag force coefficients in global/local x, y and z-directions, respectively
- $\mathrm{VRELX,VRELY,VRELZ}$: are relative water velocities in global/local x, y and z-directions respectively

The input quadratic drag force coefficients $\mathrm{CDX}$, $\mathrm{CDY}$ and $\mathrm{CDZ}$ will normally be calculated as:
- $\mathrm{CDX=\frac{1}{2}\rho B_xC_{dx}}$
- $\mathrm{CDY=\frac{1}{2}\rho B_yC_{dy}}$
- $\mathrm{CDZ=\frac{1}{2}\rho B_zC_{dz}}$

where:
- $\mathrm{\rho }$: water density
- $\mathrm{B_x,B_y,B_z}$: projected area per. unit lengt for flow in global/local y and z-directions, respectively
- $\mathrm{C_{dx},C_{dy},C_{dz}}$: nondimensional drag coefficients in global/local x, y and z-directions, respectively




#### Degrees of freedom {#inpmod_c_CONB_degrees}

~~~
IRX IRY IRZ
~~~

- `IRX: integer, default: 0`: Rotation freedom code, x-axis
- `IRY: integer, default: 0`: Rotation freedom code, y-axis
- `IRZ: integer, default: 0`: Rotation freedom code, z-axis
    - `1` - Fixed (no deformation)
    - `0` - Free (zero moment)

x-, y- and z-axes refer to local coordinate system of the neighbour element in the line where the ball
joint is specified.

\anchor Rotation_freedom_for_a_ball_joint_component
![Rotation freedom for a ball joint component](@ref figures/um_ii_fig114.svg)
@image latex figures/um_ii_fig114.pdf "Rotation freedom for a ball joint component" width=12cm




###  FLEX - Description of flex-joint connectors {#inpmod_c_FLEX}
This component can be used to model ball joints, hinges and universal joints with specified rotational
stiffness. It will introduce one extra element with zero length at the segment end to which it is attached, 
and add 6 degrees of freedom to the system model. The translation dofs of
freedom are suppressed by use of linear constraint equations. Note that this component can not be used in branch 
lines in standard systems, or in combination with bar elements. It should
also be used with care at supernodes with user defined boundary conditions for rotations in `AR` system to avoid singularities in the `FEM` solution procedure.

In present version, flex-joint connectors may only be used for nonlinear static and dynamic analysis.




#### Data group identifier {#inpmod_c_FLEX_data}

~~~
NEW COMPonent FLEX
~~~




#### Component type identifier {#inpmod_c_FLEX_component}

~~~
CMPTYP-ID
~~~

- `CMPTYP-ID: character(8)`: Component type identifier




#### Mass and volume {#inpmod_c_FLEX_mass}

~~~
AM AE RGX RGY RGZ CRX CRY CRZ
~~~

- `AM: real, default: 0`: Mass $\mathrm{[M\]}$
- `AE: real, default: 0`: Displacement volume $\mathrm{[L^3\]}$
- `RGX: real, default: 0`: Radius of gyration around local x-axis $\mathrm{[L\]}$
- `RGY: real, default: 0`: Radius of gyration around local y-axis $\mathrm{[L\]}$
- `RGZ: real, default: 0`: Radius of gyration around local z-axis $\mathrm{[L\]}$
- `CRX: real, default: 0`: Damping coeff. Rotational velocity around local x-axis $\mathrm{[FLT/deg\]}$
- `CRY: real, default: 0`: Damping coeff. Rotational velocity around local y-axis $\mathrm{[FLT/deg\]}$
- `CRZ: real, default: 0`: Damping coeff. Rotational velocity around local z-axis $\mathrm{[FLT/deg\]}$




#### Hydrodynamic coefficients {#inpmod_c_FLEX_hydrodynamic}

~~~
CDX CDY CDZ AMX AMY AMZ AMXROT AMYROT AMZROT
~~~

- `CDX: real, default: 0`: Drag coeff. in local x-direction $\mathrm{[F/(L/T)^2)\]}$
- `CDY: real, default: 0`: Drag coeff. in local y-direction $\mathrm{[F/(L/T)^2)\]}$
- `CDZ: real, default: 0`: Drag coeff. in local z-direction $\mathrm{[F/(L/T)^2)\]}$
- `AMX: real, default: 0`: Added mass in local x-direction $\mathrm{[M\]}$
- `AMY: real, default: 0`: Added mass in local y-direction $\mathrm{[M\]}$
- `AMZ: real, default: 0`: Added mass in local z-direction $\mathrm{[M\]}$
- `AMXROT: real, default: 0`: Added mass rotation around local x-direction $\mathrm{[FL\times T^2\]}$
- `AMYROT: real, default: 0`: Added mass rotation around local y-direction $\mathrm{[FL\times T^2\]}$
- `AMZROT: real, default: 0`: Added mass rotation around local z-direction $\mathrm{[FL\times T^2\]}$

The tangential drag force, the force acting in local x-axis, is computed by:

$\mathrm{FX=CDX\times VRELX\times |VRELX|}$

The drag force acting normal to the local x-direction, is assumed to act in the same direction as the relative 
velocity transverse component and are computed according to:
- $\mathrm{FY=CDY\times \sqrt{VRELY^2+VRELZ^2}\times VRELY}$
- $\mathrm{FZ=CDY\times \sqrt{VRELY^2+VRELZ^2}\times VRELZ}$




#### Stiffness properties classification {#inpmod_c_FLEX_stiffness_properties}

~~~
IDOF IBOUND RAYDMP
~~~

- `IDOF: character(4)`: Degree of freedom
    - `IDOF = IRX`: Rotation around local x-axis
    - `IDOF = IRY`: Rotation around local y-axis
    - `IDOF = IRZ`: Rotation around local z-axis
    - `IDOF = IRYZ`: Rotation around bending axis
- `IBOUND: integer`: Constraint
    - `IBOUND = -1`: Fixed (Legal if 2 of 3 dofs are fixed)
    - `IBOUND = 0`: Free. Not available with `IDOF = IRYZ`
    - `IBOUND = 1`: Constant stiffness
    - `IBOUND > 1`: Table with `IBOUND` pairs of moment - rotational angle to be specified
- `RAYDMP: real`: Stiffness proportional damping coefficient

3 or 2 input lines to be specified: `IRX, IRY, IRZ` or `IRX, IRYZ`

x, y and z-axes refer to the local coordinate system of the element to which the flex joint
is attached. This is similar to the ball joint connector as illustrated in the figure 
[Rotation freedom for a ball joint component](@ref Rotation_freedom_for_a_ball_joint_component).

              


#### Stiffness data {#inpmod_c_FLEX_stiffness_data}

Stiffness data are to be given in the sequence `IRX, IRY` and `IRZ` or `IRX` and `IRYZ`. Stiffness data are to
be omitted for `IBOUND <= 0`




##### Linear stiffness {#inpmod_c_FLEX_stiffness_data_linear}

`IBOUND = 1`, One input line
~~~
STIFF
~~~

- `STIFF: real`: stiffness with respect to rotation $\mathrm{[FL/deg\]}$




##### Nonlinear stiffness; IBOUND > 1 {#inpmod_c_FLEX_stiffness_data_nonlinear}

`IBOUND > 1`, IBOUND input lines
~~~
MOMENT ANGLE
~~~

- `MOMENT: real`: Moment corresponding to rotational angle $\mathrm{[FL\]}$
- `ANGLE: real`: Rotational angle $\mathrm{[deg\]}$

`MOMENT` and `ANGLE` must be given in increasing order. Linear extrapolation will be used
outside the specified range of values.

For dofs `IRX, IRY` and `IRZ`, both negative and positive values should be given.

For dof `IRYZ`, `MOMENT` and `ANGLE` have to be greater or equal to zero. To avoid convergence
problems, the first pair should be 0.0, 0.0.




###  FLUID - Specification of internal fluid flow {#inpmod_c_fluid}




#### Data group identifier {#inpmod_c_fluid_data}

~~~
NEW COMPonent FLUId
~~~




#### Component type number {#inpmod_c_fluid_component}

~~~
CMPTYP-ID
~~~

- `CMPTYP-ID: character(8)`: Component type identifier




#### Fluid flow characteristics {#inpmod_c_fluid_fluid_flow}

~~~
RHOI VVELI PRESSI DPRESS IDIR
~~~

- `RHOI: real`: Density $[\mathrm{M/L^3}\]$
- `VVELI: real`: Volume velocity $[\mathrm{L^3/T}\]$
- `PRESSI: real`: Pressure at fluid inlet end $[\mathrm{F/L^2}\]$
- `DPRESS: real`: Pressure drop $[\mathrm{F/L^3}\]$
- `IDIR: integer, default: 1`: Flow direction code
    - 1: Inlet at supernode end 1 of the line
    - 2: Inlet at supernode end 2 of the line

The pressure drop is assumed to be uniform over the line length. For further clarification of
pressure definition, confer Theory Manual.

In this version only `RHOI` is used to calculate weight and mass for static
and dynamic analysis.
The other parameters are used for calculating wall force (flange force) only
depending on output option (`OUTMOD`)




###  EXT1 - External wrapping {#inpmod_c_ext1}

This component can be used to model additional weight or buoyancy modules attached to a riser line. The
specified additional weight and buoyancy are used to adjust the average properties of the segment.




#### Data group identifier {#inpmod_c_ext1_data}

~~~
NEW COMPonent EXT1
~~~




#### Component type identifier {#inpmod_c_ext1_component}

~~~
CMPTYP-ID
~~~

- `CMPTYP-ID: character(8)`: Component type identifier




#### Mass and volume {#inpmod_c_ext1_mass}

~~~
AMS AE RGYR FRAC
~~~

- `AMS: real`: Mass per unit length $\mathrm{[M/L\]}$
- `AE: real`: Buoyancy volume/length $\mathrm{[L^2\]}$
- `RGYR: real`: Radius of gyration around local x-axis $\mathrm{[L\]}$
- `FRAC: real`: Fraction of the segment that is covered $\mathrm{[1\]}$
    - `0 <= FRAC <= 1`

The resulting properties of the segment with external wrapping are:

Mass / length:
- $\mathrm{AMS_{res}=AMS_{cs}+AMS_{ext}\times FRAC}$

Resulting radius of gyration:
- $\mathrm{RGYR_{res}=(AMS_{cs}\times RGYR_{cs}^2+AMS_{ext}\times RGYR_{ext}^2\times FRAC)/(AMS_{cs}+AMS_{ext}\times FRAC)}$

Resulting external area for buoyancy:
- $\mathrm{AE_{res}=AE_{cs}+AE_{ext}\times FRAC}$

Where:
- cs denotes the original cross section properties; i.e. without wrapping.
- ext denotes the properties of the wrapping given in this data group.
- res denotes the resulting average segment properties

![Description of external wrapping](@ref figures/um_ii_fig121.svg)
@image latex figures/um_ii_fig121.pdf "Description of external wrapping" width=12cm




#### Hydrodynamic coefficients {#inpmod_c_ext1_hydrodynamic}

~~~
CDX CDY AMX AMY CDLX CDLY
~~~

- `CDX: real`: Drag force coefficient in tangential direction $\mathrm{[F/((L/T)^2\times L)\]}$
- `CDY: real`: Drag force coefficient in normal direction $\mathrm{[F/((L/T)^2\times L)\]}$
- `AMX: real`: Added mass per length in tangential direction $\mathrm{[M/L\]}$
- `AMY: real`: Added mass per length in normal direction $\mathrm{[M/L\]}$
- `CDLX: real, default: 0`: Linear drag force coefficients in tangential direction $\mathrm{[F/((L/T)\times L)\]}$
- `CDLY: real, default: 0`: Linear drag force coefficients in normal direction $\mathrm{[F/((L/T)\times L)\]}$

The coefficients specified for the external wrapping are added directly to the coefficients specified
for the pipe.

The drag forces per unit length acting in the local x-direction is computed as:
- $\mathrm{F_x=(CDX_R+FRAC\times CDX)VRELX\times VRELX+(CDLX_R+FRAC\times CDLX)VRELX}$

In the case of an axis symmetric cross section the drag force per unit length, $\mathrm{F_n}$, acting normal to
the local x-axis is computed by assuming that the instantaneous drag force direction is parallel to
the instantaneous transverse relative velocity component
- $\begin{array}{l}\mathrm{F_n=(CDY_R+FRAC\times CDY)(VRELY^2+VRELZ^2)}\\+\mathrm{(CDLY_R+FRAC\times CDLY)\sqrt{VRELY^2+VREZ^2}}\end{array}$

In the case of a cross section with 2 symmetry planes the drag force per unit length in the local y
and z directions are computed as:
- $\mathrm{F_y=(CDY_R+FRAC\times CDY)VRELY\times VRELY+(CDLY_R+FRAC\times CDLY)VRELY}$
- $\mathrm{F_z=(CDZ_R+FRAC\times CDZ)VRELZ\times VRELZ+(CDLZ_R+FRAC\times CDLZ)VRELZ}$

Where:
- $\mathrm{CDX_R,CDY_R,CDZ_R}$: are the input quadratic drag force coefficients of the
    riser in local x,y and z-directions
- $\mathrm{CDLX_R,CDLY_R,CDLZ_R}$: are the input linear drag force coefficient of the riser
    in local x,y and z-directions
- $\mathrm{CDX,CDY}$: are the input quadratic drag force coefficients of the
    external wrapping in local x and y-directions
- $\mathrm{CDLX,CDLY}$: are the input linear drag force coefficients of the
    external wrapping in local x and y-directions
- $\mathrm{VRELX,VRELY,VRELZ}$: are relative water velocities in local x, y and
    z-directions

For an axis symmetric pipe with external wrapping the input drag force coefficient in normal direction can be calculated as:
- $\mathrm{CDY=\frac{1}{2}\rho (DC_{dn}-D_RC_{dnR})}$

The added mass per unit length in normal direction can be calculated as:
- $\mathrm{AMY=\rho \frac{\pi }{4}(D^2C_{mn}-D_R^2C_{mnR})}$

where:
- $\mathrm{\rho }$: water density
- $\mathrm{D}$: outer diameter of the external wrapping
- $\mathrm{D_R}$: outer diameter of the pipe
- $\mathrm{C_{dn}}$: normal drag coefficient
- $\mathrm{C_{dnR}}$: normal drag coefficient of the pipe
- $\mathrm{C_{mn}}$: normal added mass coefficient of the external wrapping
- $\mathrm{C_{mnR}}$: normal added mass coefficient of the pipe




###  CRS3 - Partly submerged axisymmetric cross section {#inpmod_c_crs3}

This cross section is used for floating structural members. It is
different from cross section type CRS1 only for hydrodynamic load
computation, in the sense that partly submerged cross section is taken
care of. For hydrodynamic load computation the element is divided into
subelements specified in data section 
[Segment specification. NSEG input lines.](@ref inpmod_b_line_segment). 
The cross section can only
be used when consistent formulation is applied (see 
[STAMOD: External, static loads] (@ref stamod_b_definition_external1)) 
and for nonlinear dynamic analysis with regular waves.

Note that hydrodynamic force coefficients are specified for a fully
submerged cross section. The actual values are taken proportional with
the instantaneous cross section submergency for hydrodynamic load
computation.


#### Exceptions compared to cross section type CRS1 {#inpmod_c_crs3_exceptions}
Hydrodynamic load specification. Only Morison type loading is
available. Use of the input card CHLOAD load type HYDR is not
implemented.

Scaling of Froude-Krylov is not available. The SCFKN and SCFKT
parameters are dummy and not used.

Aerodynamic load type specification is not implemented.



#### Data group identifier {#inpmod_c_crs3_data}
~~~
NEW COMPonent CRS3
~~~


#### Component type identifier {#inpmod_c_crs3_component}
Identical to [Component type identifier for CRS1](@ref inpmod_c_crs1_component_type_identifier).


#### Mass and volume {#inpmod_c_crs3_mass}
Identical to [Mass and volume for CRS1](@ref inpmod_c_crs1_mass_and_volume).


#### Stiffness properties classification {#inpmod_c_crs3_stiffness_properties}
Identical to [Stiffness properties classification for CRS1](@ref inpmod_c_crs1_stiffness_properties )


#### Axial stiffness. Case 1, IEA=1 {#inpmod_c_crs3_stiffness_specification1}
Identical to [Axial stiffness. Case 1, IEA=1 for CRS1](@ref inpmod_c_crs1_axial_stiffness_case_1 )


#### Axial stiffness. Case 2, IEA=N {#inpmod_c_crs3_stiffness_specification2}
Identical to [Axial stiffness. Case 2, IEA=N for CRS1](@ref inpmod_c_crs1_axial_stiffness_case_2 )


#### Bending stiffness. Case 1a, IEJ=1 IPRESS=0 IMF=0  {#inpmod_c_crs3_stiffness_specification3}
Identical to [Bending stiffness. Case 1a, IEJ=1 IPRESS=0 IMF=0 for CRS1](@ref inpmod_c_crs1_bending_stiffness_case_1a )


#### Bending stiffness. Case 1b, IEJ=1 IPRESS=0 IMF=1 {#inpmod_c_crs3_stiffness_specification4}
Identical to [Bending stiffness. Case 1b, IEJ=1 IPRESS=0 IMF=1 for CRS1](@ref inpmod_c_crs1_bending_stiffness_case_1b )


#### Bending stiffness. Case 2, IEJ=1 IPRESS=1 (Not implemented) {#inpmod_c_crs3_stiffness_specification5}
Identical to [Bending stiffness. Case 2, IEJ=1 IPRESS=1 (Not implemented) for CRS1](@ref inpmod_c_crs1_bending_stiffness_case_2 )


#### Bending stiffness description. Case 3 IEJ=N IPRESS=0 {#inpmod_c_crs3_stiffness_specification6}
Identical to [Bending stiffness description. Case 3 IEJ=N IPRESS=0 for CRS1](@ref inpmod_c_crs1_bending_stiffness_case_3 )


#### Bending stiffness. Case 4 IEJ=N1, IPRESS=N2 (Not implemented) {#inpmod_c_crs3_stiffness_specification7}
Identical to [Bending stiffness. Case 4 IEJ=N1, IPRESS=N2 (Not implemented) for CRS1](@ref inpmod_c_crs1_bending_stiffness_case_4 )


#### Torsion stiffness {#inpmod_c_crs3_torsion}
Identical to [Torsion stiffness for CRS1](@ref inpmod_c_crs1_torsion_stiffness)


#### Damping specification {#inpmod_c_crs3_damping}
Identical to [Damping specification for CRS1](@ref inpmod_c_crs1_damping_specification )


#### Hydrodynamic force coefficients {#inpmod_c_crs3_hydrodynamic}
Similar to [Hydrodynamic force coefficients for CRS1](@ref inpmod_c_crs1_hydrodynamic ), but only Morison type loading is available. 


#### Capacity parameter {#inpmod_c_crs3_capacity}
Identical to [Capacity parameter for CRS1](@ref inpmod_c_crs1_capacity )




###  CRS4 - Partly submerged double symmetric cross section {#inpmod_c_crs4}

This cross section is used for floating structural members. It is different from cross section type CRS2
only for hydrodynamic load computation, in the sense that partly submerged cross section is taken care of. There is also a difference in the formulation of drag force. For hydrodynamic
load computation the element is divided into subelements specified in data group [Segment specification. NSEG input lines.](@ref inpmod_b_line_segment). The cross section can only be used when consistent formulation is applied (see [STAMOD: External, static loads] (@ref stamod_b_definition_external1)) and for nonlinear dynamic analysis with regular waves.

Note that hydrodynamic force coefficients are specified for a fully submerged cross section. The actual
values are taken proportional with the instantaneous cross section submergence. The actual submergence is based on an equivalent circular control area identical to the external area, $\mathrm{AE}$.

The drag force per unit length acting normal to the local z-direction, is assumed to act in the same
direction as the relative velocity transverse component and are computed according to:
- $\mathrm{F_y=CDY\times (A_{sub}/AE)\times \sqrt{(VRELY^2+VRELZ^2)}\times VRELY}$
- $\mathrm{F_z=CDZ\times (A_{sub}/AE)\times \sqrt{(VRELY^2+VRELZ^2)}\times VRELZ}$

where $\mathrm{A_{sub}}$ is the instantaneous submerged area of the cross section.


#### Exceptions compared to section type CRS2 {#inpmod_c_crs4_exceptions}
Hydrodynamic load specification. Only Morison type loading is
available. Use of the input card CHLOAD load type HYDR is not
implemented.

Scaling of Froude-Krylov is not available. The SCFKN and SCFKT
parameters are dummy and not used.

Aerodynamic load type specification is not implemented.


#### Data group identifier {#inpmod_c_crs4_data}

~~~
NEW COMPonent CRS4
~~~


#### Component type identifier {#inpmod_c_crs4_component}
Identical to [Component type identifier for CRS2](@ref inpmod_c_crs2_component).

#### Mass and volume {#inpmod_c_crs4_mass}
Identical to [Mass and volume for CRS2](@ref inpmod_c_crs2_mass).

#### Stiffness properties classification {#inpmod_c_crs4_stiffness_properties}
Identical to [Stiffness properties classification for CRS2](@ref inpmod_c_crs2_stiffness_properties )

#### Axial stiffness. Case 1, IEA=1 {#inpmod_c_crs4_stiffness_specification1}
Identical to [Axial stiffness. Case 1, IEA=1 for CRS2](@ref inpmod_c_crs2_axial_stiffness_case1 )

#### Axial stiffness. Case 2, IEA=N {#inpmod_c_crs4_stiffness_specification2}
Identical to [Axial stiffness. Case 2, IEA=N for CRS2](@ref inpmod_c_crs2_axial_stiffness_case2 )

#### Bending stiffness. Case 1, IEJ=1 IPRESS=0 {#inpmod_c_crs4_stiffness_specification3}
Identical to [Bending stiffness. Case 1, IEJ=1 IPRESS=0 for CRS2](@ref inpmod_c_crs2_bending_stiffness_case1 )

#### Bending stiffness. Case 2, IEJ=1 IPRESS=1 (not implemented) {#inpmod_c_crs4_stiffness_specification4}
Identical to [Bending stiffness. Case 2, IEJ=1 IPRESS=1 (not implemented) for CRS2](@ref inpmod_c_crs2_bending_stiffness_case2 )

#### Bending stiffness description. Case 3 IEJ=N IPRESS=0 {#inpmod_c_crs4_stiffness_specification5}
Identical to [Bending stiffness description. Case 3 IEJ=N IPRESS=0 for CRS2](@ref inpmod_c_crs2_bending_stiffness_description)

#### Bending stiffness. Case 4 IEJ=N1, IPRESS=N2 (not implemented) {#inpmod_c_crs4_stiffness_specification6}
Identical to [Bending stiffness. Case 4 IEJ=N1, IPRESS=N2 (not implemented) for CRS2](@ref inpmod_c_crs2_bending_stiffness_case4 )

#### Damping specification {#inpmod_c_crs4_damping}
Identical to [Damping specification for CRS1 and CRS2](@ref inpmod_c_crs1_damping_specification)

#### Hydrodynamic force coefficients {#inpmod_c_crs4_hydrodynamic}
Similar to [Hydrodynamic force coefficients for CRS2](@ref inpmod_c_crs2_hydrodynamic ), but only Morison type loading is available. 

#### Capacity parameter {#inpmod_c_crs4_capacity}
Identical to [Capacity parameter for CRS2](@ref inpmod_c_crs2_capacity )




###  CRS5 - Partly submerged general shaped cross section {#inpmod_c_crs5}
This cross section is used for floating structural members. It can only be used for elements with local
z-axis approximately parallel the global z-axis pointing in the same direction. The roll and pitch angles 
are restricted to 30$\mathrm{^{\circ}}$ as a practical upper limit. The stiffness
properties are based on two symmetry planes, while area and hydrodynamic force 
coefficients are calculated based on the cross section description represented by offset points symmetric
with regard to the vertical (z) axis. For hydrodynamic load computation the element is divided into subelements 
specified in data section [Segment specification. NSEG input lines.](@ref inpmod_b_line_segment). The cross section can 
only be used when consistent formulation is applied (see [STAMOD: External, static loads] (@ref stamod_b_definition_external1)) 
and for nonlinear dynamic analysis with regular waves.




#### Data group identifier {#inpmod_c_crs5_data}

~~~
NEW COMPonent CRS5
~~~


#### Component type identifier {#inpmod_c_crs5_component}
Identical to [Component type identifier for CRS2](@ref inpmod_c_crs2_component).


#### Mass and volume {#inpmod_c_crs5_mass}
Identical to [Mass and volume for CRS2](@ref inpmod_c_crs2_mass).


#### Stiffness properties classification {#inpmod_c_crs5_stiffness_properties}
Identical to [Stiffness properties classification for CRS2](@ref inpmod_c_crs2_stiffness_properties )


#### Axial stiffness. Case 1, IEA=1 {#inpmod_c_crs5_stiffness_specification1}
Identical to [Axial stiffness. Case 1, IEA=1 for CRS2](@ref inpmod_c_crs2_axial_stiffness_case1 )


#### Axial stiffness. Case 2, IEA=N {#inpmod_c_crs5_stiffness_specification2}
Identical to [Axial stiffness. Case 2, IEA=N for CRS2](@ref inpmod_c_crs2_axial_stiffness_case2 )


#### Bending stiffness. Case 1, IEJ=1 IPRESS=0 {#inpmod_c_crs5_stiffness_specification3}
Identical to [Bending stiffness. Case 1, IEJ=1 IPRESS=0 for CRS2](@ref inpmod_c_crs2_bending_stiffness_case1 )


#### Bending stiffness. Case 2, IEJ=1 IPRESS=1 (not implemented) {#inpmod_c_crs5_stiffness_specification4}
Identical to [Bending stiffness. Case 2, IEJ=1 IPRESS=1 (not implemented) for CRS2](@ref inpmod_c_crs2_bending_stiffness_case2 )


#### Bending stiffness description. Case 3 IEJ=N IPRESS=0 {#inpmod_c_crs5_stiffness_specification5}
Identical to [Bending stiffness description. Case 3 IEJ=N IPRESS=0 for CRS2](@ref inpmod_c_crs2_bending_stiffness_description)


#### Bending stiffness. Case 4 IEJ=N1, IPRESS=N2 (not implemented) {#inpmod_c_crs5_stiffness_specification6}
Identical to [Bending stiffness. Case 4 IEJ=N1, IPRESS=N2 (not implemented) for CRS2](@ref inpmod_c_crs2_bending_stiffness_case4 )


#### Damping specification {#inpmod_c_crs5_damping}
Identical to [Damping specification for CRS2](@ref inpmod_c_crs2_damping)




#### Hydrodynamic force coefficients {#inpmod_c_crs5_hydrodynamic}

~~~
CDX CDY CDZ CDTMOM AMX
~~~

- `CDX: real`: Drag force coefficient per length, tangential $\mathrm{[F/((L/T)^2\times L)\]}$
- `CDY: real`: Drag force coefficient per length, local y-axis $\mathrm{[F/((L/T)^2\times L)\]}$
- `CDZ: real`: Drag force coefficient per length, local z-axis $\mathrm{[F/((L/T)^2\times L)\]}$
- `CDTMOM: real`: Drag coefficient around local x-axis
    - Dummy in present version.
- `AMX: real`: Added mass per length, tangential $\mathrm{[M/L\]}$

All hydrodynamic force coefficients applies to fully submerged cross section. That is, the
actual coefficients are proportional to submerged volume.
The drag force coefficients are to be scaled according to consistent units used, 
see [Unit names and gravitational constant](@ref inpmod_data_group_a_unit_names_and_gravitational).

The tangential drag force which is a friction force acting along the local x-direction is calculated
according to:
- $\mathrm{F_t=CDX\times (A_{sub}/A_{tot})\times V_{x,rel}\times |V_{x,rel}|}$ 

The viscous normal force per unit length is calculated using the drag force term in Morison's equation 
and assuming the drag force direction is parallel the instantaneous relative velocity transverse
component:
- $\mathrm{F_y=CDY\times (A_{sub}/A_{tot})\times \sqrt{V^2_{y,rel}\times V^2_{z,rel}}\times V_{y,rel}}$  
- $\mathrm{F_z=CDZ\times (A_{sub}/A_{tot})\times \sqrt{V^2_{y,rel}\times V^2_{z,rel}}\times V_{z,rel}}$  

where:
- $\mathrm{A_{sub}}$: is instantaneous cross section submergence
- $\mathrm{A_{tot}}$: is total external areal of the cross section
- $\mathrm{V_{x,rel}}$: is relative water velocity in local x-direction
- $\mathrm{V_{y,rel}}$: is relative water velocity in local y-direction
- $\mathrm{V_{z,rel}}$: is relative water velocity in local z-direction




#### Description of cross section shape {#inpmod_c_crs5_description}

~~~
NOB NSUB NROLL NDFS
~~~

- `NOB: integer`: Number of offset points to describe the cross section shape. 
    - Only one half of the shape is described due to assumed symmetry about local z-axis.
    - 3 <= NOB <= 20
- `NSUB: integer, default: 20`: Number of points of submergence in table of submerged volume as
    function of submergence and roll angle.
- `NROLL: integer, default: 20`: Number of roll angles in table of submerged volume as function of
    submergence and roll angle.
- `NDFS: integer, default: 20`: Number of points of submergence in table of added mass and poten-
    tial damping as function of submergence.

The submerged cross section area is calculated for a number of submergence positions and relative
roll angles in the range (`0` - $\mathrm{\pi }$/`2`). The instantaneous submerged area is found by linear interpola-
tion for points lying between those given in the table.

Tables of two-dimensional added mass and potential damping as function of submergence are calculated 
using the Frank.closefit technique. The instantaneous added mass and damping are found
by linear interpolation for points lying between those given in the tables.




#### Offset points {#inpmod_c_crs5_offset}

~~~
INB YB ZB
~~~

- `INB: integer`: Offset point number 
- `YB: real`: Local y-coordinate for offset point `INB`
- `ZB: real`: Local z-coordinate for offset point `INB`

Only one half of the cross section shape is modelled due to the assumed symmetry about
local z-axis.

The offset points must be given in increasing order with decreasing value of the z-coordinate. 
`YB` and `ZB` are referred to the principal local axis. `YB >= 0` and first and last value of
`YB` has to be zero, see the figure below.

![Example of modelling cross sectional shapes of frame elements](@ref figures/um_ii_fig126.svg)
@image latex figures/um_ii_fig126.pdf "Example of modelling cross sectional shapes of frame elements" width=12cm




#### Capacity parameter {#inpmod_c_crs5_capacity}
Identical to [Capacity parameter for CRS2](@ref inpmod_c_crs2_capacity )




###  CONTACT - Contact point of roller type {#inpmod_c_contact}
Available for elastic contact surface description only.

![Example of a pipe support consisting of four rollers](@ref figures/um_ii_fig127.svg)
@image latex figures/um_ii_fig127.pdf "Example of a pipe support consisting of four rollers" width=12cm

The local coordinate system $\mathrm{(X_L,Y_L,Z_L)}$ of the elastic contact surface is indicated. 
The $\mathrm{X_L}$-axis is pointing into the paper plane.

The contact point may contain several rollers.

The rollers are located in the $\mathrm{Y_LZ_L}$-plane of the element to which the contact point is attached. Besides
the location, each roller is described by its length, which may be infinite, by its stiffness and dash pot
damping. The location and orientation of a roller is defined by a point and an inclination angle referred
in the local coordinate system of the contact surface element. A roller of finite length is shown
in the figure below. The roller origin (starting point) is defined by the point $\mathrm{(Y_R,Z_R)}$ and the inclination angle
(`ROTX`) is defined by a clockwise rotation around the contact surface $\mathrm{X_L}$-axis.

![Roller with finite length located in the local coordinate system of an element contributing to the elastic contact surface](@ref figures/um_ii_fig128.svg)
@image latex figures/um_ii_fig128.pdf "Roller with finite length located in the local coordinate system of an element contributing to the elastic contact surface" width=12cm

The $\mathrm{X_L}$-axis is pointing into the paper plane.




#### Data group identifier {#inpmod_c_contact_data}

~~~
NEW COMPonent CONTact
~~~




#### Component type identifier {#inpmod_c_contact_component}

~~~
CMPTYP-ID
~~~

- `CMPTYP-ID: character(8)`: Component type identifier



#### Number of rollers {#inpmod_c_contact_number}

~~~
NROLLS
~~~

- `NROLLS: integer`: Number of rollers

The following 3 data groups ('Location and orientation', 'Stiffness properties' and 'Spring stiffness, Case 1 or 2') must be given in blocks for
each of the `NROLLS` roller.




#### Location and orientation of roller axis {#inpmod_c_contact_location}

~~~
ROTX YR ZR RLENG
~~~

- `ROTX: real, default: 0`: Direction of roller axis. (Clockwise around the $\mathrm{X_L}$-axis of the actual
surface plane) $\mathrm{[deg\]}$
- `YR: real, default: 0`: Y-coordinate of roller origin $\mathrm{[L\]}$
- `ZR: real, default: 0`: Z-coordinate of roller origin $\mathrm{[L\]}$
- `RLENG: real, default: 0`: Length of roller $\mathrm{[L\]}$
    - `= 0` means infinite length

In case of infinite roller length, `YR` and `ZR` describe coordinates of an arbitrary point on the roller
principal axis.




#### Stiffness properties classification and damping {#inpmod_c_contact_stiffness}

~~~
IKS DAMP
~~~

- `IKS: integer`: Stiffness code1
    - 1 : Constant spring compression stiffness
    - N : Table with N pairs of pressure force - displacements to be specified
        - N > 2
- `DAMP: real, default: 0`: Dash pot damping coefficient $\mathrm{[FT/L\]}$




#### Spring stiffness, Case 1 IKS = 1 {#inpmod_c_contact_spring_stiffness_case1}

~~~
STIFFR RADROL
~~~

- `STIFFR: real`: Spring compression stiffness $\mathrm{[F/L\]}$
- `RADROL: real`: Radius of roller $\mathrm{[L\]}$

The figure below describes the interpretation of contact force in case
that `IKS=1`. The spring is active when the distance between the
principal axis of the roller and the pipe is less than 
$\mathrm{\Delta _0=RADROl+RTUBE}$. 
The external radius of the tube, `RTUBE`, is calculated from the
external area of the cross section of the element in contact with the
roller.

![Spring stiffness IKS = 1](@ref figures/um_ii_fig130.svg)
@image latex figures/um_ii_fig130.pdf "Spring stiffness IKS = 1" width=12cm




#### Spring stiffness, Case 2 IKS > 2 {#inpmod_c_contact_spring_stiffness_case2}

~~~
FS(1) ZS(1) ... FS(N) ZS(N)
~~~

- `FS(1): real < 0`: Pressure force corresponding to compression `ZS(1)` $\mathrm{[F\]}$
- `ZS(1): real`: Spring compression $\mathrm{[L\]}$
- .
- .
- .

`ZS(i)` must be given in increasing order.

The figure below describes the interpretation of contact force in case
that `IKS>2`. The specified stiffness characteristics is moved to
account for the external radius of the tube, `RTUBE`. The external
radius of the tube, `RTUBE`, is calculated from the external area of
the cross section of the element in contact with the roller.


![Spring stiffness IKS > 2](@ref figures/um_ii_fig131.svg)
@image latex figures/um_ii_fig131.pdf "Spring stiffness IKS > 2" width=12cm

The three data groups 'Location and orientation', 'Stiffness properties' and 'Spring stiffness, Case 1 or 2' are to be repeated NROLLS times.




###  Tensioner {#inpmod_c_tensioner}

Available for elastic contact surface description only.

The function of the tensioner is to grip and apply tension to the pipeline during the lay operation. In
dynamic analysis the tensioner accounts for the pipeline pay out or pay in to prevent large oscillations in the pipeline tension. This is modelled as a dynamic boundary condition with
respect to the applied axial force, eg. the applied load is `T0` plus/minus a dead band range. Outside the dead band range the load is constant. The applied load which acts in the
longitudinal direction of the tube, is formulated as a discrete element load. During static analysis the tensioner applies a constant load, `T0`, to the pipeline.




#### Data group identifier, one input line {#inpmod_c_tensioner_data}

~~~
NEW COMPonent TENSioner
~~~




#### Component type identifier {#inpmod_c_tensioner_component}

~~~
CMPTYP-ID
~~~

- `CMPTYP-ID: character(8)`: Component type identifier




#### Characteristics of tensioner {#inpmod_c_tensioner_characteristics}

~~~
T0 TMAX TMIN DELTA SIGNX
~~~

- `T0: real`: Applied load during static analysis $\mathrm{[F\]}$
- `TMAX: real`: Maximum load transmitted from the tensioner $\mathrm{[F\]}$
- `TMIN: real`: Minimum load transmitted from the tensioner $\mathrm{[F\]}$
- `DELTA: real`: Pipeline displacement through the tensioner for a load variation of: `TMAX-TMIN`  $\mathrm{[L\]}$
- `SIGNX: real, default: 1`: Direction of applied load referring to local x-axis of the element going through the tensioner $\mathrm{[\]}$
    - `SIGNX = 1.0`: The load will act in local x-axis direction
    - `SIGNX = -1.0`: The load will act opposite local x-axis

The stiffness characteristics of the tensioner will be derived from `DELTA` as: `STIFF = (TMAX-TMIN)/DELTA`




###  Tubular contact component {#inpmod_c_tubular}

This component is available for elastic contact surface description only.




#### Data group identifier, one input line {#inpmod_c_tubular_data}

~~~
NEW COMponent TUBUlar contact
~~~




#### Component type number {#inpmod_c_tubular_component}

~~~
CMPTYP-ID
~~~

- `CMPTYP-ID: character(8)`: Component type identifier




#### Specification of contact force characteristics {#inpmod_c_tubular_specification}

~~~
RCONT CHDIR IKS DAMP STIFFR FRICST FRICDY CHAXI CHROT VELLIM
~~~

- `CONT: real`: Contact radius  $\mathrm{[L\]}$
- `CHDIR: character`: Contact direction: `INWARDS` or `OUTWARDS` 
- `IKS: integer`: Stiffness code for radial contact force 
    - `= 1` Constant contact compression stiffness
    - `= N` Table with N pairs of contact force - displacement to be specified
- `RELDAM: real`: = Desired relative damping level at estimated eigen
   period in the pipe, pipe and contact spring system (see below) $\mathrm{[1\]}$. Damping is only applied in the radial
    direction. Not used in static analysis. 
- `DAMP: real`: Dash pot damping coefficient $\mathrm{[FT/L\]}$. Damping is only applied in the radial
  direction. Not used in static analysis.
- `STIFFR: real`: Spring stiffness associated with static friction
  coefficient `FRICST`, $\mathrm{[F/L\]}$. The spring stiffness is
  applied in the ring and axial directions until the spring force
  exceeds the static friction force. Not used in static
  analysis. Dummy if `CHAXI = OFF`.
- `FRICST: real`: Static friction coefficient $\mathrm{[1\]}$. Not
  used in static analysis. Dummy if `CHAXI = OFF`.
- `FRICDY: real`: Dynamic sliding friction coefficient $\mathrm{[1\]}$. `FRICDY <= FRICST`. Not used in static
  analysis. Dummy if `CHAXI = OFF`.
- `CHAXI: character`: Control parameter for axial sliding friction
    - `= ON`
    - `= OFF `
- `CHROT: character`: Control parameter for friction caused by rotation
    - `= ON` Requires `CHAXI=ON`
    - `= OFF `
- `VELLIM: real`: Velocity limit for determining that sliding has
  stopped $\mathrm{[L/T\]}$. If the relative sliding velocity
  between the pipes falls below `VELLIM`, the spring stiffness `STFFR`
  is applied.  Should be small, but not zero. Not used in static
  analysis. Dummy if `CHAXI = OFF`.

Based on specified damping level the stiffness proportional damping coefficient is
calculated by

$\mathrm{a_2=RELDAM\times 2\times \sqrt\frac{(AMS\times L)_M+(AMS\times L)_S}{STIFF}}$

where $\mathrm{(AMS\times L)_M}$ and $\mathrm{(AMS\times L)_S}$
 are total structural element mass of the master pipe and the slave pipe 
respectively and $\mathrm{STIFF}$ is contact spring sitffness.




#### Contact spring stiffness; IKS = 1 {#inpmod_c_tubular_contact_spring_stiffness_1}

~~~
STIFF
~~~

- `STIFF: real`: Spring compression stiffness $\mathrm{[F/L\]}$




#### Contact spring stiffness; IKS > 1 {#inpmod_c_tubular_contact_spring_stiffness_2}

~~~
FS(1) ZS(1) ........ FS(N) ZS(N)
~~~

- `FS(1): real < 0`: Pressure force corresponding to compression `ZS(1)` $\mathrm{[F\]}$
- `ZS(1)`: Spring compression $\mathrm{[L\]}$

`ZS(i)` must be given in increasing order




### Seafloor contact {#inpmod_c_seafloor}

The seafloor contact properties are relevant for riser systems with
tubular cross sections, which are partly resting on the bottom. This
may be the case for `SB` and `AR` systems.




#### Data group identifier, one input line {#inpmod_c_seafloor_data}

~~~
NEW COMPonent SEAFloor contact
~~~




#### Component type identifier and type {#inpmod_c_seafloor_component}

~~~
CMPTYP-ID CHSFCT
~~~

- `CMPTYP-ID: character(8)`: Component identifier 
- `CHSFCT: character(4)`: Seafloor contact component type
    - `= SPRI`: Original RIFLEX seafloor springs normal to the seafloor 
and separate axial and lateral spring-friction contact in the seafloor plane.
    - `= SOIL`: Consolidated riser-soil interaction model
    - `= CARI`: Carisima seafloor contact (restricted option)



#### Original RIFLEX seafloor spring contact {#inpmod_c_seafloor_orig}

The following three lines of input must be given if `CHSFCT = SPRI`


##### Seafloor normal contact parameters {#inpmod_c_orig_1}

~~~
STFBOT DAMBOT
~~~
- `STFBOT: real > 0`: Seafloor stiffness normal to the seafloor $[\mathrm{F/L^2}\]$ 
- `DAMBOT: real >= 0, default: 0`: seafloor damping coefficient normal to the seafloor $[\mathrm{F\times T/L^2}\]$


`STFBOT` is used for computing the spring stiffness normal to the
seafloor, $\mathrm{k_V}$ , for seafloor contact. $\mathrm{k_V}$ = `STFBOT`
$\mathrm{\times L}$ where $\mathrm{L}$ is the element length.




##### Seafloor in-plane contact parameters, two input lines {#inpmod_c_orig_2}

~~~
STFAXI FRIAXI DAMAXI
~~~

- `STFAXI: real >= 0, default: 0`: In-plane seafloor stiffness for friction in axial direction $[\mathrm{F/L^2}\]$
- `FRIAXI: real >= 0, default: 0`: In-plane seafloor friction coefficient in axial direction [1]
- `DAMAXI: real >= 0, default: 0`: In-plane seafloor damping coefficient in axial direction $[\mathrm{F\times T/L^2}\]$

~~~
STFLAT FRILAT DAMLAT ILTOR
~~~

- `STFLAT: real >= 0, default: 0`: In-plane seafloor stiffness for friction in lateral direction $[\mathrm{F/L^2}\]$
- `FRILAT: real >= 0, default: 0`: In-plane seafloor friction coefficient in lateral direction [1]
- `DAMLAT: real >= 0, default: 0`: In-plane seafloor damping coefficient in lateral direction $[\mathrm{F\times T/L^2}\]$
- `ILTOR: integer, default: 0`: Option for applying lateral contact forces at the external contact radius, giving a torsional moment
    - `= 0`: Lateral loads are applied at the node
    - `= 1`: Lateral loads are applied at the external contact radius if it is specified for the associated beam cross-section.


Contact in the seafloor plane is modelled independently in the
axial and lateral directions.  Contact is initially modelled with
linear springs. Sliding will occur when an axial or lateral spring
force reaches the friction force value. Springs will be reinstated if
the line starts sliding in the opposite direction, or if the friction
force increases and is greater than the spring force. The spring
stiffness is calculated as $k_h=\mathrm{Stalks}\times L_h$,
where $\mathrm{L_h}$ is the length of the element's horizontal
projection.  The seafloor friction forces are calculated as $F=\mathrm{FRIxxx}\times F_{vert}$ and are directed against the
axial or lateral displacements, where $\mathrm{F_{vert}}$ is the vertical
contact force between the pipe and the bottom.




#### Consolidated riser-soil seafloor contact {#inpmod_c_seafloor_ndp}

The following four lines of input must be given if `CHSFCT = SOIL`

The external contact radius `R_EXTCNT` must be positive for the
segments that have consolidated riser-soil seafloor contact.


##### Seafloor soil properties {#inpmod_c_ndp_1}

~~~
W A1 A2 V G
~~~

- `W: real > 0`: Soil submerged weight $\mathrm{[F/L^3\]}$
- `A1: real > 0`: Soil shear strength at seabed $\mathrm{[F/L^2\]}$
- `A2: real`: Soil shear strength vertical gradient $\mathrm{[F/L^3\]}$
- `V: real > 0`: Soil Poisson ratio $\mathrm{[1\]}$
- `G: real`: Soil G-modulus/compressive strength $\mathrm{[F/L^2\]}$



##### Consolidated riser-soil seafloor contact options {#inpmod_c_ndp_2}

~~~
F ALPHA BETA KBC KT
~~~

- `F: real, default: 0.88`: Relationship between dynamic stiffness and G-modulus $\mathrm{[1\]}$
- `ALPHA: real, default: 1.0`: Control parameter for suction release displacement $\mathrm{[1\]}$
- `BETA: real, default: 1.0`: Scaling factor for peak soil suction relative to peak soil compression $\mathrm{[1\]}$
- `KBC: real, default: 0.05`: Mobilization displacement for soil bearing capacity as fraction of pipe soil contact width $\mathrm{[1\]}$
- `KT: real, default: 0.08`: Mobilization displacement for max soil suction as fraction of pipe soil contact width $\mathrm{[1\]}$



##### In-plane contact parameters, two input lines {#inpmod_c_ndp_3}

~~~
STFAXI FRIAXI DAMAXI
~~~

- `STFAXI: real >= 0, default: 0`: In-plane seafloor stiffness for friction in axial direction $[\mathrm{F/L^2}\]$
- `FRIAXI: real >= 0, default: 0`: In-plane seafloor friction coefficient in axial direction [1]
- `DAMAXI: real >= 0, default: 0`: In-plane seafloor damping coefficient in axial direction $[\mathrm{F\times T/L^2}\]$

~~~
STFLAT FRILAT DAMLAT
~~~

- `STFLAT: real >= 0, default: 0`: In-plane seafloor stiffness for friction in lateral direction $[\mathrm{F/L^2}\]$
- `FRILAT: real >= 0, default: 0`: In-plane seafloor friction coefficient in lateral direction [1]
- `DAMLAT: real >= 0, default: 0`: In-plane seafloor damping coefficient in lateral direction $[\mathrm{F\times T/L^2}\]$

Contact in the seafloor plane is modelled independently in the
axial and lateral directions.  Contact is initially modelled with
linear springs. Sliding will occur when an axial or lateral spring
force reaches the friction force value. Springs will be reinstated if
the line starts sliding in the opposite direction, or if the friction
force increases and is greater than the spring force. The spring
stiffness is calculated as $k_h=\mathrm{Stalks}\times L_h$,
where $\mathrm{L_h}$ is the length of the element's horizontal
projection.  The seafloor friction forces are calculated as $F=\mathrm{FRIxxx}\times F_{vert}$ and are directed against the
axial or lateral displacements, where $\mathrm{F_{vert}}$ is the vertical
contact force between the pipe and the bottom.




#### Carisima seafloor contact, restricted option {#inpmod_c_seafloor_carisima}

The following input must be given if `CHSFCT = CARI` (restricted optio).

The soil can be modeled either as an elastic foundation with coulomb friction or as a sandy or clayey
soil. The sand/clay model account for initial penetration by weight and digging due to small displacements of the pipe. 
The penetration is used to determine vertical and lateral stiffness and breakout forces.



##### Carisima factors and debug options {#inpmod_c_cari_factors}

~~~
UFA1 UFA2 IPRSO IPREL IPRPO ILIN ISEG INOD IPCE
~~~

- `UFA1: real, default: 1`: Factor for converting default values from $\mathrm{[kN/m^2\]}$ to actual unit for $\mathrm{[F/L^2\]}$
- `UFA2: real, default: 1`: Factor for converting default values from $\mathrm{[kN/m^3\]}$ to actual unit for $\mathrm{[F/L^3\]}$
- Temporary input for debug print of detailed `CARISIMA` results (use with caution): 
    - Either:
        - `IPRSO: integer, default: 0`: Debug print switch 
        - `IPREL: integer, default: 0`: Element for original print (`IPRSO`) 
        - `IPRPO: integer, default: 0`: Contact point for original print (`IPRSO`) 
    - Or specify up to 10 soil contact points:
        - `ILIN: integer, default: 0`: Line for print of detailed `CARISIMA` results 
        - `ISEG: integer, default: 0`: Local segment for print of detailed `CARISIMA` results 
        - `INOD: integer, default: 0`: Local element for print of detailed `CARISIMA` results 
        - `IPCE: integer, default: 0`: Local contact point for print of detailed `CARISIMA` results




##### Elastic foundation with coulomb friction {#inpmod_c_seafloor_elastic}

~~~
ISTYP RKU RKV RKW RMUU RMUV
~~~

- `ISTYP: character(4)`: `= COUL` 
- `RKU: real, default: 145`: Longitudinal stiffness per unit pipe length  $\mathrm{[F/L^2\]}$
- `RKV: real, default: 145`: Transverse stiffness per unit pipe length  $\mathrm{[F/L^2\]}$
- `RKW: real, default: 200`: Vertical stiffness per unit pipe length  $\mathrm{[F/L^2\]}$
- `RMUU: real, default: 0.7`: Axial friction coefficient 
- `RMUV: real, default: 0.7`: Transverse friction coefficient 

Indicated default values for parameters with dimension $\mathrm{[F/L^2\]}$ or $\mathrm{[F/L^3\]}$ are in $\mathrm{[kN/m^2\]}$ or
 $\mathrm{[kN/m^3\]}$ and will be scaled by `UFA1` or `UFA2` before being applied. See echo of input if in doubt.




##### Sandy soil  {#inpmod_c_seafloor_sandy}

Use one of the lists.

~~~
ISTYP GRADING
~~~

- `ISTYP: character(4)`: `= SAND` 
- `Grading: character`: One of: `LOOSe, MEDIum, DENSe`

Indicated default values for parameters with dimension $\mathrm{[F/L^2\]}$ or $\mathrm{[F/L^3\]}$ are in $\mathrm{[kN/m^2\]}$ or
 $\mathrm{[kN/m^3\]}$ and will be scaled by `UFA1` or `UFA2` before being applied. See echo of input if in doubt.

~~~
ISTYP PHI WSOI POI ES RMUU RMUV
~~~

- `ISTYP: character(4)`: `= SAND` 
- `PHI: real, default: 30`: Angle of friction  $\mathrm{[deg\]}$
- `WSOI: real, default: 9.1`: Submerged unit weight of soil  $\mathrm{[F/L^3\]}$
- `POI: real, default: 0.35`: Poisson's ratio 
- `ES: real, default: 0.7`: Void ratio 
- `RMUU: real, default: 0.6`: Axial friction coefficient 
- `RMUV: real, default: 0.6`: Transverse friction coefficient (not used)

Indicated default values for parameters with dimension $\mathrm{[F/L^2\]}$ or $\mathrm{[F/L^3\]}$ are in $\mathrm{[kN/m^2\]}$ or
 $\mathrm{[kN/m^3\]}$ and will be scaled by `UFA1` or `UFA2` before being applied. See echo of input if in doubt.




##### Clay soil {#inpmod_c_seafloor_clay}

Use one of the lists.

~~~
ISTYP GRADING
~~~

- `ISTYP: character(4)`: `= CLAY` 
- `Grading: character`: One of: `LOOSe, SOFT, STIFf, HARD`

Indicated default values for parameters with dimension $\mathrm{[F/L^2\]}$ or $\mathrm{[F/L^3\]}$ are in $\mathrm{[kN/m^2\]}$ or
 $\mathrm{[kN/m^3\]}$ and will be scaled by `UFA1` or `UFA2` before being applied. See echo of input if in doubt.

~~~
ISTYP SU WSOI SUG POI ES PIX OCR RMUU RMUV RFVMX
~~~

- `ISTYP: integer/character`: `= CLAY` 
- `SU: real, default: 5`: Undrained shear strength $\mathrm{[F/L^3\]}$
- `WSOI: real, default: 4.4`: Submerged unit weight of soil  $\mathrm{[F/L^3\]}$
- `SUG: real, default: 0`: Shear strength gradient $\mathrm{[F/L^3\]}$
- `POI: real, default: 0.45`: Poisson's ratio $\mathrm{[1\]}$
- `ES: real, default: 2`: Void ratio $\mathrm{[1\]}$
- `PIX: real, default: 60`: Plasticity index $[\mathrm{\%}\]$
- `OCR: real, default: 1`: Over-consolidation ratio
- `RMUU: real, default: 0.2`: Axial friction coefficient 
- `RMUV: real, default: 0.2`: Transverse friction coefficient (not used)
- `RFVMX: real, default: 2.5`: Max transverse capacity ratio $\mathrm{[1\]}$

Indicated default values for parameters with dimension $\mathrm{[F/L^2\]}$ or $\mathrm{[F/L^3\]}$ are in $\mathrm{[kN/m^2\]}$ or
 $\mathrm{[kN/m^3\]}$ and will be scaled by `UFA1` or `UFA2` before being applied. See echo of input if in doubt.




##### Clay soil (final model) {#inpmod_c_seafloor_clay_final}

Use one of the lists.

~~~
ISTYP GRADING
~~~

- `ISTYP: character`: `= CARI` 
- `Grading: character(4)`: One of: `LOOSE, SOFT, STIF, HARD`

The input lines must be given in sequence of increasing frequency values.

~~~
ISTYP SU WSOI SU0 POI ES PIX OCR RMUU RMUV RFVMX
~~~

- `ISTYP: character(4)`: `= CARI` 
- `SU: real, default: 5`: Undrained shear strength $\mathrm{[F/L^3\]}$
- `WSOI: real, default: 4.4`: Submerged unit weight of soil  $\mathrm{[F/L^3\]}$
- `SU0: real, default: 0`: Shear strength gradient $\mathrm{[F/L^3\]}$
- `POI: real, default: 0.45`: Poisson's ratio $\mathrm{[1\]}$
- `ES: real, default: 2`: Void ratio $\mathrm{[1\]}$
- `PIX: real, default: 60`: Plasticity index $[\mathrm{\%}\]$
- `OCR: real, default: 1`: Over-consolidation ratio $\mathrm{[1\]}$
- `RMUU: real, default: 0.2`: Axial friction coefficient 
- `RMUV: real, default: 0.2`: Transverse friction coefficient (not used)
- `RFVMX: real, default: 2.5`: Max transverse capacity ratio $\mathrm{[1\]}$

Indicated default values for parameters with dimension $\mathrm{[F/L^2\]}$ or $\mathrm{[F/L^3\]}$ are in $\mathrm{[kN/m^2\]}$ or
 $\mathrm{[kN/m^3\]}$ and will be scaled by `UFA1` or `UFA2` before being applied. See echo of input if in doubt.




##### Options for calculation of contact forces {#inpmod_c_seafloor_options}

~~~
FLAG ISYMR IZVEC IRINI RZ0 RZ1 IMOMC NCPE ILUCO
~~~

- `FLAG: character`: `= SOPT`
- `ISYMR: integer, default: 1`: Option for keeping symmetry in force model. 
    - Remaining function symmetry option
    - `= 0`: Trench shoulders move independently
    - `= 1`: Trench shoulders move symmetrically
    - Used for soil types `SAND` and `CLAY` only.
- `IZVEC: integer, default: 0`: Option for considering velocities in calculations
    - `=0`: Ignore velocities
    - `=1`: Use velocities to improve accuracy at plastic to elastic drop
    - Used for soil types `COULOMB`, `SAND` and `CLAY` only.
- `IRINI: integer, default: 0`: Option for re-initialization of trench position
    - `= 0`: No re-initialization allowed
    - `= 1`: Re-initialization of trench at new position allowed; i.e. the initial trench will "follow" the line to a new contact position.
- `RZ0: integer, default: 0.001`: Penetration ratio for secant stiffness 
- `RZ1: integer, default: 0.01`: Initial penetration ratio 
- `IMOMC: integer, default: 1`: Options for including rotation / moment terms 
    - `= 0`: Related rotation/moment terms not included, i. e. only translational dofs active in seafloor contact.
    - `= 1`: Related rotation/moment terms included in load, stiffness and damping
- `NCPE: integer >= 2, default: 3`: Number of contact points to be used along each element
- `ILUCO: integer, default: 0`: Option to calculate contact at element ends
    - `= 0`: Contact forces calculated at NCPE points along each element
    - `= 1`: Contact forces calculated at element ends
    - Dummy for bar elements, for which forces are calculated at the element ends.




##### Stiffness data {#inpmod_c_seafloor_stiffness}

~~~
FLAG ISSMO RKU RKVI RKWI RKWN RKWX
~~~

- `FLAG: character`: = `STIM`
- `ISSMO: integer, default: 1`: 
    - `= 0`: Linear springs in all directions
    - `< 0`: Linear springs in axial and transverse directions
    - `= ±1`: Stiffness based on DNV/Guideline model
    - `= ±2`: Stiffness based on STATOIL/SINTEF model
    - Used for soil types `SAND` and `CLAY` 
- `RKU: real, default: 145`: Fixed stiffness in axial direction (`ISSMO >= 0`) $\mathrm{[F/L^2\]}$
    - Used for soil types `COUL`, `SAND` and `CLAY` and `ISSMO <= 0`
- `RKVI: real, default: 145`: Fixed stiffness in transverse direction (`ISSMO >= 0`) $\mathrm{[F/L^2\]}$
    - Used for soil types `COUL`, `SAND` and `CLAY` and `ISSMO <= 0`
- `RKWI: real, default: 200`: Fixed stiffness in vertical direction (`ISSMO >= 0`) $\mathrm{[F/L^2\]}$
    - Used for soil types `COUL`, `SAND` and `CLAY` and `ISSMO = 0`
- `RKWN: real, default: 10`: Minimum vertical stiffness $\mathrm{[F/L^2\]}$
    - Used for soil types `COUL`, `SAND` and `CLAY` and `ISSMO` $\mathrm{\neq }$ `0`
- `RKWX: real, default: 15000`: Maximum vertical stiffness $\mathrm{[F/L^2\]}$
    - Used for soil types `COUL`, `SAND` and `CLAY` and `ISSMO` $\mathrm{\neq }$ `0`
    - Also used for soil type `CARI`?

Indicated default values for parameters with dimension $\mathrm{[F/L^2\]}$ or $\mathrm{[F/L^3\]}$ are in $\mathrm{[kN/m^2\]}$ or
 $\mathrm{[kN/m^3\]}$ and will be scaled by `UFA1` or `UFA2` before being applied. See echo of input if in doubt.

Specified values of `RKU`, `RKVI` and `RKWI` overwrite values specified (or set to default) for soil type
`COUL`, or default values set for `SAND`, `CLAY` and `CARI`.




##### Suction data {#inpmod_c_seafloor_suction}


##### If `ISTYP = COUL, SAND` or `CLAY` the input is given as:

~~~
FLAG ISU RFO RC1 RC2 RC3 RC4
~~~

- `FLAG: character(4)`: = `SSUC` 
- `ISU: integer, default: 0`: Option for including soil suction
    - `= 0`: No suction
    - `= ± 1`: Suction force is related to vertical penetration force (static capacity) at actual penetration.
        - Reference length is the distance from the seafloor to the origin for vertical contact, but not more than one diameter.
    - `= ± 2`: Suction force is related to then maximum contact force since last lift off (or laydown).
        - Reference length is the distance from the seafloor to the origin for vertical contact, but not more than one diameter.
    - `= ±`3 : Suction force is related to $\mathrm{S_u\times D}$
        - `= -3`: Reference length is footprint.
        - `= +3`: Reference length is diameter.
- `RF0: real, default: 0.25`: Suction force factor $\mathrm{[1\]}$
- `RC1: real, default: 0.7`: Total elongation $\mathrm{[1\]}$
- `RC2: real, default: 0.12`: Elastic fraction $\mathrm{[1\]}$
- `RC3: real, default: 0.7`: Degradation fraction $\mathrm{[1\]}$
- `RC4: real, default: 0.75`: Chusion force factor $\mathrm{[1\]}$

This data group is dummy for `ISTYP = COUL` or `SAND`.

  
- The vertical extent of suction over the origin for vertical contact is to `RC1` $\mathrm{\times }$ reference length.
- The `RC2` fraction of `RC1` $\mathrm{\times }$ reference length is the elastic fraction.
- The `RC3` fraction of `RC1` $\mathrm{\times }$ reference length is the degradation fraction.

The maximum suction force is `RC0` $\mathrm{\times }$  reference force. The maximum chusion force is `RC4` $\mathrm{\times }$ `RC0` $\mathrm{\times }$  reference force.


###### If `ISTYP = CARI` the input is given as:

~~~
FLAG ISU CC TCO PFO PFN
~~~

- `FLAG: character(4)`: = `SSUC` 
- `ISU: integer, default: 1`: Suction option
    - `= 0`: off
    - `> 0`: on 
- `CC: real, default: 0.63E7`: Consolidation coefficient $\mathrm{[T/L^2\]}$
- `TCO: real, default: 0.432E5`: Initial consolidation time $\mathrm{[T\]}$
- `PF0: real, default: -1`: Initial contact force expressed in penetration $\mathrm{[1\]}$
    - `> 0`: penetration given in diameters
    - `< 0`: penetration to trench depth 
- `PFN: real, default: 0`: Minimum contact force to be used expressed in penetration $\mathrm{[1\]}$
    - `> 0`: penetration in diameters
    - `< 0`: penetration to trench depth




##### Damping data {#inpmod_c_seafloor_damping}

~~~
FLAG RDA TREF DHFAC
~~~

- `FLAG: character`: = `SDAM` 
- `RDA: real, default: See below`: Effective soil damping ratio $\mathrm{[1\]}$
- `TREF: real, default: 10`: Reference period for damping ratio $\mathrm{[s\]}$
- `DHFAC: real, default: 1`: Ratio of longitudinal and transverse damping to vertical damping

Stiffness proportional damping is applied in the vertical direction with the coefficient $\mathrm{a2}$ found as 
$\mathrm{a2=RDA\times TREF/\pi }$. 
The $\mathrm{a2}$ coefficients in the longitudinal and transverse directions are scaled by `DHFAC`.

The default value of `RDA` depends on the soil type and grading:
- `SAND`:
    - `LOOS`: 0.14
    - `MEDI`: 0.10
    - `DENS`: 0.08
    - `Other`: 0.14
- `CLAY / CARI`:
    - `LOOS`: 0.17
    - `SOFT`: 0.14
    - `STIF`: 0.06
    - `HARD`: 0.02
    - `Other`: 0.17

For `CARI`, additional vertical damping may come from suction.




##### Trench data {#inpmod_c_seafloor_trench}

~~~
FLAG NTRPT TRSHI TRLSC TRDSC
~~~

- `FLAG: character`: = `TREN` 
- `NTRPT: integer`: Number of points in the trench input table ( <= 200 in present version) 
- `TRSHI: real, default: 0`: Trench shift parameter $\mathrm{[L\]}$
- `TRLSC: real, default: 1`: Trench length scale factor $\mathrm{[1\]}$
- `TRDSC: real`: Trench depth scale factor $\mathrm{[1\]}$


Trench profile, one input line per distance from supernode 1, i.e. `NTRPT` input lines
~~~
X TD TW
~~~

- `X: real`: Arc distance from supernode 1
- `TD: real`: Depth - to be scaled by `TRLSC` 
- `TW: real`: Excess width $\mathrm{[L\]}$

Total trench width will be TW + pipe diameter.




##### Additional nonlinear spring. Only if IADSPR=1 {#inpmod_c_seafloor_additional}

~~~
ALFU BETU ALFV BETV
~~~

- `ALFU: real, default: 0.01`: Number of points in the trench input table ( <= 200 in present version) 
- `BETU: real, default: 0.1`: Additional offloading axial stiffness ratio 
- `ALFV: real, default: 0.01`: Additional onloading transverse stiffness ratio 
- `BETV: real, default: 0.1`: Additional offloading transverse stiffness ratio




##### Default values for sandy soils: {#inpmod_c_seafloor_default_sandy}

| Grading  | PHI                  | WSOI                                  | POI              | ES                 | RDA                  |
|:--------:|:--------------------:|:-------------------------------------:|:----------------:|:------------------:|:--------------------:|
|          |$\mathrm{\phi s}$| $\mathrm{W_{soil}}$             | $\mathrm{n}$ | $\mathrm{e_s}$ | $\mathrm{\xi d}$ |
|          |$\mathrm{[Deg\]}$ | $\mathrm{[kN/m^3\]}$| -                | -                  | $\mathrm{[\%\]}$  |
| LOOSe    | 30                   | 9.1                                   | 0.35             | 0.7                | 14                   |
| MEDIum   | 35                   | 9.6                                   | 0.35             | 0.5                | 10                   |
| DENSe    | 40                   | 10.1                                  | 0.35             | 0.4                |  8                   |




##### Default values for clay (OCR=1): {#inpmod_c_seafloor_default_clay}

| Grading  | SU                                  |  WSOI                                 |  POI             | ES                 |  RDA                 |  PIX               |
|:--------:|:-----------------------------------:|:-------------------------------------:|:----------------:|:------------------:|:--------------------:|:------------------:|
|          |$\mathrm{S_u}$                  | $\mathrm{W_{soil}}$             | $\mathrm{n}$ | $\mathrm{e_s}$ | $\mathrm{\xi d}$ | $\mathrm{i_p}$ |
|          |$\mathrm{[kN/m^3\]}$| $\mathrm{[kN/m^3\]}$| -                | -                  | $\mathrm{[\%\]}$  | $\mathrm{[\%\]}$|
| LOOSe    | 5                                   | 4.4                                   | 0.45             | 2.0                | 17                   | 60                 |
| SOFT     | 17                                  | 5.4                                   | 0.45             | 1.8                | 14                   | 55                 |
| STIFf    | 70                                  | 7.4                                   | 0.45             | 1.3                |  6                   | 35                 |
| HARD     | 280                                 | 9.4                                   | 0.45             | 0.8                |  2                   | 20                 |





###  Drag chain element {#inpmod_c_drag}
The drag chain element is a single node element that models a simplified contact between a drag chain and
the seafloor.




#### Data group identifier, one input line {#inpmod_c_drag_data}

~~~
NEW COMPonent DRAGchain
~~~




#### Component type identifier, one input line {#inpmod_c_drag_component}

~~~
CMPTYP-ID
~~~

- `CMPTYP-ID: character(8)`: Component type identifier




#### Drag chain element properties, one input line {#inpmod_c_drag_element}

~~~
LDC WDC FRDC LCAB WCAB
~~~

- `LDC: real`: Drag chain length $\mathrm{[L\]}$
- `WDC: real`: Drag chain weight $\mathrm{[F/L\]}$
- `FRDC: real`: Chain / seafloor friction coefficient $\mathrm{[1\]}$
- `LCAB: real, default: 0`: Cable length $\mathrm{[L\]}$
- `WCAB: real, default: 0`: Cable weight $\mathrm{[F/L\]}$







### Fibre rope cross section {#inpmod_c_fibre}


#### Data group identifier {#inpmod_c_fibr_data}

~~~
NEW COMPonent FIBRe_rope
~~~


#### Component type identifier {#inpmod_c_fibr_component}

~~~
CMPTYP-ID TEMP ALPHA BETA
~~~

- `CMPTYP-ID: character(8)`: Component type identifier
- `TEMP: real, default: 0`: Temperature at which the specification applies $\mathrm{[Temp\]}$
- `ALPHA: real, default: 0`: Thermal expansion coefficient $\mathrm{[Temp^{-1}\]}$
- `BETA: real, default: 0`: Pressure expansion coefficient $\mathrm{[1/(F/L^2)\]}$
    - `BETA` gives the expansion of an element with zero effective tension from the difference between
    the internal and the external pressure.


#### Mass and volume {#inpmod_c_fibr_mass}

~~~
AMS AE R_EXTCNT
~~~

- `AMS: real`: Mass/unit length $\mathrm{[M/L\]}$
- `AE: real`: External cross-sectional area $\mathrm{[L^2\]}$
- `R_EXTCNT: real, default: 0`: External contact radius $\mathrm{[L\]}$

The outer contact radius of the cross section, `R_EXTCNT`, is used for seafloor
contact. The default value of `R_EXTCNT` is zero.


#### Stiffness properties classification {#inpmod_c_fibr_stiffness_properties}

~~~
NOC NOWC NWC TMAX
~~~

- `NOC: integer, default: 0`: Original curve, number of point pairs
- `NOWC: integer, default: 0`: Original working curve, number of point pairs
- `NWC: integer, default: 0`: Working curve, number of point pairs
- `TMAX: real, default: 0`: Maximum mean tension $\mathrm{[F\]}$

The non-linear material curve used in static analysis is given by shifting the working
curve by redefining the initial stress-free length so that the working and original working
curves intersect at tension `TMAX`.
See figure [Tension strain curves](@ref Tension_strain_curves).


#### Axial stiffness curves {#inpmod_c_fibr_axial_stiffness}

~~~
EAF(1) ELONG(1) . . . EAF(N) ELONG(N)
~~~

- `EAF(1): real`: Tension corresponding to strain `ELONG(1)` $\mathrm{[F\]}$
- `ELONG(1): real`: Strain $\mathrm{[\%\]}$

The pairs of `EAF` and `ELONG` must be given in increasing order on a single input line.
Three sets of pairs must be given, for the working curve, original working curve and
original curve, respectively. Each curve must begin with the point pair (0.0, 0.0).
For the three curves, `N` = `NOC`, `N` = `NOWC` and `N` = `NWC`, respectively.


#### Dynamic stiffness coefficients {#inpmod_c_fibr_dynamic_st_coeff}

~~~
DSCA DSCB
~~~

- `DSCA: real, default: 1.0`: Dynamic stiffness coefficient a
- `DSCB: real, default: 0.0`: Dynamic stiffness coefficient b

The linear material curve used in dynamic analysis is given by $\mathrm{DSCA+DSCB\cdot TMEAN}$, where `TMEAN` is the mean tension of the segment, and by
redefining the initial stress-free length such that the tension is identical
between static and dynamic analysis given the elongation of static analysis.
See figure [Tension strain curves](@ref Tension_strain_curves).

\anchor Tension_strain_curves
![Tension strain curves](@ref figures/Syrope.png)
@image latex figures/Syrope.pdf "Tension strain curves" width=12cm


#### Damping specification {#inpmod_c_fibr_damping}
Identical to [Damping specification for CRS1](@ref inpmod_c_crs1_damping_specification )


#### Hydrodynamic force coefficients {#inpmod_c_fibr_hydrodynamic}
Similar to [Hydrodynamic force coefficients for CRS1](@ref inpmod_c_crs1_hydrodynamic ), but only Morison type loading is available.


#### Capacity parameter {#inpmod_c_fibr_capacity}
Identical to [Capacity parameter for CRS1](@ref inpmod_c_crs1_capacity )







### Growth - Specification of marine growth profile{#inpmod_c_growth}



#### Data group identifier, one input line {#inpmod_c_growth_comp}

~~~
NEW COMPonent GROWth
~~~




#### Component type identifier, one input line {#inpmod_c_growth_data}

~~~
CMPTYP-ID    NGRLEV
~~~

- `CMPTYP-ID: character(8)`: Component type identifier
- `NGRLEV    : integer`: Number of growth levels 


#### Growth profile, one input line per growth level, i.e. NGRLEV input lines {#inpmod_c_growth_profile}


~~~
GRLEV GRTH GRDENS
~~~

- `GRLEV: real`: Z coordinate of level given in global coordinate system $\mathrm{[L\]}$
- `GRTH: real`: Growth thickness $\mathrm{[L\]}$
- `GRDENS: real`: Growth density at this level $[\mathrm{M/L^3}\]$

The input lines must be given for decreasing values of `GRLEV`;
i.e. with increasing depth. Linear interpolation will be used to find
values at intermediate levels. Outside the specified range, the growth
thickness is set to zero, i.e. for `Z > GRLEV(1)` and `Z <
GRLEV(NGRLEV)` the thickness is zero.

Marine growth will be applied to elements with `CRS0`, `CRS1`, `CRS2`,
`CRS3`, `CRS4` and `CRS7` cross-sections.

The volume loads will be modified if the external area is non-zero. A
circular cross-section is assumed and the thickness of the marine
growth is added to the radius corresponding to the initial external area.

The Morison quadratic drag and added mass coefficients will be
modified if the hydrodynamic diameter is non-zero. For `CRS2`, `CRS4`
and `CRS7` cross-sections, the diameter of a circular cross-sections
with the same external area is used as the hydrodynamic diameter. The
quadratic drag coefficients will be scaled by the ratio of the updated
to the initial hydrodynamic diameter. The added mass coefficients will
be scaled by the square of this ratio. Linear drag coefficients will
not be modified.

Marine growth will be applied if it is specified as a load group in
`STAMOD`. The load incrementation procedure is specified as input to
the `STAMOD` module.

Currently, only one growth profile may be given.

Note that specification of marine growth profile cannot be used in
combination with drag amplification (@ref stamod_sawu).



## Data Group D: Environmental Data {#inpmod_d}

A complete environmental description consists of
environmental constants, wave and current data. When an
environment description has been completed, a new one may be given by
repeating data groups 'Identification of the environment' to 'Current parameters'
with the appropriate data for the new environment. Up
to 10 complete environmental descriptions may be given as input to
`INPMOD` in one run each identified by an unique identifier given in data
group 'Identification of the environment'. The minimum data required
in one environmental condition is environmental constants (i.e. data
groups 'Water depth and wave indicator' and 'Environment constants' are required).

Note that this data group is dummy for coupled analysis.




###  Identification of the environment {#inpmod_d_identification}




#### Data group identifier, one input line {#inpmod_d_identification_data_group}

~~~
ENVIronment IDENtification
~~~




#### Describing text. One input line {#inpmod_d_identification_describing}

~~~
< TEXT >
~~~
- `character(60)`:

Description of the environment by alphanumerical text.
Note: May be empty, but must be present.




#### Data-set identifier. One input line {#inpmod_d_identification_data_set}

~~~
IDENV
~~~

- `IDENV: character(6)`: Data set identifier for this environment description. Each environment must have a unique identifier.




###  Water depth and wave indicator {#inpmod_d_water}




#### Data group identifier, one input line {#inpmod_d_water_data}

~~~
WATErdepth AND WAVEtype
~~~




####  Water depth and control parameters. One input line {#inpmod_d_water_depth}

~~~
WDEPTH NOIRW NORW NCUSTA NWISTA
~~~

- `WDEPTH: real`: Water depth $\mathrm{[L\]}$ 
- `NOIRW: integer`: Number of irregular wave cases, maximum 10 
- `NORW: integer`: Number of regular wave cases, maximum 10 
- `NCUSTA: integer`: Number of current states, maximum 10 
- `NWISTA: integer, default: 0`: Number of wind states, maximum 10

`WDEPTH>0`. This water depth is defined as a scalar. This parameter is used in calculation of water
particle motions.

An environment description can contain up to 10 irregular wave cases and 10 regular wave
cases. A uniquely defined environment used in `STAMOD` or `DYNMOD` must refer to the
actual environment by the identifier `IDENV` and wave case number.

If a numerically defined spectrum is used, `IWASP1=5` in [Irregular wave control](@ref inpmod_d_irregular_irregular_irregular), 
the number of irregular wave cases is limited to `NOIRW=1`.

If a current line ([Spatially varying current](@ref inpmod_d_spatially)) is specified, then `NCUSTA` must be set to the total number
of current profiles given.




###  Environment constants {#inpmod_d_environment}




####  Data group identifier, one input line {#inpmod_d_environment_data}

~~~
ENVIronment CONStants
~~~




#### Constants. One input line {#inpmod_d_environment_constants}

~~~
AIRDEN WATDEN WAKIVI AIRKIVI
~~~

- `AIRDEN: real > 0`: Air density $\mathrm{[M/L^3\]}$
- `WATDEN: real > 0`: Water density $\mathrm{[M/L^3\]}$
- `WAKIVI: real, default: ` $\mathrm{1.188\times 10^{-6}}$: Kinematic viscosity of water $\mathrm{[L^2/T\]}$
- `AIRKIVI: real, default: ` $\mathrm{1.516\times 10^{-5}}$: Kinematic viscosity of air $\mathrm{[L^2/T\]}$

Typical values of `AIRDEN` and `WATDEN`  are
$\mathrm{[AIRDEN=1.3kg/m^3\]}$
and
$\mathrm{[WAYDEN=1025kg/m^3\]}$
if the units 'm' and 'kg' are used.




###  Irregular waves {#inpmod_d_irregular}
This data group is given only if `NOIRW > 0`, and is then repeated `NOIRW` times.




#### Data group identifier, one input line {#inpmod_d_irregular_data}

~~~
NEW IRREgular SEAState
~~~



#### Irregular wave control data {#inpmod_d_irregular_irregular}




##### Irregular wave control {#inpmod_d_irregular_irregular_irregular}

~~~
NIRWC IWASP1 IWADR1 IWASP2 IWADR2
~~~

- `NIRWC: integer`: Irregular wave case number 
- `IWASP1: integer`: Wave-spectrum type (wind sea)
    - `IWASP1=1`: Two-parameter Pierson-Moscowitz type spectrum
    - `IWASP1=2`: One-parameter Pierson-Moscowitz type spectrum
    - `IWASP1=3`: Jonswap spectrum
    - `IWASP1=4`: Derbyshire-Scott spectrum
    - `IWASP1=5`: Numerically defined spectrum
    - `IWASP1=6`: Ochi spectrum
        - To be used only for SI and modified SI units
    - `IWASP1=7`: Bretschneider I spectrum
        - To be used only for SI and modified SI units
    - `IWASP1=8`: Bretschneider II spectrum
        - To be used only for SI and modified SI units
    - `IWASP1=9`: Three parameter Jonswap spectrum
        - To be used only for SI and modified SI units
    - `IWASP1=10`: Double peaked spectrum (Torsethaugen) 
        - To be used only for SI and modified SI units
- `IWADR1: integer`: Wave-direction code (wind sea)
    - `IWADR1=0`: Unidirectional
    - `IWADR1>1`: Cosine-spreading function, `IWADR1` directions are used. 
    - `IWADR1=1`: Cosine-spreading function, 11 directions are used. `IWADR1=1` is thus equivaent to specifying `IWADR1=11`.
- `IWASP2: integer`: Wave-spectrum type (swell)
    - `IWASP2=0`: No swell spectrum
    - For interpretation of other values, see `IWASP1` above
- `IWADR2: integer`: Wave-direction code (swell) (dummy if `IWASP2=0`)
    - `IWADR2=0`: Unidirectional
    - `IWADR2>1`: Cosine-spreading function, `IWADR2` directions are used. 
    - `IWADR2=1`: Cosine-spreading function, 11 directions are used. `IWADR2=1` is thus equivaent to specifying `IWADR2=11`.

Bretschneider I is based on fetch and wind speed. Bretschneider II is based on wave
height and wave period.

For `IWADR1 > 0`, the directions will be evenly spaced around the
average wave propagation direction `WADIR1` at intervals of
180/(`IWADR1`+1) degrees. Specifying an even numbers of directions
should be avoided as the average wave propagation direction will not
be included in this case. The same applies to `IWADR2`.




#### Wave spectrum parameters (wind sea) {#inpmod_d_irregular_wave_wind_sea}




##### Data group identifier, one input line {#inpmod_d_irregular_wave_wind_sea_spectrum_data}

~~~
WAVE SPECtrum WIND
~~~




##### Spectrum parameters {#inpmod_d_irregular_wave_wind_sea_spectrum_parameters}

One of (i), (ii), ...., (x) is given, depending on the value of the `IWASP1` parameter in the data group 
[Irregular wave control data](@ref inpmod_d_irregular_irregular) above.




###### (i) Two-parameter Pierson-Moscowitz (`IWASP1=1`), one input line. 
~~~
SIWAHE AVWAPE
~~~

- `SIWAHE: real`: Significant wave-height, $\mathrm{H_S}$  $\mathrm{[L\]}$
- `AVWAPE: real > 0`: Zero-crossing wave-period, $\mathrm{T_Z}$  $\mathrm{[T\]}$

. 
- $\mathrm{S_{\eta }(\omega )=A\omega ^{-5}exp[-^B/\omega ^4\];0<\omega <\infty}$
- $\mathrm{A=124.2H_S^2/T_Z^4}$
- $\mathrm{B=496/T_Z^4}$

The relation between peak period, $\mathrm{T_p}$ and zero-crossing period is $\mathrm{T_Z\approx T_p/1.408}$




###### (ii) One-parameter Pierson-Moscowitz (`IWASP1=2`), one input line
~~~
SIWAHE
~~~

- `SIWAHE: real > 0`: Significant wave-height, $\mathrm{H_S}$  $\mathrm{[L\]}$

. 
- $\mathrm{S_{\eta }(\omega )=A\omega ^{-5}exp[-^B/\omega ^4\];0<\omega <\infty}$
- $\mathrm{A=0.0081g^2}$
- $\mathrm{B=3.11/H_S^2}$




###### (iii) Jonswap spectrum (`IWASP1=3`), one input line 
~~~
PEAKFR ALPHA BETA GAMMA SIGMAA SIGMAB
~~~

- `PEAKFR: real > 0`: Peak frequency (wp) $\mathrm{[radians/T\]}$
- `ALPHA: real, default: 0.008`: Phillip's constant
- `BETA: real, default: 1.25`: Form parameter 
- `GAMMA: real, default: 3.3`: Peakedness parameter giving the ratio of the maximum spectral
    energy to that of the corresponding Pierson- Moscowitz spectrum
    - `0 < GAMMA <= 20 `
- `SIGMAA: real > 0, default: 0.07`: Spectrumwidth parameter 
- `SIGMAB: real > 0, default: 0.09`: Spectrumwidth parameter 

. 
- $\mathrm{S_{\eta }(\omega )=\alpha g^2\omega ^{-5}exp(-\beta (\frac{\omega _p}{\omega })^4)\times \gamma ^{exp(-\frac{(\omega -\omega _p)^2}{2\sigma ^2\omega ^2_p})}}$ 
- $\mathrm{\alpha =1.2905H_S^2/T_Z^4}$
- $\mathrm{\beta =1.25}$ for North Sea conditions
- $\mathrm{\gamma =}$
$\begin{cases}\mathrm{1.0;}\quad\mathrm{T_p>=5\sqrt{H_S}}\\\mathrm{exp(5.75-1.15T_p/\sqrt{H_S})}\\\mathrm{5.0;}\quad\mathrm{T_p<3.6\sqrt{H_S}}\end{cases}$
 - $\mathrm{\sigma =}$
 $\begin{cases}\mathrm{\sigma _a=0.07}\quad\mathrm{for}\quad\omega <=\omega _p\\\mathrm{\sigma _b=0.09}\quad\mathrm{for}\quad\omega <=\omega _p\end{cases}$
- $\mathrm{\omega _p=\frac{2\pi }{T_p}}$
- $\mathrm{\frac{T_p}{T_Z}=1.407(1-0.287ln\gamma )^{1/4}}$




###### (iv) Derbyshire-Scott spectrum (`IWASP1=4`), one input line
~~~
SPEC1 SPEC2 SPEC3 SIWAHE AVWAPE TRUNCL TRUNCU
~~~

- `SPEC1: real, default: 0.214`: Spectrum parameter, a $\mathrm{[T/rad\]}$
- `SPEC2: real > 2, default: 0.065`: Spectrum parameter, b $\mathrm{[rad/T\]}$
- `SPEC3: real, default: 0.26`: Spectrum parameter, d $\mathrm{[rad/T\]}$
- `SIWAHE: real`: Significant wave height, $\mathrm{H_S}$ $\mathrm{[L\]}$
- `AVWAPE: real > 0`: Average wave period, $\mathrm{T}$ $\mathrm{[T\]}$
- `TRUNCL: real, default: 0.0414`: Lower truncation parameter $\mathrm{[radians/T\]}$
- `TRUNCU: real, default: 10.367`: Upper truncation parameter $\mathrm{[radians/T\]}$

- $\mathrm{S_{\eta }(\omega )=\alpha H_S^2exp\sqrt{\frac{(\omega -\omega _p)^2}{b(\omega -\omega _p+d)}}}$ for $\mathrm{TRUNCL<\omega <TRUNCU}$




###### (v) Numerically defined spectrum (`IWASP1=5`)

Both (v.1) and (v.2) must be given.

(v.1) Number of discrete frequencies, one input line.
~~~
NDFRQ1
~~~

- `NDFRQ1: integer >= 4`: Number of discrete frequencies

(v.2) Spectrum values, NDFRQ input lines. Either:
~~~
FRQ DSPDEN
~~~

- `FRQ: real`: Frequency $\mathrm{[radians/T\]}$
- `DSPDEN: real`: Associated discrete spectral density value $\mathrm{[L^2T\]}$

The input lines must be given in sequence of increasing frequency values.




###### (vi) Ochi spectrum (`IWASP1=6`), one input line.
~~~
SIWAHE
~~~

- `SIWAHE: real`: Significant wave height $\mathrm{[L\]}$




###### (vii) Bretschneider spectrum I (`IWASP1=7`), one input line
~~~
FETCH WISPD
~~~

- `FETCH: real`: Fetch $\mathrm{[L\]}$
- `WISPD: real`: Wind speed $\mathrm{[L/T\]}$




###### (viii) Bretschneider spectrum II (`IWASP1=8`), one input line
~~~
SIWAHE SIWAPE
~~~

- `SIWAHE: real`: Significant wave height $\mathrm{[L\]}$
- `SIWAPE: real > 0`: Significant wave period $\mathrm{[T\]}$




###### (ix) Three parameter JONSWAP spectrum (`IWASP1=9`), one input line.
~~~
SIWAHE PEAKPE GAMMA
~~~

- `SIWAHE: real`: Significant wave height $\mathrm{[L\]}$
- `PEAKPE: real > 0`: Peak period $\mathrm{[T\]}$
- `GAMMA: real, default: see below`: Peakedness parameter giving the ratio of the maximum spectral
    energy to that of the corresponding Pierson-Moscowitz spectrum
    - `0< GAMMA <= 20`

Default value of `GAMMA` is calculated from `SIWAHE` and `PEAKPE`, see (iii) Jonswap spectrum (`IWASP1=3`):

$\mathrm{GAMMA=exp[5.75-1.15\times \frac{PEAKPE}{\sqrt{SIWAHE}}\]}$

$\mathrm{1<=GAMMA<=5}$

Note that use of the three parameter `JONSWAP` spectrum requires that the SI units m and s be
used.




###### (x) Double peaked JONSWAP spectrum (`IWASP1=10`) (described by Torsethaugen) , one input line.
~~~
SIWAHE PEAKPE
~~~

- `SIWAHE: real`: Significant wave height $\mathrm{[L\]}$
- `PEAKPE: real > 0`: Peak period $\mathrm{[T\]}$

Note that use of the double peaked `JONSWAP` spectrum requires that the SI units m and s be used.




#### Wave spectrum parameters (swell) {#inpmod_d_irregular_swell}

This data group is omitted for `IWASP2=0`, see [Irregular wave control data](@ref inpmod_d_irregular_irregular) (no swell present).




##### Data group identifier, one input line {#inpmod_d_irregular_swell_data}

~~~
WAVE SPECtrum SWELl
~~~




##### Spectrum parameters {#inpmod_d_irregular_swell_parameters}

One of (i), (ii), ..., (x) is given, depending on the value of the IWASP2 parameter given in 
data group [Irregular wave control data](@ref inpmod_d_irregular_irregular). 
The input is identical to input of wind sea spectrum and is therefore not
repeated, see [Wave spectrum parameters (wind sea)](@ref inpmod_d_irregular_wave_wind_sea).




#### Direction parameters of waves {#inpmod_d_irregular_direction}




##### Data group identifier, one input line {#inpmod_d_irregular_direction_data}

~~~
DIRECTION PARAMETERS
~~~

The two input lines below ('Wave direction parameters (wind sea)' and 'Wave direction parameters (swell)') must be given in sequence if both are present.




##### Wave direction parameters (wind sea), one input line {#inpmod_d_irregular_direction_wind_sea}

~~~
WADR1 EXPO1
~~~

- `WADR1: real`: Average propagation direction of waves, measured in degrees from the global X-axis. 
    - Confer the figure [Location of support vessel coordinate system](@ref Location_of_support_vessel_coordinate_system) 
- `EXPO1: real`: Exponent of cosine distribution 
    - dummy if `IWADR1=0`, see [Irregular wave control data](@ref inpmod_d_irregular_irregular).

If `IWADR1 > 0`, a cosine directional spreading function is used:
$\mathrm{f(\alpha _i)=\frac{[cos(\alpha _i-WADR1)\]^{EXPO1}}{\sum[f(\alpha _j)\]}}$
where $\mathrm{\alpha _i}$ is one of the `IWADR1` short-crested wave
directions. The sum in the denominator is taken over all `IWADR1` directions.
The total wind sea energy is thus kept.




##### Wave direction parameters (swell), one input line {#inpmod_d_irregular_direction_swell}

This data group is omitted for `IWASP2=0`, see [Irregular wave control data](@ref inpmod_d_irregular_irregular) (no swell present).

~~~
WADR2 EXPO2
~~~

- `WADR2: real`: Average propagation direction of waves, measured in degrees from the global X-axis. 
    - Confer the figure [Location of support vessel coordinate system](@ref Location_of_support_vessel_coordinate_system) 
- `EXPO2: real`: Exponent of cosine distribution 
    - dummy if `IWADR2=0`, see [Irregular wave control data](@ref inpmod_d_irregular_irregular).

If `IWADR2 > 0`, a cosine directional spreading function is used:
$\mathrm{f(\alpha _i)=\frac{[cos(\alpha _i-WADR2)\]^{EXPO2}}{\sum[f(\alpha _j)\]}}$
where $\mathrm{\alpha _i}$ is one of the `IWADR2` short-crested wave
directions. The sum in the denominator is taken over all `IWADR2` directions.
The total swekk energy is thus kept.



###  Regular waves {#inpmod_d_regular}
This data group is given only if `NORW > 0`.




#### Data group identifier, one input line {#inpmod_d_regular_data}

~~~
REGULAR WAVE DATA
~~~




#### Regular wave data, NORW input lines {#inpmod_d_regular_norw}

~~~
INRWC AMPLIT PERIOD WAVDIR
~~~

- `INRWC: integer`: Regular wave case number 
- `AMPLIT: real`: Wave amplitude $\mathrm{[L\]}$
- `PERIOD: real > 0`: Wave period $\mathrm{[T\]}$
- `WAVDIR: real`: Wave propagation direction from the global X-axis $\mathrm{[deg\]}$
    - Confer the figure [Location of support vessel coordinate system](@ref Location_of_support_vessel_coordinate_system) 




###  Current parameters {#inpmod_d_current}
This data group is given only if `NCUSTA > 0`, and is then repeated `NCUSTA` times.




#### Data group identifier, one input line {#inpmod_d_current_data}
May be omitted if no current is present for actual environment.

~~~
NEW CURRENT STATE
~~~




#### Current dimension parameter, one input line {#inpmod_d_current_dimension}

~~~
ICUSTA NCULEV L_EXT
~~~

- `ICUSTA: integer`: Current state number 
- `NCULEV: integer`: Number of current levels 
- `L_EXT: integer, default: 0`: Flag to indicate if current data is given in this input file, or if it shall
    be read from an external file. 
    - For details on the format of the external file, confer CURMOD User’s Documentation. 
    - `0`: Data specified on this file
    - `1`: Data specified on external file

`1 <= NCULEV <= 30`. Current states must be given in increasing order, i. e. `1,2, ..., NCUSTA`




#### Current profile, one input line per current level, i.e. NCULEV input lines {#inpmod_d_current_profile}




##### This data group is given only if `L_EXT = 0`

~~~
CURLEV CURDIR CURVEL
~~~

- `CURLEV: real`: Z coordinate of level given in global coordinate system $\mathrm{[L\]}$
- `CURDIR: real`: Current velocity direction at this level. The angle is measured in
    degrees from the global X-axis counter-clockwise around the global
    Z-axis. (seen from above) 
- `CURVEL: real`: Current velocity at this level $\mathrm{[L/T\]}$

The input lines must be given in sequence of decreasing Z coordinates. Linear
interpolation is applied between the levels. Outside the specified range of levels a
"flat" extrapolation is used, i.e. for `Z > CURLEV(1)` the velocity is set to
`CURVEL(1)` and for `Z < CURLEV(NCULEV)` the velocity is set to `CURVEL(NCULEV)`

This current profile may be scaled when applied in static or dynamic analysis.

Z coordinate is zero at mean water level and negative below sea surface.




##### This data group is given only if `L_EXT = 1`

~~~
CURRFILE
~~~

- `CURRFILE: character(120)`: Name of external file with specified current data




###  Spatially varying current {#inpmod_d_spatially}




#### Data group identifier, one input line {#inpmod_d_spatially_data}

~~~
NEW CURRENT LINE
~~~




#### Current line control parameters, one input line {#inpmod_d_spatially_line}

~~~
ICUSTA NPT
~~~

- `ICUSTA: integer`: Current state number 
- `NPT: integer`: Number of current profiles given

The number of current states `NCUSTA` (see [Water depth and control parameters](@ref inpmod_d_water_depth)) must be increased by
`NPT` for each current line specified.

Current states must be given in ascending order




#### Current dimension parameters, one input line {#inpmod_d_spatially_dimension}

~~~
IPT NCULEV XPT YPT
~~~

- `IPT: integer`: Current profile number. Must be given from 1 to `NPT` consecutively 
- `NCULEV: integer`: Number of current levels 
    - `1 < NCULEV <= 30`
- `XPT: real`: Global X- and Y- coordinates 
- `YPT: real`: For which this current profile is specified




#### Current profile, one input line per current level, i.e. NCULEV input lines {#inpmod_d_spatially_profile}

~~~
CURLEV CURDIR CURVEL
~~~

- `CURLEV: real`: Z coordinate of level given in global coordinate system $\mathrm{[L\]}$
- `CURDIR: real`: Current velocity direction at this level. The angle is measured in
    degrees from the global X-axis counter-clockwise around the global
    Z-axis. (seen from above) 
- `CURVEL: real`: Current velocity at this level $\mathrm{[L/T\]}$

The input lines must be given in sequence of decreasing Z coordinates. Linear
interpolation is applied between the levels. Outside the specified range of levels a
"flat" extrapolation is used, i.e. for `Z > CURLEV(1)` the velocity is set to
`CURVEL(1)` and for `Z < CURLEV(NCULEV)` the velocity is set to `CURVEL(NCULEV)`

This current profile may be scaled when applied in static or dynamic analysis.

Z coordinate is zero at mean water level and negative below sea surface.




###  Wind parameters {#inpmod_d_wind}
This data group is given only if `NWISTA > 0`, and is then repeated `NWISTA` times.




#### Data group identifier, one input line {#inpmod_d_wind_data}
May be omitted if no wind is present for actual environment.

~~~
NEW WIND SPECification
~~~




#### Wind case number, one input line {#inpmod_d_wind_number}

~~~
IWISTA
~~~

- `IWISTA: integer`: Wind case number





#### Wind type, one input line {#inpmod_d_wind_type}

~~~
IWITYP
~~~

- `IWITYP: integer`: Wind type
    - `IWITYP=10`: Stationary uniform wind with shear, values interpolated at grid points
    - `IWITYP=11`: Fluctuating uniform 2-component wind
    - `IWITYP=12`: Fluctuating 3-comp. wind read from files (IECWind format)
    - `IWITYP=13`: Fluctuating 3-comp. wind read from files (TurbSim Bladed style format)
    - `IWITYP=14`: Stationary uniform wind with shear

The wind types 10 - 14 are intended for wind turbine analyses. However, they may
also be applied for other type of analysis.

For the IECWind fluctuating 3-component wind (`IWITYP=12`), only the fluctuating part of the wind is
given in the wind input files. The mean wind speed `UMEAN` given above is added to the
yield the total wind velocity in the longitudinal direction. The input files must conform to the
3-dimensional 3-component wind time series from the rectangular IEC format 
(See Thomsen, K., 2006. Mann turbulence for the IEC Code Comparison Collaborative (OC3). Risø
National Laboratory). More specifically they must include time series of wind velocity in
binary format, with a 3-dimensional array having indices in vertical direction running fastest, 
then indices in lateral direction and indices in longitudinal direction running slowest.

For wind files from NREL's TurbSim (`IWITYP=13`), the mean wind speed and shear are included 
in the binary files. The input files must be generated by TurbSim with WrBLFF=True. Both the 
.wnd file and .sum file are needed. 




#### Wind type specifications {#inpmod_d_wind_specification}




##### Stationary uniform wind with shear, values interpolated at grid points (`IWITYP=10`) {#inpmod_d_wind_specification_stationary}

Wind direction, one input line
~~~
WIDIR
~~~

- `WIDIR: real`: Wind propagation direction in global XY-plane $\mathrm{[deg\]}$

Wind velocity, one input line
~~~
UMVEL VMVEL WMVEL
~~~

- `UMVEL: real`: Longitudinal wind velocity component $\mathrm{[L/T\]}$
- `VMVEL: real`: Lateral wind velocity component $\mathrm{[L/T\]}$
- `WMVEL: real`: Vertical (global Z-axis) wind velocity component $\mathrm{[L/T\]}$

The parameters `UMVEL` and `VMVEL` refer to the direction given by the `WIDIR` parameter

Number of levels in shear profile, one input line
~~~
NZPROF
~~~

- `NZPROF: integer`: Number of vertical levels for defining the shear profile

Wind velocity profile definition, `NZPROF` input lines
~~~
ZLEV UFACT VFACT WFACT
~~~

- `ZLEV: real`: Vertical coordinate of profile level $\mathrm{[L\]}$
- `UFACT: real`: Wind speed scaling factor for longitudinal wind velocity 
- `VFACT: real`: Wind speed scaling factor for the lateral wind velocity 
- `WFACT: real`: Wind speed scaling factor for the vertical wind velocity 

Wind field domain location, one input line
~~~
Z0
~~~

- `Z0: real`: Z coordinate of the lower edge of the wind field domain $\mathrm{[L\]}$

Domain size, one input line
~~~
NZ
~~~

- `NZ: integer`: Number of grid points in Z- (vertical) direction

Domain resolution, one input line
~~~
DLWFZ
~~~

- `DLWFZ: real`: Domain resolution in the vertical direction $\mathrm{[L\]}$




##### Fluctuation uniform 2-component wind read from file (`IWITYP=11`) {#inpmod_d_wind_specification_fluctation_2}

Wind direction, one input line
~~~
WIDIR
~~~

- `WIDIR: real`: Wind propagation direction in global XY-plane $\mathrm{[deg\]}$

Wind data file name, one input lines
~~~
CHWIFI
~~~

- `CHWIFI: character(256)`: Path and filename for import of wind velocity time series. See the
SIMO User Manual ('Reading wind time series from file' in 'Initialization of time domain simulation' in 'Use of DYNMOD') for explanation on file format.




##### Fluctuating 3-component wind field read from file (IWITYP=12) {#inpmod_d_wind_specification_fluctation_3}

Mean wind direction, one input line
~~~
WIDIR
~~~

- `WIDIR: real`: Wind propagation direction in global XY-plane $\mathrm{[deg\]}$

Mean wind velocity, one input line
~~~
UMVEL
~~~

- `UMVEL: real`: Mean wind velocity along `WIDIR` $\mathrm{[L/T\]}$

Number of levels in shear profile, one input line
~~~
NZPROF
~~~

- `NZPROF: integer`: Number of vertical levels for defining the shear profile

Wind velocity profile definition, `NZPROF` input lines
~~~
ZLEV UMFACT UFACT VFACT ZFACT
~~~

- `ZLEV: real`: Vertical coordinate of profile level $\mathrm{[L\]}$
- `UMFACT: real`: Scaling factor for the mean wind velocity
- `UFACT: real`: Scaling factor for fluctuating part of the longitudinal wind velocity 
- `VFACT: real`: Scaling factor for fluctuating part of the lateral wind velocity 
- `ZFACT: real`: Scaling factor for fluctuating part of the vertical wind velocity 

Name of file containing the fluctuating longitudinal wind time series, one input line
~~~
CHWFU
~~~

- `CHWFU: character(256)`: Path and filename for the fluctuating U-component wind time series

Name of file containing the fluctuating lateral wind time series, one input line
~~~
CHWFV
~~~

- `CHWFV: character(256)`: Path and filename for the fluctuating V-component wind time series

Name of file containing the fluctuating vertical wind time series, one input line
~~~
CHWFW
~~~

- `CHWFW: character(256)`: Path and filename for the fluctuating Z-component wind time series

Wind field domain location, one input line
~~~
X0LL Y0LL Z0LL
~~~

- `X0LL: real`: X-coordinate of the lower left corner of the upstream border of the
    wind field domain $\mathrm{[L\]}$
- `Y0LL: real`: Y-coordinate of the lower left corner of the wind field domain $\mathrm{[L\]}$
- `Z0LL: real`: Z-coordinate of the lower left corner of the wind field domain$\mathrm{[L\]}$

These three coordinates defines the lower left corner of the wind field domain, which is defined as a rectangular
cuboid. The coordinates refers to a coordinate system centred at the global origin, with the x-axis (longitudinal
direction) pointing in the down-stream mean wind speed direction and the z-axis coincident with the global z-axis.

Domain size, one input line
~~~
NX NY NZ
~~~

- `NX: integer`: Number of grid points in X- (longitudinal) direction $\mathrm{[L\]}$
- `NY: integer`: Number of grid points in Y- (lateral) direction $\mathrm{[L\]}$
- `NZ: integer`: Number of grid points in Z- (vertical) direction$\mathrm{[L\]}$

Field size, one input line
~~~
LWFX LWFY LWFZ
~~~

- `LWFX: real`: Field size in X- (longitudinal) direction 
- `LWFY: real`: Field size in Y- (lateral) direction 
- `LWFZ: real`: Field size in Z- (vertical) direction

Buffer size, one input line
~~~
NSLICE
~~~

- `NSLICE: integer, default: 10`: Buffer size: Number of wind crossectional planes (Slices) in memory




##### Fluctuating 3-component wind field read from TurbSim file (IWITYP=13) {#inpmod_d_wind_specification_turbsim}

The wind field domain- and field size are extracted from the TurbSim .sum file.

The wind field domain location in the global coordinate system is not
given explicitly by the user. The vertical position of the wind field center
is the same as in TurbSim; i.e. taken as the hub height given
on the turbsim .sum file. 

Horizontally, the wind field is positioned around the global origin, but with
a half grid width downwind of the origin. Since the TurbSim wind is non-periodic,
this is necessary to ensure that the entire turbine lies in the same part of
the wind field at the start of the simulation. The wind at the global origin
will thus not start at the first slice

The wind field must be large enough to ensure that the whole structure is
within the wind field during the entire simulation. As the TurbSim wind field
is nonperiodic, the beginning and end of the wind field will not fit together.


Mean wind direction, one input line 
~~~
WIDIR
~~~

- `WIDIR: real`: Wind propagation direction in global XY-plane $\mathrm{[deg\]}$

Name of binary (.wnd) file containing the TurbSim fluctuating wind time series, one input line
~~~
CHWFTW
~~~

- `CHWFTW: character(256)`:  Path and filename for the binary TurbSim (.wnd) file

Name of the summary (.sum) file from TurbSim, one input line
~~~
CHWFTS
~~~

- `CHWFTS: character(256)`:  Path and filename for the summary TurbSim (.sum) file


Buffer size, one input line
~~~
NSLICE
~~~

- `NSLICE: integer, default: 800`: Buffer size: Number of wind crossectional planes (Slices) in memory

Note: Since TurbSim files are not periodic, time series are shifted by 1/2 Grid Width. The number of slices in memory must be greater than (Grid Width/MeanWindSpeed/WindFileTimeStep).




##### Stationary uniform wind with shear (`IWITYP=14`) {#inpmod_d_wind_specification_shearform}


Wind direction, velocity and shear profile type, one input line
~~~
WIDIR UMVEL WMVEL CH_SHEAR
~~~

- `WIDIR: real`: Wind propagation direction in global XY-plane $\mathrm{[deg\]}$
- `UMVEL: real`: Longitudinal wind velocity component $\mathrm{[L/T\]}$
- `WMVEL: real`: Vertical (global Z-axis) wind velocity component $\mathrm{[L/T\]}$
- `CH_SHEAR: character(4)`: Shear profile type
    - `NONE` - No shear profile
    - `POWR` - Power shear profile
    - `LOGA` - Logarithmic shear profile


`UMVEL` is the wind velocity in the direction `WIDIR`.


Poser shear profile input, one input line, only given if `CH_SHEAR = POWR`
~~~
ZREF ALPHA
~~~

- `ZREF: real`: Reference height $\mathrm{[L\]}$
- `ALPHA: real`: Wind shear exponent $\mathrm{[-\]}$


Logarithmic shear profile input, one input line, only given if `CH_SHEAR = LOGA`
~~~
ZREF Z0
~~~

- `ZREF: real`: Reference height $\mathrm{[L\]}$
- `Z0: real`: Roughness length $\mathrm{[L\]}$





## Data Group E: Support Vessel Data {#inpmod_e}

Observe that the motion transfer function definition is related to the
wave field definition. See 'Motion Transfer Functions' in the Theory Manual for the definition of
wave field and motion transfer functions. Transfer functions based on
other definitions must be converted by appropriate phase shift
operations before they are used as input to this program.

This data group needs not be given for systems with no vessel attachment
points. Note that either 'Support vessel data on file' or 'Identification' through 'Transfer function input' is to be given.




###  Support vessel data on file {#inpmod_e_on_file}




#### Data group identifier, one line {#inpmod_e_on_file_data}

~~~
TRANsfer FUNCtion FILE
~~~




#### File name {#inpmod_e_on_file_name}

~~~
CHFTRA
~~~

- `CHFTRA: character(80)`: File name with transfer functions data

File with transfer function data given in RIFLEX format terminated with an `END` statement.

This group replaces the rest of group E if given. Either 'Support vessel data on file' or 'Identification' through 'Transfer function input' should be given. If 'Support vessel data on file' is given, the content on the file should be 'Identification' to 'Transfer function input' with an `END` termination.




###  Identification {#inpmod_e_identification}




#### Data group identifier, one input line {#inpmod_e_identification_data}

~~~
SUPPort VESSel IDENtification
~~~




#### Heading, one input line {#inpmod_e_identification_heading}

~~~
Heading
~~~

Text describing the transfer functions.

Always one input line, which may be blank. The line may contain up to
60 characters.




#### Identifier, one input line {#inpmod_e_identification_identifier}

~~~
IDWFTR
~~~

- `IDWFTR: character(6)`: Identifier for transfer functions. The value 'NONE' is not allowed.




###  Transfer function reference position {#inpmod_e_transfer_reference}

This data group is used as control parameter and compared with vessel
position specified in
[Data Group B: Single Riser Data](@ref inpmod_data_group_b_single_riser_data).




#### Data group identifier, one input line {#inpmod_e_transfer_reference_data}

~~~
HFTRan REFErence POSItion
~~~




#### Reference position, one input line {#inpmod_e_transfer_reference_reference}

~~~
ZG
~~~

- `ZG: real`: Vertical position of the support vessel coordinate system. $\mathrm{[L\]}$
    - (The global Z coordinate for which the vessel motion transfer function is calculated.) 
    - Confer the figure [Location of support vessel coordinate system](@ref Location_of_support_vessel_coordinate_system) (below).
    -  This parameter is used as control parameter and compared with `ZG` in data groups.

\anchor Location_of_support_vessel_coordinate_system
![Location of support vessel coordinate system](@ref figures/um_ii_fig164.svg)
@image latex figures/um_ii_fig164.pdf "Location of support vessel coordinate system" width=12cm




###  Dimension parameter and input type code {#inpmod_e_dimension}




#### Data group identifier, one input line {#inpmod_e_dimension_data}

~~~
HFTRansfer CONTrol DATA
~~~




#### Dimension parameters, one input line {#inpmod_e_dimension_parameters}

~~~
NDHFTR NWHFTR ISYMHF ITYPIN
~~~

- `NDHFTR: integer`: No. of directions for which transfer functions are given 
    - `NDHFTR=1` or `NDHFTR>=4`
- `NWHFTR: integer`: No of frequencies for which transfer functions are given
    - `NWHFTR>=4`
- `ISYMHF: integer`: Symmetry code related to transfer functions
    - `ISYMHF=0`: No symmetry
    - `ISYMHF=1`: Symmetry about XV-ZV plane
    - `ISYMHF=2`: Symmetry about XV-ZV and YV-ZV planes
- `ITYPIN: integer`: Code for which format the HF-transfer function are given
    - `ITYPIN=1`: Non-dimensional complex form
    - `ITYPIN=2`: Non-dimensional amplitude ratio and phase, where phase is given in degrees
    - `ITYPIN=3`: Non-dimensional amplitude ratio and phase, where phase is given in radians


The complex form and the amplitude ratio are to be given as non-dimensional.
This means: 
- L/L for freedoms surge, sway and heave
- radian/radians or degrees/degrees for freedoms roll, pitch and yaw, giving motion
    angle/surface wave slope amplitude. The wave slope amplitude is defined by
    $\mathrm{\gamma _a=k\zeta_a}$ where $\mathrm{k}$ is the wave number and $\mathrm{\zeta_a}$ is
    the wave amplitude.

If `NDHFTR=1`, `ISYMHF` is dummy (set to zero by the program). In this case the specified 
transfer function is used, regardless of the wave direction. Note that the specified motions 
are applied in the local vessel coordinate system regardless of the wave direction; e.g. 
surge motions are applied in the local vessel x-direction. In practice, the wave direction will not have
any effect on the vessel motions in this case. To rotate the motions with the wave direction, 
update the vessel heading when the wave direction is changed. This method must however be used with care, 
if the model is not symmetric and connected to the vessel in the local vessel origo, it may not give the
desired effect.




###  Specifications of wave directions {#inpmod_e_specificattions_directions}

Wave directions given in vessel coordinate system for input of motion transfer functions.




#### Data group identifier, one input line {#inpmod_e_specificattions_directions_data}

~~~
WAVE DIREctions
~~~




#### Directions, NDHFTR input lines {#inpmod_e_specificattions_directions_directions}

~~~
IHEAD HEAD
~~~

- `IHEAD: integer`: Direction number
- `HEAD: real`: Direction. The angle `HEAD` is measured in degrees from the XV axis
    counter clockwise to the wave propagation vector

`IHEAD` and `HEAD` must be given in ascending order

If `NDHFTR=1`, `HEAD` is dummy.

If the directions do not cover a full circle, the transfer functions for the first
direction will be repeated for the direction `HEAD(1) + 360`. For `ISYMHF`> 0, the
last direction after mirroring is `360 - HEAD(1)`.



###  Specification of wave frequencies {#inpmod_e_specification_frequencies}




#### Data group identifier, one input line {#inpmod_e_specification_frequencies_data}

~~~
WAVE FREQuencies
~~~




#### Frequencies, NWHFTR input lines {#inpmod_e_specification_frequencies_nwhftr}

~~~
IFREQ WHFTR
~~~

- `IFREQ: integer`: Frequency number
- `WHFTR: real`: Frequency $\mathrm{[rad/T\]}$

Frequencies must be given in increasing order.




###  Transfer function input {#inpmod_e_transfer_input}




#### Data group identifier, one input line {#inpmod_e_transfer_input_data}

~~~
HFTRansfer FUNCtion "DOF"
~~~

"dof" is either `SURGE, SWAY, HEAVE, ROLL, PITCH` or `YAW`




#### Transfer function for HF "dof" motion, NDHFTR x NWHFTR input lines {#inpmod_e_transfer_input_function}

~~~
IDIR IFREQ A B
~~~


- `IDIR: integer`: Direction number 
- `IFREQ: integer`: Frequency number 
- `A: real`: Interpretation according to value of `ITYPIN`
(given in the data group [Reference position, one input line](@ref inpmod_e_transfer_reference_reference))
    - `ITYPIN=1:` A - Real part
    - `ITYPIN=2:` A - Amplitude ratio
    - `ITYPIN=3:` A - Amplitude ratio 
- `B: real`: Interpretation according to value of `ITYPIN`
(given in the data group [Reference position, one input line](@ref inpmod_e_transfer_reference_reference))
    - `ITYPIN=1:` B - Imaginary part
    - `ITYPIN=2:` B - Phase (degrees)
    - `ITYPIN=3:` B - Phase (radians)




[Data group identifier, one input line](@ref inpmod_e_transfer_input_data) is repeated for each 
degree of freedom included in motion description. If one (or more)
degrees of freedom are omitted, they are set equal to zero.

For phase and sign convention, see 'Motion Transfer Functions' in the Theory Manual.

If only one direction is specified (`NDHFTR=1`), the transfer function is used
independent of incoming wave direction.

Amplitudes and phase angles at required frequencies are calculated by linear
interpolation/extrapolation in the dynamic analysis. Transfer functions will therefore be extrapolated for spectral 
components outside the frequency range defined for the transfer
function. Ensure that the amplitude values given for the two highest/lowest frequencies give physical realistic values when extrapolated. 
Add two zero amplitude components at both ends of the frequency range if no extrapolation is wanted.

Linear interpolation is also used for wave direction.




###  Termination of input data {#inpmod_e_termination}

Do not forget the `END` input line if this is the “last” data group given in this `INPMOD` run. 
See also [Termination of input data](@ref inpmod_data_group_a_termination_of_input_data).

~~~
END
~~~




## Data Group F: Floater Force Model Data {#inpmod_f}

This option enables user to perform coupled analysis which means:
simultaneous analysis of vessel motions and mooring line and riser
dynamics.

The vessel load model may account for wind, wave and current forces,
which are applied as nodal loads. For further description of vessel load
model, confer `SIMO`.

Note that his option requires access to the computer program `SIMO`.




###  Data group identifier, one input line {#inpmod_f_data}

~~~
FLOAter FORCe MODEl
~~~




###  Number of SIMO bodies, one input line {#inpmod_f_number}

~~~
NSBODY
~~~

- `NSBODY: integer`: The number of `SIMO` bodies
    - `NSBODY>0`




#### SIMO Body identification, location and optional artificial stiffness {#inpmod_f_number_identification}
These data are specified on input lines 'SIMO Body identification' through 'SIMO Body artificial stiffness' and must be given in one block for
each `SIMO` body.




#####  SIMO Body identification, SIMO body node identification and location option {#inpmod_f_number_identification_body_identification}

~~~
CHBODY CHBODY_NOD_ID CHLOCA_OPT 
~~~

- `CHBODY: character(8)`: `SIMO` Body identification
- `CHBODY_NOD_ID: character(8), default: 'SBDYi'`: Optional `SIMO` body node identifier, where `i` is the `RIFLEX` internal number of the `SIMO` body so that the first `SIMO` body will have a default `SIMO` body node identifer equal to 'SBDY1'.
- `CHLOCA_OPT: character(4), default: 'ELEM'`: Optional `SIMO` body location option
    - `CHLOCA_OPT='ELEM'`: The `SIMO` body location is specified in terms of a line segment element end.
    - `CHLOCA_OPT='NODE'`: The `SIMO` body location is specified in terms of a line segment node.
    - `CHLOCA_OPT='POSI'`: The `SIMO` body location is specified in terms of a position.

`CHBODY_NOD_ID` is the `SIMO` body node identifier which is set automatically 
if not specified by the user. The automatic naming convention
is based on concatenating the character string `'SBDY'` and the `RIFLEX` 
internal number of the `SIMO` body starting at 1 for the first `SIMO` body. 



#####  SIMO Body location, orientation and artificial stiffness option for CHLOCA_OPT='ELEM' {#inpmod_f_number_identification_body_location1}

The input line below must be specified for the option `CHLOCA_OPT='ELEM'`, and whenever `CHBODY_NOD_ID` and `CHLOCA_OPT` is omitted.

~~~
LINE-ID ISEG IEL IEND ROTX ROTY ROTZ IST
~~~

The `SIMO` body is connected to
- `LINE-ID: character(8)`: Reference to line identifier 
- `ISEG: integer`: Local segment number within line 
- `IEL: integer`: Local element number within segment 
- `IEND: integer`: Element end (1 or 2) 

The initial orientation of the `SIMO` body is:
- `ROTX0: real, default: 0`: Rotation around X-axis $\mathrm{[deg\]}$
- `ROTY0: real, default: 0`: Rotation around Y-axis $\mathrm{[deg\]}$
- `ROTZ0: real, default: 0`: Rotation around global Z-axis $\mathrm{[deg\]}$

`ROTX0`, `ROTY0` and `ROTZ0` are the euler angles taken in the order `ROTZ0 -> ROTY0 -> ROTX0`. 

- `IST: integer, default:0`: Artificial stiffness option
    - `IST=0`: No artificial stiffness
    - `IST=1`: Artificial stiffness is specified



##### SIMO Body location, orientation and artificial stiffness option for CHLOCA_OPT='NODE' {#inpmod_f_number_identification_body_location2}

The input line below is specified for the option `CHLOCA_OPT='NODE'` only.

~~~
LINE-ID ISEG ISEGNOD ROTX ROTY ROTZ IST
~~~

The `SIMO` body is connected to
- `LINE-ID: character(8)`: Reference to line identifier 
- `ISEG: integer`: Local segment number within line 
- `ISEGNOD: integer`: Local node within segment 

The initial orientation of the `SIMO` body is:
- `ROTX0: real, default: 0`: Rotation around X-axis $\mathrm{[deg\]}$
- `ROTY0: real, default: 0`: Rotation around Y-axis $\mathrm{[deg\]}$
- `ROTZ0: real, default: 0`: Rotation around global Z-axis $\mathrm{[deg\]}$

`ROTX0`, `ROTY0` and `ROTZ0` are the euler angles taken in the order `ROTZ0 -> ROTY0 -> ROTX0`. 

- `IST: integer, default:0`: Artificial stiffness option
    - `IST=0`: No artificial stiffness
    - `IST=1`: Artificial stiffness is specified



##### SIMO Body position, orientation, boundary conditions and artificial stiffness option for CHLOCA_OPT='POSI' {#inpmod_f_number_identification_body_position3}

The input lines in this section are specified for the option `CHLOCA_OPT='POSI'` only. The first input line reads:

~~~
CHBOUND IST
~~~

- `CHBOUND: character(4), default: FREE`: Boundary condition for all nodal DOFs
    - `CHBOUND='FREE'`: All DOFs for the `SIMO` body node are free
    - `CHBOUND='FIXEd'`: All DOFs for the `SIMO` body node are initially fixed
- `IST: integer, default:0`: Artificial stiffness option
    - `IST=0`: No artificial stiffness
    - `IST=1`: Artificial stiffness is specified


The next input line defines the initial configuration of the `SIMO` body:

~~~
XG0 YG0 ZG0 ROTX0 ROTY0 ROTZ0
~~~
- `XG0: real, default: 0`: Initial global X-coordinate of `SIMO` body node $\mathrm{[L\]}$
- `YG0: real, default: 0`: Initial global Y-coordinate of `SIMO` body node $\mathrm{[L\]}$
- `ZG0: real, default: 0`: Initial global Z-coordinate of `SIMO` body node $\mathrm{[L\]}$
- `ROTX0: real, default: 0`: Initial rotation around X-axis $\mathrm{[deg\]}$
- `ROTY0: real, default: 0`: Initial rotation around Y-axis $\mathrm{[deg\]}$
- `ROTZ0: real, default: 0`: Initial rotation around global Z-axis $\mathrm{[deg\]}$

`ROTX0`, `ROTY0` and `ROTZ0` are the euler angles taken in the order `ROTZ0 -> ROTY0 -> ROTX0`. 


If `CHBOUND='FIXEd'`, an additional input line defining the `SIMO`
body configuration at final static equilibrium must be
included. However, the values must at present be identical to the
values specified for the initial configuration:
~~~
XG YG ZG ROTX ROTY ROTZ
~~~
- `XG: real, default: XG0`: Global X-coordinate of `SIMO` body node at final static equilibrium $\mathrm{[L\]}$
- `YG: real, default: YG0`: Global Y-coordinate of `SIMO` body node at final static equilibrium $\mathrm{[L\]}$ 
- `ZG: real, default: ZG0`: Global Z-coordinate of `SIMO` body node at final static equilibrium $\mathrm{[L\]}$ 
- `ROTX: real, default: ROTX0`: Rotation around X-axis at final static equilibrium $\mathrm{[deg\]}$
- `ROTY: real, default: ROTY0`: Rotation around Y-axis at final static equilibrium $\mathrm{[deg\]}$
- `ROTZ: real, default: ROTZ0`: Rotation around global Z-axis at final static equilibrium $\mathrm{[deg\]}$

`ROTX`, `ROTY` and `ROTZ` are the euler angles taken in the order `ROTZ -> ROTY -> ROTX`. 




##### SIMO Body artificial stiffness {#inpmod_f_number_identification_body_artificial}

This input line is given if `IST=1` only. 

~~~
STX STY STZ SRX SRY SRZ
~~~

- `STX: real, default: 0`: Stiffness in global X-direction $\mathrm{[F/L\]}$
- `STY: real, default: 0`: Stiffness in global Y-direction $\mathrm{[F/L\]}$
- `STZ: real, default: 0`: Stiffness in global Z-direction $\mathrm{[F/L\]}$
- `SRX: real, default: 0`: Stiffness around global X-direction $\mathrm{[FL/deg\]}$
- `SRY: real, default: 0`: Stiffness around global Y-direction $\mathrm{[FL/deg\]}$
- `SRZ: real, default: 0`: Stiffness around global Z-direction $\mathrm{[FL/deg\]}$


The artificial stiffness is applied in static analysis only for improving the 
convergence properties. It does not affect the final static solution.



###  Termination of input data {#inpmod_f_termination}

Do not forget the `END` input line if this is the “last” data group given in this `INPMOD` run. 
See also [Termination of input data](@ref inpmod_data_group_a_termination_of_input_data).

~~~
END
~~~




## Additional Features {#inpmod_af}

This group gives a description of special features that normally are not
used in analysis of flexible riser system.




### Local element axis definition {#inpmod_af_local}

Additional to [Arbitrary system](@ref inpmod_b_arbitrary_arbitrary).

This data group may be used to specify a reference vector that is used
to determine the initial orientation of the local y- and z-axes of
beam elements.

If a local element axis is not specified for an element, the default 
procedure described in 
[Line, line type and supernode connectivity](@ref inpmod_b_arbitrary_line)
is used.

This data group must be given for all elements with a CRS6 cross
section as the reference vector and the element's x-axis define the
net plane during static and dynamic analysis.



#### Data group identifier, one input line {#inpmod_af_local_data}

~~~
LOCAl ELEMent AXIS
~~~




#### Number of input lines for special axis definition, one input line {#inpmod_af_local_number}

~~~
NAXDEF
~~~

- `NAXDEF: integer`: Number of input lines for special axis definition




#### Specification of reference vector for definition of the local axes in the initial configuration, NAXDEF input lines {#inpmod_af_local_specification}

~~~
LINE-ID ISEG IEL RNX RNY RNZ
~~~

- `LINE-ID: character(8)`: Line identifier. 
- `ISEG: character/integer`: Local segment number within line `LINE-ID`
    - `=` ‘`0`’ or ‘ALL’ means all segments in specified line 
- `IEL: character/integer`: Local element number within segment `ISEG`
    - `=` ‘`0`’ or ‘ALL’ means all elements in specified segment `ISEG` 
- `RNX: real`: X-component of the reference vector 
- `RNY: real`: Y-component of the reference vector 
- `RNZ: real`: Z-component of the reference vector

The reference vector is to be given in global system.

The element's local x-axis goes from end 1 to end 2 of the element.

The element's local z-axis is given by the cross product between the
element's local x-axis and the reference vector.

The element's local y-axis is given by the cross product of the local
z-axis and the local x-axis.

The reference vector must not be parallel with the element's initial
x-axis. For CRS6 cable/bar cross sections, the reference vector must be
chosen so that it is not parallel to the element's x-axis during the
static and dynamic analyses.

For beam elements, the element axes are found at the stress-free
configuration and will subsequently follow the element.




### Fish net cross section {#inpmod_af_fish}

Additional to [Data Group C: Component Data](@ref inpmod_c_component_data_data_group_c)


A fish net is subdivided into sections where each section is
represented by a cable/bar element with equivalent properties.

Note that the fish net load model requires that the net plane is
defined. The net plane is the plane containing the updated local
element X-axis and the fixed reference vector specified in the input
group [LOCAL ELEMENT AXIS](@ref inpmod_af_local).



#### Data group identifier {#inpmod_af_fish_data}

~~~
NEW COMPonent CRS6
~~~




#### Component type identifier {#inpmod_af_fish_component}

~~~
CMPTYP-ID TEMP
~~~

- `CMPTYP-ID: character(8)`: Component type identifier 
- `TEMP: real`: Temperature at which the specification applies. In the present version this item serves only as label




#### Mass and volume {#inpmod_af_fish_mass}

~~~
AMS AE
~~~

- `AMS: real`: Mass/unit length $\mathrm{[M/L\]}$
- `AE: real`: External volume per length $\mathrm{[L^2\]}$




#### Stiffness properties classification {#inpmod_af_fish_stiffness_properties}

~~~
IEA
~~~

- `IEA:  integer`: Axial stiffness code
    - `1`: constant stiffness
    - `N`: table with N paris of tension - elongation
    to be specified 2 <= N <= 10




#### Axial stiffness. Case 1 IEA = 1 {#inpmod_af_fish_axial_stiffness_case1}

~~~
EA
~~~

- `EA: real > 0`: Axial stiffness $\mathrm{[F\]}$




#### Axial stiffness. Case 2 IEA = N {#inpmod_af_fish_axial_stiffness_case2}

~~~
EAF(1) ELONG(1) . . . EAF(N) ELONG(N)
~~~

- `EAF(1): real`: Axial force corresponding to relative elongation `ELONG(1)` $\mathrm{[F\]}$
- .
- .
- .
- `ELONG(N): real`: Relative elongation $\mathrm{[1\]}$

`EAF` and `ELONG` must be given in increasing order.




#### Net properties {#inpmod_af_fish_net}

~~~
SN WIDTH1 WIDTH2 REDVEL
~~~

- `SN: real`: Solidity ratio $\mathrm{[1\]}$
- `WIDTH1: real`: Net width at segment end 1 $\mathrm{[L\]}$
- `WIDTH2: real`: Net width at segment end 2 $\mathrm{[L\]}$
- `REDVEL: real`: Reduction factor for current velocity




#### Damping specification {#inpmod_af_fish_damping}

Identical to input for cross-section type CRS1, see data group [Damping specification](@ref inpmod_c_crs1_damping_specification).




#### Hydrodynamic force coefficients {#inpmod_af_fish_hydrodynamic}

~~~
AMX AMY
~~~

- `AMX: real`: Added mass per length, tangential direction $\mathrm{[M/L\]}$
- `AMY: real`: Added mass per length, normal direction $\mathrm{[M/L\]}$




#### Capacity parameter {#inpmod_af_fish_capacity}

~~~
TB YCURMX
~~~

- `TB: real`: Tension capacity $\mathrm{[F\]}$
- `YCURMX: real`: Maximum curvature $\mathrm{[I/L\]}$

These parameters are dummy in the present version.




## Additional Input Files {#inpmod_aif}




### Specification of internal control system for blade pitch and electrical power {#inpmod_aif_specification}




#### Description of internal control system {#inpmod_aif_specification_description}

The implemented control system is based on the choice of a conventional
variable-speed, variable blade-pitch-to-feather configuration wind
turbine and consists of two basic control systems: a generator torque
controller and a full span rotor-collective blade-pitch controller. The
two control systems are designed to work independently. The objective of
generator-torque controller is to maximize power capture below the rated
operation point. The goal of the blade-pitch controller is to regulate
generator speed above the rated operation point.




##### Control measurement filter

Both the generator torque and blade pitch controllers use the generator
speed as the sole feedback input. A recursive, single-pole low-pass
filter exponential smoothing to reduce the high frequency excitation of
the control systems is provided. The discrete time recursion equation
for this filter is

$\mathrm{\omega _{f.k}=\alpha \omega _{f.k-1}+(1-\alpha )\omega _K}$

where

$\mathrm{\alpha =exp((-\Delta t)/(TC))}$

where $\mathrm{\Delta t}$ is the discrete time
step, $\mathrm{TC}$ is the filter time constant,
$\mathrm{\alpha }$ is the low-pass filter
coefficient $\mathrm{\omega _f}$ is low pass
filtered generator speed and $\mathrm{k}$ indicates the time step. The relation
between the filter time constant and the cut off (corner) frequency 
$\mathrm{f_C}$ is given by:

$\mathrm{TC=\frac{1}{2\pi f_C}}$




##### Generator torque controller

The generator torque is computed as a tabulated function of the filtered
generator speed, incorporating five control regions: 1, 1 1/2, 2, 2 1/2
and 3 as illustrated in the figure 'Illustration of the variable speed
controller - Generator torque versus generator
speed' below. Region 1 is
a control region before cut-in wind speed, where the generator torque is
zero and no power is extracted. Instead, the wind is used to accelerate
the rotor for start-up. Region 2 is a control region for optimizing
power capture. Here, the generator torque is proportional to the quare
of the filtered generator speed to maintain a constant (optimal)
tip-speed ratio. In region 3, the generator torque or the generator
power is held constant. In case of constant power the generator torque
is inversely proportional to the filtered generator speed.




##### Blade pitch controller

In region 3, the collective blade pitch angle commands are computed
using a gain-scheduled proportional-integral (PI) control on the speed
error between the filtered generator speed and the rated generator
speed. The PI regulator is represented by the Laplace transform:
$\mathrm{(K(s+a))/s}$ where $\mathrm{K}$ and $\mathrm{a}$ are the
proportional gain and the integrator gain. The corresponding and simple
regulator algorithm is given by

$\mathrm{R(t+\Delta t)=R(t)+\Delta \omega \Delta t}$

$\mathrm{\theta=K_P\Delta \omega +aK_PR(t+\Delta t)=K_P\Delta \omega +K_IR(t+\Delta t)}$

where $\mathrm{\Delta t}$ is the regulator time
step, $\mathrm{\Delta \omega }$ is the rotor speed
error, i.e. the difference between filtered rotor speed and rated rotor
speed. $\mathrm{R}$ is accumulated time integrated speed error which is set to zero
for filtered generator speed less than rated generator speed.
$\mathrm{\theta}$ is the instructed/required
collective blade pitch angle.




##### Gain scheduling

Gain scheduling is introduced because the optimal proportional and
integrator gains are dependent of the blade pitch angle. At each step
the gain will be corrected based on the pitch angle applied in the
previous step. The user may specify a gain scheduling law or choose to
apply the default law presented in the table 'The defaults gain scheduling
law'. For intervening generator speeds, linear interpolation is used.

![Illustration of the variable speed controller - Generator torque versus generator speed](@ref figures/um_ii_fig176.svg)
@image latex figures/um_ii_fig176.pdf "Illustration of the variable speed controller - Generator torque versus generator speed" width=12cm




###### The defaults gain scheduling law

Collective Blade Pitch Angle  | Correction Factor
----------------------------- | -----------------
$\mathrm{[deg\]}$         | $\mathrm{[1\]}$
0.0                           | 1.00
5.0                           | 0.56
10.0                          | 0.39
15.0                          | 0.30
20.0                          | 0.24
90.0                          | 0.05




#### Input description {#inpmod_aif_specification_input}




##### Engine Data, Generator, One input line
~~~
GBRATIO GNS_RATE TRQ_RATE RGN3MP
~~~

- `GBRATIO: real >= 1`: Gear box ratio. Number of rotations of the high speed
shaft for one rotation of the low speed shaft, i.e. generator versus rotor
- `GNS_RATE: real > 0`: Rated generator speed $\mathrm{[rad/T\]}$
- `TRQ_RATE: real > 0`: Rated generator torque $\mathrm{[FL\]}$
- `RGN3MP: real`: Minimum pitch angle for which electrical torque versus generator
speed will stay in region 3 $\mathrm{[deg\]}$




##### Engine Data, Generator One input line
~~~
RGN15SP RGN20SP RGN25SP RGN30SP TRQRGN2
~~~

- `RGN15SP: real > 0`: Transitional generator speed between region 1 and 1 1⁄2.
    Start speed for extracting power. $\mathrm{[rad/T\]}$
- `RGN20SP: real > RGN15SP`: Transitional generator speed between region 1 1⁄2 and 2. $\mathrm{[rad/T\]}$
- `RGN25SP: real > RGN20SP`: Transitional generator speed between region 2 and 2 1⁄2 $\mathrm{[rad/T\]}$
- `RGN30SP: real > RGN25SP`: Transitional generator speed between region 2 1⁄2 and 3 $\mathrm{[rad/T\]}$
- `TRQRGN2: real > 0`: Generator torque constant in region 2$\mathrm{[FL/(rad/T)^2\]}$




##### Engine Data, Generator One input line
~~~
METRGN3
~~~

- `METRGN3: character(6)`: Method for power extraction in region 3
    - `POWER`: Constant Power
    - `TORQUE`: Constant Torque




##### Engine Data, Generator actuator One input line
~~~
TRQ_MAXRAT TRQ_MAX
~~~

- `TRQ_MAXRAT: real > 0`: Maximum torque rate $\mathrm{[FL/T\]}$
- `TRQ_MAX: real > 0`: Maximum electrical torque $\mathrm{[FL\]}$




##### Blade pitch Controller/actuator One input line
~~~
PC_MINPIT PC_MAXPIT PC_MAXRAT
~~~

- `PC_MINPIT: real`: Minimum pitch setting in pitch controller $\mathrm{[deg\]}$
- `PC_MAXPIT: real`: Maximum pitch setting in pitch controller $\mathrm{[deg\]}$
- `PC_MAXRAT: real`: Maximum pitch rate $\mathrm{[deg/T\]}$




##### Controller Data (PI regulator : K(s+a)/s One input line
~~~
KP KI G_SHEDULE TC
~~~

- `KP: real`: Proportional gain at zero pitch angle
- `KI: real`: Integral gain
- `G_SHEDULE: character`: Gain scheduling; Default or Tabulated
    - `= D`: Default
    - `= T`: Tabulated 
- `TC: real`: Time constant for first order low pass filter, $\mathrm{TC=1/\omega }$ $\mathrm{[s/rad\]}$

Input refer to low-speed shaft




##### Gain scheduling (G_SHEDULE=T) One input line
~~~
GSNumber
~~~

- `NOP_GST: integer > 0` : Number of points in gain scheduling table.
The maximum is currently 30.




##### Gain Scheduling; Gain correction factors. NOP\_SGST input lines
~~~
BPITCH GCF
~~~

- `BPITCH: real`: Blade pitch angle $\mathrm{[deg\]}$
- `GCF: real`: Gain correction factor




##### Controller sample interval
~~~
DTSAMP
~~~

- `DTSAMP: real > 0`: Controller sample interval $\mathrm{[T\]}$




##### Example input for control system

~~~

‘                                                                        
'gbratio        gnsrate         trq_rate        rgn3mp                                       
  97            122.911         43.09355         1.0                                                  
'rgn15sp        rgn20sp         rgn25sp         rgn30sp         trqrgn2                                
  70.16         91.208          119.0137        121.6805        0.002332288                               
'metrgn3                                                                
 TORQUE                                                                   
'trq_maxrat     trq_max                                                   
   15.0         43.09355                                                            
'pc-minpit      pc-maxpit       pc-maxrat                                          
  0.            90.             8.                                                               
'kp             ki              g_shedule       TC                                                     
0.006275604     0.000896514     D               0.6366                                            
‘                                                                        
‘dtsamp                                                                  
0.0125                                                                   

~~~




### Interface for external wind turbine control system {#inpmod_extWTcontrol_specification}



#### Control system files needed for RIFLEX simulation {#inpmod_aif_extWTcontrol_files}

The input to RIFLEX for the external wind turbine control system
requires the (path and) name of the executable .jar file, the class to
be used within that .jar file, and the (path and) name of a file which
may contain input data for the external control.
See [Wind turbine specification](@ref inpmod_b_wind_wind_turbine_specification). 
For example, the input may be: 

~~~

'jarName
MyController.jar
'className                                                                  
no.marintek.wind.control.WindTurbineController
'config
ControlInput.txt

~~~



#### Description of control system interface {#inpmod_aif_extWTcontrol_description}

The external control class must contain at least the three main methods 
(init, step, and finish) that are called by RIFLEX. 



##### init

`init` is called once at the beginning of RIFLEX DYNMOD. 
The controller receives input from RIFLEX about the time step, 
number of blades, and the name of the control input file. 


~~~

public void init(double dt, int nblades, String filename)

~~~


##### step

`step` is called at the beginning of each time step in RIFLEX DYNMOD.
The controller receives measurements (rotor velocity, pitch angles,
hub position/velocity/acceleration, instantaneous wind velocity at the
hub, etc.) from RIFLEX and returns feedback (torque to be applied on
the rotor, pitch angle to be applied on each blade, and - for output
purposes - gear shaft rotor speed and generated electrical power).

~~~

public void step(Measurements measurements, Feedback feedback) 

~~~

`measurements` contains:
 
- omega: Rotor velocity $\mathrm{[rad/T\]}$. May be extracted with the Java method getOmega().

- pitch angles: Blade pitch angles for all blades $\mathrm{[rad\]}$. May be extracted with the Java method getPitchAngle(i), i = 0, ..., nblades-1.

- position: (x,y,z,rx,ry,rz) dynamic displacement $\mathrm{[L\]}$
and rotation $\mathrm{[rad\]}$ from final static position /
orientation for the node at the second end of the shaft
flex-joint. Values are in the shaft measurement system described
below. May be extracted with the Java method getPosition().

- velocity: (vx,vy,vz,vrx,vry,vrz) velocity $\mathrm{[L/T\]}$ and
angular velocity $\mathrm{[rad/T\]}$ for the node at the second
end of the shaft flex-joint. Values are in the shaft measurement
system described below. May be extracted with the Java method 
getVelocity().

- acceleration: (ax,ay,az,arx,ary,arz) acceleration $\mathrm{[L/T^2\]}$ and angular acceleration $\mathrm{[rad/T^2\]}$
for the node at the second end of the shaft flex-joint. Values are in
the shaft measurement system described below. May be extracted with
the Java method getAcceleration().

- hub wind: (wix,wiy,wiz) hub wind velocity $\mathrm{[L/T\]}$,
global coordinate system. May be extracted with the Java method
getHubWindVelocity().

- blade root torsional moment around local element x-axis for all
blades $\mathrm{[FL\]}$. May be extracted with the Java method 
getBladeRootBMX(i), i = 0, ..., nblades-1.

- blade root bending moment around local element y-axis for all blades
$\mathrm{[FL\]}$. May be extracted with the Java method 
getBladeRootBMY(i), i = 0, ..., nblades-1.

- blade root bending moment around local element z-axis for all blades
$\mathrm{[FL\]}$. May be extracted with the Java method 
getBladeRootBMZ(i), i = 0, ..., nblades-1.

- aerodynamic torsional moment load around local element x-axis for all
blades $\mathrm{[FL\]}$. May be extracted with the Java method 
getBladeRootAeroTor(i), i = 0, ..., nblades-1.

- nodal measurements for the `NNOD_MEAS` specified nodes. 18 values
for each node: 3 displacements $\mathrm{[L\]}$ and 3 rotations $\mathrm{[rad\]}$ relative to the stress-free configuration, 6
velocities $\mathrm{[L/T\]}$ or $\mathrm{[rad/T\]}$ and 6
accelerations $\mathrm{[L/T^2\]}$ or $\mathrm{[rad/T^2\]}$. The rotations (R1,R2,R3) are taken in the order
R3, R2, R1 ; i.e. first rotation around the global z-axis, then around
the local (rotated) y-axis and then finally around the local (rotated)
x-axis. Global or shaft measurement system as selected by input. May
be extracted with the Java method getAddNodeMeas(i) i, i = 0, ...,
nnod_meas-1. nnod_meas may be extracted with the Java method
getNnodMeas().

- element measurements for the `NEL_MEAS` specified elements. 10
values for each element: effective tension $\mathrm{[F\]}$,
torsional moment $\mathrm{[FL\]}$, My-moment end 1 and 2 $\mathrm{[FL\]}$, Mz-moment end 1 and 2 $\mathrm{[FL\]}$, Qy-shear
force end 1 and 2 $\mathrm{[F\]}$, Qz-shear force end 1 and 2 $\mathrm{[F\]}$. Local element system. May be extracted with the Java
method getAddNelMeas(i), i = 0, ..., nel_meas-1. nel_meas may be
extracted with the Java method getNelMeas().


The shaft measurement system is used for the hub position, velocity
and acceleration measurements and may be chosen for the additional
nodal measurements. This coordinate system is determined from the
stress-free orientation of the shaft element where the electrical
torque is applied.
- the local z-axis is vertical,
- the local x-is the horizontal projection of the element's x axis
- the local y-axis is oriented so that the x-, y- and z-axes are a
right-handed coordinate system (i.e. the y-axis is the vector cross
product of the local z- and x-aces)

If the stress-free orientation of the shaft is in the global X-Z
plane, the shaft measurement coordinate system will coincide with the
global coordinate system.



`feedback` contains:

- Torque request: Actuator torque to apply on rotor axis $\mathrm{[ML^2/T^2\]}$

- Pitch angle request for all blades: Controller pitch angle $\mathrm{[rad\]}$

- Gear shaft omega: Gear shaft rotor speed $\mathrm{[rad/T\]}$
Used for presentation only.

- Generated power: Generated electrical power $\mathrm{[kW\]}$
Used for presentation only.



##### finish

`finish` is called at the end of the simulation and primarily serves to close files. 

~~~

public void finish()

~~~



### Airfoil library file {#inpmod_aif_airlib}

The airfoil library file contains the coefficient data required for
aerodynamic calculations. All of the airfoils which are referred to
must be included in a single file; i.e. whether or not they are part
of a wind turbine. The airfoils may be listed in any order. Airfoils
which are not referred to will be ignored.

Comment lines may be included on any line, as in other input
files. Blank lines between airfoils will at present be ignored, but it
is recommended to use comment lines instead. Blank lines at other
locations in the file will be interpreted as input lines and the
default values will be used.

For each airfoil, the following data groups must be given.


#### Airfoil identifier {#inpmod_aif_airlib_airname}
~~~
CHAIRF
~~~

- `CHAIRF: character(64)`: Name of the airfoil


#### Airfoil table extension parameters {#inpmod_aif_airlib_extpar}
~~~
IATEXT ATAIL1 ATAIL2 ANOSE1 ANOSE2 RNOSEC
~~~

- `IATEXT: integer`: Flag for extending the table to deep stall regime
    - `= 1`: Extend the table
    - `= 0`: Do not extend the table
- `ATAIL1: real`: tail angle between a line perpendicular to the flow 
and the line from the tip of the wedge, low (negative) angles of attack  $\mathrm{[deg\]}$
- `ATAIL2: real`: as ATAIL1, but for high (positive) angles of attack $\mathrm{[deg\]}$
- `ANOSE1: real`: nose angle between a line perpendicular to the flow 
and the line from the tip of the wedge, low (negative) angles of attack $\mathrm{[deg\]}$
- `ANOSE2: real`: as ANOSE1, but for high (positive) angles of attack $\mathrm{[deg\]}$
- `RNOSEC: real`: ratio of the nose radius to the chord of the airfoil $\mathrm{[1\]}$


#### Airfoil table size parameters {#inpmod_aif_airlib_sizpar}
~~~
NRE NGEO DSIN
~~~

- `NRE: integer`: Number of Reynolds numbers with coefficient data
- `NGEO: integer, default: 0`: number of points describing the airfoil geometry
- `DSIN: integer, default: 0`: flag for user-defined dynamic stall initialization
parameters
    - `= 1`: User-defined dynamic stall initialization parameters will be given below
    - `= 0`: No user-defined dynamic stall initialization parameters will be given


#### Airfoil data {#inpmod_aif_airlib_airdat}
One block per Reynolds number, i.e. NRE data blocks 

If only one block is given, the data will be used for all Reynolds
numbers. For Reynolds numbers outside the range of Reynolds numbers
given, the data for the closest Reynolds number will be used;
i.e. flat extrapolation.


##### Reynolds number

~~~
RE NAOA
~~~

- `RE: real`: Reynolds number for this block $\mathrm{[1\]}$
- `NAOA: integer`: number of angle-of-attack points for this data block


##### Dynamic stall initialization parameters {#inpmod_aif_airlib_ds}
To be given only if `DSIN`=1

~~~
AOA0 DCLDA1 DCLDA2 AOAFS1 AOAFS2
~~~

- `AOA0: real`: the angle of attack where there is zero lift, upcrossing $\mathrm{[deg\]}$
- `DCLDA1: real`: maximum slope of the lift curve in the 
linear region above AOA0 $\mathrm{[1/deg\]}$
- `DCLDA2: real`: maximum slope of the lift curve in the 
linear region below AOA0 $\mathrm{[1/deg\]}$
- `AOAFS1: real`: angle of attack corresponding to full separation above AOA0 $\mathrm{[deg\]}$
- `AOAFS2: real`: angle of attack corresponding to full separation below AOA0 $\mathrm{[deg\]}$

The dynamic stall initialization parameters are shown in the figure 
'Illustration of dynamic stall initialization parameters' below. 

![Illustration of dynamic stall initialization parameters](@ref figures/dynstall_param.svg)
@image latex figures/dynstall_param.pdf "Illustration of dynamic stall initialization parameters" width=12cm




##### Aerodynamic coefficients  {#inpmod_aif_airlib_coeff}
NAOA input lines

~~~
AOA CL CD CM
~~~

- `AOA: real`: angle of attack $\mathrm{[deg\]}$
- `CL: real`: non-dimensional lift coefficient $\mathrm{[1\]}$
- `CD: real`: non-dimensional drag coefficient $\mathrm{[1\]}$
- `CM: real`: non-dimensional moment coefficient $\mathrm{[1\]}$


#### Normalized airfoil geometry {#inpmod_aif_airlib_airgeo}
NGEO input lines, to be given only if `NGEO > 0`.  
Airfoil coordinates are normalized by the chord length,
with the origin at the aerodynamic reference point. Points around the full 
airfoil should be given, i.e. several lines may have the same `XGEO` and 
different values for `YGEO`.

~~~
XGEO YGEO
~~~

- `XGEO: real`: x coordinate of geometry point, normalized by chord length. 
- `YGEO: real`: y coordinate of geometry point, normalized by chord length. 
