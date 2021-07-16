# RIFLEX Release Notes
:sectnums!:


## RIFLEX 4.20.0 (2020-XX-XX)

Initial release `RIFLEX` 4.20.


### RIFLEX 4.20.0 New / improved functionality


#### Nacelle yaw control (Under development)

Nacelle yaw control is implemented. 
The controller rotates the entire rotor-nacelle assemble (RNA),
aligning it with the mean wind direction.


#### Coriolis centripal loads.

Coriolis centripetal load has been added for general cross sections CRS7, i.e. the
effect of rotational speeds about 2 local element axes that gives rise to moment
about the 3rd axis. This functionality was mainly implemented for analysis of
operational wind turbines. It is normally insignificant for analysis with moderate
dynamic rotational speeds; e.g. normal riser analysis.



#### Structural damping improvements

The cross sectional damping specified in `INPMOD` can now differ for axial, torsional and bending
dofs in `VIVANA`.

The curvature-related damping specified in `VIVANA` is  applied to local bending only.



#### Input to the internal wind turbine controller

The input to the internal wind turbine controller is now read with the
FREAD package which is used for other RIFLEX input.



#### Visualization of regular wave 

Visualization of regular wave is enabled.

The visualization is an approximation of the input wave used in the analysis.
A single component wave spectrum is used to generate the wave and slight deviation in period may occur. 


### RIFLEX 4.20.0 Corrected errors


#### Mass-proportional damping

If the added mass of an attached body is given in the global system, it has
not contributed to the Rayleigh mass-proportional damping.

Also, the MacCamy & Fuchs added mass from radiation force and the added mass at infinite
frequency from potential wave flow theory have not contributed to the Rayleigh
mass-proportional damping. 

This is corrected and these contributions are now included.

Note that mass-proportional damping should be used with caution as it will give
damping for long response periods.



### RIFLEX 4.20.0 Known issues

No known issues in the 4.20.0 version.



### RIFLEX 4.20.0 Input changes

Most input files used in version 4.18 can be used unchanged. The
exceptions are described below.


#### External wind turbine pitch controller

The input to external wind turbine pitch controller is changed in version 4.19.1.


#### Removed some unit-dependent default values

Removed the default values for
- air density (AIRDEN) and
- water density (WATDEN) in the ENVIRONMENT CONSTANTS data group in INPMOD
- minimum yield stress (SMYS) and
- modulus of elasticity (EMOD) in the CODE CHECK CURVES data group in OUTMOD.
The user must now specify these values.

The previous default values for AIRDEN and WATDEN were only valid if
the units 'm' and 'kg' are used.

The previous default values for SMYS and EMOD were only valid if the
units 'm' and 'kN' are used.



### RIFLEX 4.20.0 Removed functionality

No previously available functionality have been removed in this
version.



### RIFLEX 4.20.0 Deprecated functionality

No functionality is deprecated in this version.



## RIFLEX licensing

`RIFLEX` is license-managed using the FLEXlm / FLEXlnet software license
management system. If you want `RIFLEX` to be used from any networked
computer on your site, you must run a license manager on a server in your
network. Alternatively, `RIFLEX` may be run on a single computer using a
standalone license file.

**Please note that version 4.2 and higher requires a licence file with
a feature version that is equal or larger than the link date.**

In order to issue a server license or a standalone license file,
SINTEF Ocean or DNV GL needs the following info on your server:

-   License type (server or standalone)

-   Operating system and version (Windows 7, Windows XP, HP-UX and
Linux currently supported)

-   MAC address / FLEXlm hosted of the computer.

Your IT-staff is probably already familiar with this procedure as FLEXlm
is used by a large number of other applications (e.g. Matlab).



## RIFLEX version numbers

The version number consists of three numbers separated by periods,
e.g. 4.16.0. The two first are the version. The third is updated for
each subsequent (bug fix) release.

Even numbered versions, e.g. 4.14, 4.16, are reserved for official
versions.

Odd numbered versions, e.g. 4.15, 4.17, are reserved for development
versions. The next official release will therefore be 4.22.



## RIFLEX 4.18.2 (2020-XX-YY)

Bugfix release of `RIFLEX` 4.18.


### RIFLEX 4.18.2 New / improved functionality


#### Maximum number of arrays in ifndyn

Increase maximum arrays in ifndyn to 100million.



### RIFLEX 4.18.2 Corrected errors


#### MacCamy-Fuchs loads for regular waves given as a tabulated spectrum 

When MacCamy-Fuchs wave loads were calculated for a regular wave given as a tabulated
wave spectrum, numerical inaccuracies could lead to the wave frequency being missed
in the calculations. This resulted in the MacCamy-Fuchs loads being zero. 

Error since RIFLEX 4.18.1, but also present in 4.16.7. The error has been corrected.
Some changes in results may occur. The changes will be insignificant if the length
of the pre-generated wave time series is reasonably long.



#### Effect of eccentric mass center on inertia forces not always included

Morison hydrodynamic loads had to be specified to include the effect of
eccentric mass center in calculating inertia forces.

It is in general allowed to specify no hydrodynamic forces

The error applied to lumped formulation only.  



#### Potential flow library file name

The potential flow library file name can now start with slash.



## RIFLEX 4.18.1 (2020-06-01)

Bugfix release of `RIFLEX` 4.18.



### RIFLEX 4.18.1 New / improved functionality


#### Improved MacCamy-Fuchs wave load generation

The performance in pre-generation of MacCamy-Fuchs wave loads has
been significantly improved.



## RIFLEX 4.18.0 (2020-03-23)

Initial release `RIFLEX` 4.18.


### RIFLEX 4.18.0 Known issues


### RIFLEX 4.18.0 New / improved functionality



#### Implementation of fibre rope characteristics

The SYROPE model for fibre ropes has been implemented in the new cross section
component FIBR.

Reference:
Falkenberg et. al.: The SYROPE Method For Stiffness Testing Of Polyester Ropes. In:
Proc. of the ASME 2018 37th International Conference on Ocean,
Offshore and Arctic Engineering (OMAE). 2018



#### Requirements to identical wind turbine blades

The requirement to identical blades in a wind turbine model have been
relaxed. The wind turbine blades have still to be identical with
regarding the element distribution, foil profile description and
aerodynamic coefficients along the blades. However, the mass and
stiffness distribution may be different.



#### Improved Rayleigh damping

An option to apply stiffness proportional damping based on material
stiffness only has been implemented.  This option should be used for
wind turbine blades because the geometric stiffness will introduce
damping of the rigid body motion. This will also ensure symmetrical
behaviour of the blades when constant Rayleigh damping is specified.



#### Improve name on output signal `Electrical generator torque`

A signal named `Electrical generator torque` is a part of the Wind
Turbine output.  This is however not on the high speed shaft, but on
the low speed shaft.

The name is changed from `Electrical generator torque` to `Mechanical
generator torque on LSS`



#### Interpolation and extrapolation of airfoil coefficients

Airfoil coefficients may now be given for a single Reynolds
number. They will then be used for all Reynolds numbers.

Extrapolation outside the range of Reynolds values given will now be
allowed. The value for the closest Reynolds number will be used;
i.e. flat extrapolation.



#### More efficient import of airfoil library

The import of the airfoil library for foil load coefficients has been
improved. This will reduce the analysis time for both static and
dynamic analysis. The reduction will be most noticeable in static
analysis.



#### Choice of method for generating random numbers

The algorithm for generating pseudo-random numbers may be selected by
the user. The "mersenne twister" is the recommended method and should
be used unless backwards compatibility with previous versions is
required. Note that the default value may change in a future
release. The choice of random number generator will apply to:
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




### RIFLEX 4.18.0 Input changes


#### Rayleigh damping

Stiffness-proportional damping was previously based on only the material stiffness for elements that were
- axisymmetric cross section (CRS1) specified with with hysteresis generated by an internal friction moment at reversed curvature
- general cross section (CRS7)

To reproduce dynamic results for models containing either of these, the stiffness contribution to damping has to be specified as based
on the material stiffness only.



#### Input to the internal wind turbine controller 

The input to the internal wind turbine controller is now checked more
thoroughly. Some input that was previously accepted gave errors in the
subsequent analysis. Illegal input will now give an error message and
program termination.




### RIFLEX 4.18.0 Corrected errors



#### MacCamy-Fuchs radiation contribution from dry elements

Corrected an error that caused MacCamy-Fuchs radiation forces (inertia and
dissipation forces due to specified added mass and damping coefficients) to
contribute even for elements above the mean water level (dry elements).



#### Abrupt stop during generation of second order waves

Corrected an error that could cause abrupt stop during generation of long
second order wave time series.



#### Possible error in hydrodynamic loads for simulations without current

In rare cases without current, uninitialized values could occur for
current velocity at the nodes. These could potentially result in
incorrect hydrodynamic loads in dynamic simulations and thus to
incorrect dynamic results.

The error was avoided if a current with zero velocity was included in
the simulation.

Longstanding error



#### Coupled analysis with 6-dof SIMO body and only bar elements

Corrected an error in coupled analysis when a 6-dof SIMO body is
attached to an element system that only contains bar elements. The
error could cause overwriting of nodal coordinates and give incorrect
results.

No error if at least one element in the system has bending stiffness,
for example if a stiff beam element was used to connect the SIMO body
to the rest of the element system.

Error since RIFLEX 4.16.0.


#### Tabulated wave spectrum with more than 4 values

Corrected the error that meant that only the first four values of a
tabulated wave spectrum were used.

Error since RIFLEX 4.10 (2017-03-21).



#### Boundary change in the first step of static analysis

If a boundary change was used to change a master node from fixed to
free on the first step of static analysis, the slave nodes would end
up with the same coordinates as the master node.

Longstanding error.



#### MacCamy & Fuchs wave excitation load with simplified radiation load model

The damping contribution to the radiation load was not included. This
has been fixed.  Both the added mass and damping terms now contribute
to the radiation loads.

Error since RIFLEX 4.14.0.



#### Avoid NaN from Torsethaugen wave spectrum

The peakedness factor gamma in Torsethaugen spectrum is restricted to
be greater than, or equal to, 1.0 since lower values caused an illegal
numerical operation and result in NaN in results. The problem has been
encountered for seastates with extremely small significant wave
height.

Long-standing error



#### Riflex specified inner pressure always applied at end 1

The inner pressure is now applied at end 2 if specified.  The pressure
can be changed for more than one MRL.



#### Time domain VIV loads and inconsistent units (restricted functionality)

The time domain VIV loads were incorrect if inconsistent mass and
force units were used, i.e. GCONS different from 1.0.  The error would
normally be obvious, e.g. with the units kN and kg, GCONS is 0.001 and
the applied loads were too large by a factor of 1000.

The error was avoided when running in SIMA as SIMA always uses a
consistent set of units.

Error since RIFLEX 4.14.0.



#### In-line term of the time domain VIV loads (restricted functionality)

The in-line term of the time domain VIV loads has been calculated
using the relative velocity at the first end of the element at both
ends. This has been corrected.

Note that the time domain VIV load model is currently restricted
functionality and that a license is required.

Error since RIFLEX 4.14.0.




## RIFLEX 4.16.4 (2020-03-03)

Bugfix release with minor corrections and improvements.


### RIFLEX 4.16.4 Corrected errors


#### Coupled analysis with 6-dof SIMO body and only bar elements

Corrected an error in coupled analysis when a 6-dof SIMO body is
attached to an element system that only contains bar elements. The
error could cause overwriting of nodal coordinates and give incorrect
results.

No error if at least one element in the system has bending stiffness,
for example if a stiff beam element was used to connect the SIMO body
to the rest of the element system.

Error since RIFLEX 4.16.0.




## RIFLEX 4.16.3 (2020-02-06)

Bugfix release with minor improvements.



### RIFLEX 4.16.3 New / improved functionality


#### Interpolation and extrapolation of airfoil coefficients

Airfoil coefficients may now be given for a single Reynolds
number. They will then be used for all Reynolds numbers.

Extrapolation outside the range of Reynolds values given will now be
allowed. The value for the closest Reynolds number will be used;
i.e. flat extrapolation.



#### More efficient import of airfoil library

The import of the airfoil library for foil load coefficients has been
improved. This will reduce the analysis time for both static and
dynamic analysis. The reduction will be most noticeable in static
analysis.



### RIFLEX 4.16.3 Corrected errors


### Tabulated wave spectrum with more than 4 values

Corrected the error that meant that only the first four values of a
tabulated wave spectrum were used.

Error since RIFLEX 4.10 (2017-03-21).




## RIFLEX 4.16.2 (2019-11-12)

Bugfix release with RIFLEX corrections.



### RIFLEX 4.16.2 Corrected errors


#### MacCamy & Fuchs wave excitation load with simplified radiation load model

The damping contribution to the radiation load was not included. This
has been fixed.  Both the added mass and damping terms now contribute
to the radiation loads.

Error since RIFLEX 4.14.0.



## RIFLEX 4.16.1 (2019-08-12)

Bugfix release with `RIFLEX` and `SIMO` corrections.



### RIFLEX 4.16.1 New / improved functionality


#### Linearized time domain simulation with Simo elements

Simo body system elements, i.e. Floater Forces Model Data, may now be used in
linearized time domain simulations.

This is a new implementation and should be used with caution.



### RIFLEX 4.16.1 Corrected errors


#### Hydrodynamic interaction between SIMO bodies

Corrected an error that caused restriction in the number of SIMO bodies that
could interact hydrodynamically. The simulation failed if the number of bodies
was larger than 3.



#### Dynamic Current Variation

Corrected an error that caused simulations with dynamic current
variation to fail unless the selected environment contained at least
one irregular wave.

Long-standing error.




## RIFLEX 4.16.0 (2019-05-06)

Initial release of `RIFLEX` 4.16.




### RIFLEX 4.16.0 Known issues


#### Wave kinematics at updated position in coupled analysis

Currently, the FFT wave method must be selected in `SIMO` to allow
wave kinematics at updated position to be used in `RIFLEX` for a
coupled analysis.



#### Main Riser Line inner pressure

The Main Riser Line (MRL) input allows the pressure to be specified at
either end of the MRL. The specified inner pressure is, however,
always applied at end 1 of the MRL. This will give errors in true wall
tension and some stress components calculated in OUTMOD.

Long-standing error.



#### Specified loads at nodes with skew boundary conditions

Specified nodal loads at nodes with user-defined skew boundary
conditions are not handled correctly. The loads in the global
directions are applied in the skew system. A warning is written to the
.res file.

Nodes connected to a flex-joint will have degrees of freedom in a skew
system. Specified loads at these nodes are not handled correctly. An
error message will be written to the .res file and the analysis
stopped.




### RIFLEX 4.16.0 New / improved functionality


#### Visualization of airfoil profiles

Visualization is now enabled also for foil profiles not part of a wind
turbine. The foil profiles have all to be described in a
airfoil-library file.



#### Time domain fatigue calculations in OUTMOD

A thickness correction based on a reference thickness and an exponent
may now be included in the calculation of the fatigue capacity.

The calculated fatigue damage is now printed on the _outmod.mpf file.

The user may now specify an identifier for the fatigue calculations
and may also specify all segments / elements / ends for fatigue
calculations.

The criteria for skipping fatigue calculations and print at the first
end of elements has been modified. Fatigue is now always calculated
for all locations specified in OUTMOD. If fatigue is calculated for
all elements with stored forces; i.e. NSECT = 0; fatigue calculation
at the first end of an element is skipped if calculation was performed
at the second end of the neighbouring element in the same segment.

Previously, fatigue was only calculated at the first end of the first
element with fatigue calculation in each segment. As forces may not be
stored for all elements within a segment, this may skip more nodes
than intended.



#### OUTMOD input array size

The size of the integer and real input arrays in OUTMOD has previously
been fixed to 1000 and 500 places. This is now increased to a minimum
of 10000 and 6000 places and will be linearly increased if the OUTMOD
work array size is larger than the default size.

This change decreases the available space for other arrays and may
cause a previously successful OUTMOD run to fail. Increasing
RIFLEX_OUTMOD_MEM by one (million Bytes); e.g. from the default 32 to
33; will solve this.



#### External wind turbine controller measurements

The coordinate system for the measurements is now based on the
stress-free orientation of the shaft element where the electrical
torque is applied. It was previously based on this element's
orientation at the end of static analysis.  No change in results
unless the shaft rotates around the global z-axis during the static
analysis.

A minor change has been made to the additional nodal measurements for
an external wind turbine controller that were added in RIFLEX
4.14.0. The nodal rotations are changed from the updated orientation
of the neighbouring element to the rotations of the specified node
from the stress-free to the current orientation.



#### Wave loads on elements

The case that wave loads on elements are specified but no points for
computation of wave kinematics are detected, will no longer lead to
controlled program termination.



#### Extended specification of pre-curved line type

Transverse offsets may now also be specified for the second end of the
last segment within a line type.  See [Transverse offset
specification](@ref inpmod_b_line_transverse) in INPMOD.



#### Boundary change for supenodes

Boundary change may be specified directly for a supernode. This is in
addition to the existing boundary change for local segment nodes.



#### Simo body system element

The Simo body system element is introduced to make it possible to
acount for hydrodynamic interaction between bodies in a Riflex
"coupled" analysis. The element nodes are of Simo body type, a new
type of supernode. One Simo body is automatically attached to one simo
body node having the same number of degrees of freedom as the Simo
body. The Simo body system element may have one or more simo body
nodes dependig how many bodies that interact.

The simo body supernode may be attaced to any already existing
FE-node, or be used as master in a rigid super node connection.



#### New file format for external dynamic nodal forces

The nodal forces can be given in a column format.



#### Rigid supernode connections in linear time domain analysis

Rigid supernode connections may now be used in in linear time domain
analysis



#### Visualization for linear time domain analysis

Visualization is enabled for linear time domain analysis.



#### Bash shell script for running coupled analysis

A Bash shell script for running a complete coupled analysis has been
added to the share/bin folder.




### RIFLEX 4.16.0 Corrected errors


#### Eccentric mass center CRS7 (General Cross Section)

Error in system set up. Local line segment number used instead of global segment
number for eccentric mass center; Cross sections of type CRS7.

This caused incorrect results if eccentric mass was specified for CRS7
cross-sections on lines other than the first line specified. The error has been
corrected.

Error since 4.10.0



#### No wave forces in combination with export for visualization

The combination of no wave forces acting on elements and export for
visualization leads to uncontrolled program termination. The error
has been corrected.



#### Nodal component at end 2 in linear time domain

Include loads for nodal components at end 2 of a segment in linear
time domain simulation. These were previously not included if the
segment had more than one element.

Long-standing error



#### Potential flow and MacCamy-Fuchs loads

Neither Potential flow loads nor MacCamy-Fuchs loads are currently
implemented for regular wave analysis. The is now checked and DYNMOD
will give an error message and stop.

An alternative is to replace the regular wave with a tabulated
("numerical") wave spectrum with a single frequency component.



#### Kinematic viscosity in air is changed

The default value for viscosity in air is set to 1.516E-5, air
temperature 20 degree centigrades.



#### Error in boundary change during parameter variation in static analysis

Error in static analysis if boundary change was specified during
parameter variation.  The error normally caused program termination,
but could give error in results if the energy norm was used for
solution accuracy.

Error since 4.12.0



#### Error in boundary change during parameter variation in static analysis

Error if a node is specified to become a slave node during static
parameter variation.

Long-standing error



#### IEC extreme wind events with detailed specification

Corrected an error in the initialization of the IEC 2005 wind events
    - extreme vertical wind shear, EWSV
    - extreme horizontal wind shear, EWSH
    - extreme operating gust, EOG
    - extreme direction change, EDC
The wind events were incorrectly initialized when defined by a
detailed specification; i.e. velocity or direction change and event
duration. The error resulted in the event duration being zero and no
change in wind.

Error since RIFLEX 4.12.0.



#### IEC extreme wind events for wind turbine class S

Corrected an error in the initialization of the IEC 2005 wind events
for wind turbine class S. The expected turbulence intensity, Iref, was
incorrectly set to the reference wind speed, Vref.

Error since RIFLEX 4.12.0.



#### Error in time domain fatigue for systems with only bar elements

Corrected an error in fatigue calculations for systems with only bar
elements.

Long-standing error.



#### Correct echo of Froude-Krylov scaling factor for time domain VIV

The echo on the _inpmod.res file of the Froude-Krylov scaling factor
in the normal direction was incorrectly identified as in the
tangential direction.

Note that the time domain VIV load model is currently restricted
functionality and that a license is required.

Error since RIFLEX 4.14.0.



#### Time domain VIV loads and consistent formulation (restricted functionality)

The time domain VIV loads may now be used with consistent mass / load
formulation.

Note that the time domain VIV load model is currently restricted
functionality and that a license is required.

Error since RIFLEX 4.14.0.




### RIFLEX 4.16.0 Input changes

Most input files used in version 4.14 can be used unchanged. The
exception is described below.



#### Coupled analysis with IUPPOS = 0

The option IUPPOS = 0, hydrodynamic loads calculated with lines kept
fixed in static position and no update of surface penetration, is no
longer available for analyses with SIMO bodies.



### RIFLEX 4.16.0 Removed functionality

No previously available functionality have been removed in this
version.




### RIFLEX 4.16.0 Deprecated functionality


#### Default values for air and water density (INPMOD)

The default values for air and water density in the ENVIRONMENT
CONSTANTS data group in INPMOD will be changed. The current default
values of 1.3 and 1025 for air and water respectively are only
applicable if the units 'm' and 'kg' are used.

In RIFLEX 4.18.0, the current default values will be used if 'kg' is
specified for the mass unit. Alternative default values will be used
if 'Mg' is specified. For other mass unit names, teh air and water
density must be specified by thee user.



#### Default values in CODE CHECK CURVES (OUTMOD)

Two default values will be removed in the OUTMOD data group CODE CHECK
CURVES in RIFLEX 4.18.0.
- minimum yield stress, SMYS, and
- modulus of elasticity, EMOD.

The current default values of 220.0E3 and 2.1E8 are only applicable if
the units 'm' and 'kN' are used.



#### CARISIMA riser-seafloor contact (restricted functionality)

The CARISIMA riser-seafloor contact is deprecated and will be removed
in the future.



#### Old OUTMOD fatigue data group

The old, undocumented OUTMOD data group TIME FATIGUE LIFE
will be removed following the 4.16 release.

The OUTMOD data group TIME FATIGUE DAMAGE should be used instead.




## RIFLEX 4.14.0 (2018-11-01)


### RIFLEX 4.14.0 New / improved functionality


#### Scaling of tangential Froude-Krylov loads

A scaling factor for the tangential Froude-Krylov load term has been
added for Morison or potential flow loads. The scaling factor is
available for the CRS0, CRS1, CRS2 and CRS7 cross-sections.

The option to specify no hydrodynamic loads has also been added for
these cross-sections.



#### MacCamy & Fuchs - Simplified radiation force

The input is extended in order to make the loads on bottom-fixed cylindrical
monopiles to be applicable for floating single column systems by including
a simple load model representing the radiation forces.

The (horizontal) radiation loads will be based on an added mass
coefficient and a damping coefficient, AMY and DAMP.

In the vertical direction the wave excitation forces is calculated in
a similar manner as the corresponding load term in the Morison
equation. A user specified added mass coefficient will be input and
used for the vertical direction, CAX.


Example of input (with default values):

~~~
'------------------------------------------------------
'chtype
MACF
'------------------------------------------------------
'cqx             cqy             cax  icode hydrod
 0.550000000e+00 9.000000000e-01  0.    2     /
'
'Simplified radiation force:
'amy damp
 0.0 0.0
'------------------------------------------------------
~~~

Note that the extension of the MacCacmy & Fuchs input in Riflex 4.14.0
is not compatible with earlier versions.



#### External wind turbine controller

Additional nodal or element responses may now be made available as
additional measurements to an external wind turbine controller. This
functionality is currently under implementation.



#### Irregular simulation with vessel transfer function NONE

Irregular simulations with vessel transfer function NONE are now
permitted. The vessel motions must be read from file or not be
applied, i.e. the irregular motion indicator must be FILE or NONE.



#### The Wind turbine BEM code

The BEM code has been made less time-consuming. Automatic reshaping
of matrices when calling subroutines have been avoided.



#### Hydrodynamic loads based on potential theory

Improved memory handling to avoid program termination for analyses
with large amount of input data.



#### 3D seafloor geometry file

Improved accuracy for 3D grids with very short distances between grid
points. Improved data checking and warnings when reading the seafloor
geometry file.




### RIFLEX 4.14.0 Corrected errors



#### Error in water plane stiffness for lumped loads

The water plane stiffness was zero if current was present and the
element crossing the water line did not have attached nodal components.

Long-standing error.

Minor changes in convergence for cases with lumped formulation and
current are expected.



#### Low frequency motions from file

Corrected a long-standing error for low frequency vessel motions from
file. The specified low frequency motions were only applied if wave
frequency motions were also specified.



#### External wind turbine controller

Corrected the calculation of the "measurement" accumulated aerodynamic
torsional load which is made available to external wind turbine
controllers. Previously, the accumulated global x-moment was exported
to the control system.

No error in applied aerodynamic loads.

Error since 4.12.0.




### RIFLEX 4.14.0 Known issues


#### Wave kinematics at updated position in coupled analysis

Currently, the FFT wave method must be selected in `SIMO` to allow
wave kinematics at updated position to be used in `RIFLEX` for a
coupled analysis.



#### Main Riser Line inner pressure

The Main Riser Line (MRL) input allows the pressure to be specified at
either end of the MRL. The specified inner pressure is, however,
always applied at end 1 of the MRL. This will give errors in true wall
tension and some stress components calculated in OUTMOD.

Long-standing error.




### RIFLEX 4.14.0 Input changes


#### MacCamy Fuchs loading

The MacCacmy & Fuchs input has been changed in RIFLEX 4.14.0. Old
input must be updated.

Example of input (with default values):

~~~
'------------------------------------------------------
'chtype
MACF
'------------------------------------------------------
'cqx             cqy             cax  icode hydrod
 0.550000000e+00 9.000000000e-01  0.    2     /
'
'Simplified radiation force:
'amy damp
 0.0 0.0
'------------------------------------------------------
~~~





### RIFLEX 4.14.0 Removed functionality

No previously available functionality have been removed in this
version.




### RIFLEX 4.14.0 Deprecated functionality

No functionality is deprecated in this version.





## RIFLEX 4.12.5


### RIFLEX 4.12.5 Corrected errors


#### Avoid array overwriting in dynmod

Avoid overwriting the beginning of the array containing element forces
and moments in nonlinear time domain simulation. The values for the
first seven elements were temporarily zero during the time step. No
consequence for normal analyses as the correct values were used in the
calculation of geometric stiffness and in reporting.




## RIFLEX 4.12.3


### RIFLEX 4.12.3 Improved functionality


#### Increase the model size that can be read by INPMOD

The maximum number of DMS arrays is increased from 10503 to 20003 to
allow larger models to be read by INPMOD. The INPMOD work array size is
increased to 2 million integer words.




### RIFLEX 4.12.3 Corrected errors


#### Error for SIMO generic external control systems in Coupled models

An error introduced in version 4.12.0 made it impossible to run
generic external control systems in a `RIFLEX` Coupled model. This has
now been resolved.



#### Application of marine growth

Restrict application of marine growth to CRS0, CRS1, CRS2. CRS3, CRS4
and CRS7 cross-sections. Volume loads and Morison hydrodynamic loads
will be modified. The modifications are calculated with the assumption
that the cross-section is circular.

The modification of Morison coefficients is now based on the increase
in hydrodynamic diameter so that it is consistent with the initial
non-dimensional coefficients.

Numerical errors and not-a-number ("NaN") results are avoided by
skipping modification of the volume loads if the external area is
zero.

Modification of the Morison coefficients is skipped if the initial
hydrodynamic diameter is zero.




## RIFLEX 4.12.2


### RIFLEX 4.12.2 Corrected errors


#### Error when calculating eigenvalues for model with SIMO bodies

An error has been fixed where `RIFLEX` would crash when eigenvalues
was calculated for a model with `SIMO` bodies (coupled model).

Error since 4.12.0.



#### Application of marine growth

The drag coefficients are corrected for marine growth.



#### Error exit for MacCamy-Fuchs loads and a wave condition containing swell

The MacCamy-Fuchs loads are only calculated for the wind-sea part of a
wave condition. An error exit is therefore added if a wave condition
containing swell is specified for a case with MacCamy-Fuchs loads.




## RIFLEX 4.12.1


### RIFLEX 4.12.1 Corrected errors


#### Application of marine growth

The application of marine growth in static analysis for systems with
non-consistent units has been corrected. No error for analyses with
consistent units; i.e. gcons = 1.0.

The error caused the volume loads of the whole system to be scaled by
a factor of 1/gcons when growth was applied in static analysis. As the
typical value of gcons for non-consistent units is 0.001, the error
gave clearly non-physical results.

The error occurred even if a growth scaling factor of zero was
specified.



#### Wave kinematics at updated position in coupled analysis

Wave kinematics may now be calculated at updated dynamic positions in
a coupled simulation. This resulted in an error exit from `RIFLEX`
`DYNMOD` in 4.12.0.



#### Hydrodynamic loads based on potential theory

Error corrections and enhanced funtionality to allow for swell and
short-crested waves. The functionality is currently under testing.



## RIFLEX 4.12.0



### RIFLEX 4.12.0 New / improved functionality


#### Wind turbine response storage

Wind turbine response storage is available based on user input specification.



#### MacCamy-Fuchs wave loads

The drag force input specification has been expanded to allow for dimensional
drag force coefficients.



#### Energy convergence criterion

A convergence criterion based on energy has been implemented in
Stamod and Dynmod. The rotational degrees of freedom are included,
as opposed to the existing displacement convergence criterion.
The new convergence criterion is approximate because the unbalanced loads refer
to the configuration at the previous equilibrium iteration. Hence, false
convergence may occur for problems with oscillating
convergence behavior. The energy convergence criterion can therefore
not be applied without also using the displacement convergence criterion.



#### Wind turbine blade bending moment measurements passed to external controller

The blade root (at end 1 of the first element of the foil line) bending moments
about the local x, y, z axes are now available to the external wind turbine controller.



#### Hydrodynamic drag on cross section with 2 symmetry planes

The Morison drag term has been modified to be in accordance with the drag term
used for axis symmetric cross sections. Please confer the user documentation.



#### Implementation of stochastic wave amplitudes

The wave components of a realization of an irregular seastate may now
have stochastic amplitudes.  The new option CHAMP is used to specify
deterministic ('DET') or stochastic ('STOCH') amplitudes.

Note that using stochastic wave amplitudes will cause the significant
wave height to vary between realizations.



#### Wave kinematics at updated position

Wave kinematics may now be calculated at updated dynamic positions
during a time domain simulation by specifying IUPPOS = 2.

Wave kinematics can be calculated during the simulation for ISURF <=4;
i.e. potential fixed at mean water level (ISURF <= 1 and ISURF = 4),
potential stretched / compressed to instantaneous wave surface (ISURF
= 2) and potential moved to instantaneous wave surface (ISURF =
3). Wave kinematics may not be calculated during the simulation for
second order waves (ISURF = 5).

Except for very short simulations, this will be significantly slower
than pre-generating the wave kinematics at the static position. This
is because complete wave kinematics time series may be generated using
FFT, while wave kinematics at individual time steps are calculated as
a sum of all the non-zero wave components.

The option IUPPOS = -2; calculate wave kinematics at the static
positions during the simulation; is added for verification and
comparison.



#### Storage of wave kinematics on additional file

Wave kinematics may now alternatively be stored on an additional file
in ASCII format. Previously, only the binary format was available.

Wave kinematics calculated during a simulation; IUPPOS = 2 or IUPPOS =
-2; are stored on files <prefix>_updkin.asc / <prefix>_updkin.bin.



#### Undo changes to PATH at the end of riflex.bat

When riflex.bat is called with CALL, variables such as PATH will also be
changed in the calling environment. Multiple calls to riflex.bat will
thus increase the length of the PATH variable, which may lead to
the execution stopping if it becomes too long.

Calling riflex.bat with "CMD /C" will ensure that variables in the
calling environment will not be changed. This is therefore
recommended, e.g.:
~~~
CMD /C C:/SINTEF/riflex_simo-4.10.4.BIWR-46-win64/Riflex/bin/riflex.bat i stdin
CMD /C C:/SINTEF/riflex_simo-4.10.4.BIWR-46-win64/Riflex/bin/riflex.bat s stdin
CMD /C C:/SINTEF/riflex_simo-4.10.4.BIWR-46-win64/Riflex/bin/riflex.bat d stdin
~~~
Either backward slashes ( "\" ) or forward slashes ( "/" ) may be used
in the path to the riflex.bat file.

riflex.bat has been modified so that the PATH variable is now set back
to its initial value after running RIFLEX.

Also included in `RIFLEX` 4.10.5.



#### Wind force as separate load group in Stamod

The wind load was earlier activated together with specified forces.
Now the wind load on turbine blades and and the rest of the structure may be activated as a separate load group in Stamod.

Example of input:

~~~
LOAD GROUP DATA
WIND   1
'WindOnTurbineBlades
ON
~~~



#### Improved bending hysteresis model

The numerical performance of the hysteresis bending
model for CRS1 with IEJ=1 and IMF=1 has been improved.
A new procedure for updating the hysteresis
bending moments based on Backward-Euler integration was
implemented, which allows for a fully consistent tangent
stiffness matrix that is expected to improve the
convergence properties of the solution procedure.



#### Displacement storage for duplicated nodes also

A duplicated node occurs when the last node of a line segment
is the first node of the  next segment. This shared node has
one unique global node id but has two local node ids known to
the user: `lineid-segm1-lastnode` and `lineid-segm2-1`.

Previously, only the data for the first of these were written to
the ascii or binary storage file. The other was skipped.
This occured even if both were requested part of the
`DISPLACEMENT RESPONSE STORAGE` card.
Now, both will be written - if requested.



#### New stationary uniform wind with shear

Wind type 14, stationary uniform wind with shear, has been added. A
power or logarithmic shear profile may be specified.

This wind type differs from wind type 10, stationary uniform wind with
shear, values interpolated at grid points, in that the shear profile
is used directly.



#### Extreme wind events in dynamic analysis

An extreme wind event from "IEC 61400-1 Wind turbines – Part 1: Design
requirements – 2005" may be applied in a time domain simualtion. The
wind event can be applied to a stationary uniform wind with shear,
IWITYP = 14, in both `RIFLEX` analyses and in coupled
`RIFLEX` - `SIMO` analyses. The following extreme wind events are
available:
    - IEC 2005 extreme coherent gust with direction change, ECD
    - IEC 2005 extreme vertical wind shear, EWSV
    - IEC 2005 extreme horizontal wind shear, EWSH
    - IEC 2005 extreme operating gust, EOG
    - IEC 2005 extreme direction change, EDC

The EWSV and EWSH events can only be used for systems which include a
`RIFLEX` wind turbine. The ECD, EOG and EDC events may be used for
systems without a wind turbine, but some event parameters must then be
specified; e.g. velocity change, direction change and duration of
event for an ECD event.



#### Wind turbine shutdown with generator fault conditions

Wind turbine shutdown with generator fault conditions may be applied in a
time domain analysis. The shutdown event can be applied to a RIFLEX modelled
wind turbine in both `RIFLEX` analyses and in coupled `RIFLEX` - `SIMO` analyses.
The generator fault options include total loss of
generator torque and  bakup power formulated as following scaled torque
control. In addition a mechanical brake in form of linear torque damping
may be modelled.



#### Wind turbine blade pitch fault conditions

Wind turbine blade pitch fault conditions may be applied in a time domain
analysis. The fault conditions can be applied to a RIFLEX modelled wind
turbine in both `RIFLEX` analyses and in coupled `RIFLEX` - `SIMO`
analyses. The following blade pitch fault types may modelled:
- Seized, i.e. fixed blade pitch from a specific time
- Runaway, i.e. blade pitch change at a specific rate until reach of final pitch angle
- Actuator bias, i.e. constant pitch deviation from required pitch

The blade pitch fault conditions are modelled individually for blades with pitch fault.



#### Pipe-In-pipe contact forces in global system

Pipe-in-pipe contact forces and moments in the global system are now
stored on the file <pref>_cntfor.asc / <pref>_cntfor.bin along with
the forces and moment in the local system. The contact forces are
stored if element forces are stored on an additional ascii or binary
file; i.e. IFORFM /= 0; and pipe-in-pipe elements are present in the
system.



#### Visualization of wind speeds and forces for wind turbine blades

Wind speeds and aerodynamic forces acting on wind turbine blades are made
available for visualization in SIMA and SimVis.



#### Hydrodynamic loads based on potential theory

A test version of hydrodynamic loads based on potential theory (WAMIT) has
been implemented. The functionality is currently under testing.


#### Marine growth

The marine growth is defined by specifying the thickness and density for a range of depths.


Example of input:

~~~
'---------------------------
NEW COMPonent GROWth
'---------------------------
'ID NumbOfLevels
NOR300    5
'---------------------------
' MGLEV  MG   MDENS
'---------------------------
  2.0  0.06  1.325
 40.0  0.06  1.325
-40.1  0.03  1.325
-300.0  0.03  1.325
-700.0  0.03  1.325
'---------------------------
~~~

Marine growth is defined as a new static load group. During the load steps in this load
group, the mass and diameter properties of the elements in this zone will be modified based
on their current location. These properties will be fixed in the rest of the static analysis
and in the dynamic analysis. The user may thus select the static configuration that is most
representative for the conditions for which the marine growth is accumulated.

An overall scaling factor for the accumulated thickness will allow the user more easily to
switch between no marine growth, partly accumulated marine growth and fully developed marine growth.


Example of input:

~~~
'---------------------------
LOAD GROUP DATA
'---------------------------
'nstep maxit raco
4 50 1.1e-5
'lotype NLSPEC
GROWTH    1
'MGFAC
1.0
'--------------
~~~






### RIFLEX 4.12.0 Corrected errors


#### Wind turbine with number of blades different from 3

Riflex failed or gave incorrect results if the number of foil blades was
different from 3.

Corrected in  `RIFLEX` 4.10.4.



#### Hydrodynamic drag on CRS2 and CRS7 cross-sections, lumped formulation

Corrected a long-standing error in hydrodynamic drag loads on CRS2 and
CRS7 cross-sections when the lumped load formulation is chosen;
i.e. LCONS = 0 in STAMOD.

Corrected in RIFLEX 4.10.5.



#### Scaling of the Froude-Krilov term for CRS2 and CRS7 cross-sections, consistent formulation

The input scaling factor for the Froude-Krilov term was not used for
for CRS2 and CRS7 cross-sections if the consistent load formulation was
chosen. Error in applied loads if
- consistent load formulation was chosen; LCONS = 1 in STAMOD; and
- CRS2 or CRS7 cross-sections with SCFK /= 1.0 were used.



#### Corrected the line length used in result presentation

The accumulated line length used in result presentation is now
calculated from the actual stress-free segment lengths given in the
line type definition in INPMOD; i.e. parameter SLGTH0 if it is given,
otherwise SLGTH.

The line length is mainly used for results on the MatrixPlot files.

Previously, the line length was calculated from the updated
stress-free element lengths in STAMOD and DYNMOD and from the final
static nodal coordinates in VIVANA and OUTMOD.

The change in line length will be small for cases without
    - length changes due to temperature or pressure changes
    - element length modification for elements on / leaving a winch
    - large static elongation / compression


#### Elctrical torque in wind turbine

A minor error in the application of the torque from the wind turbine controller
has been corrected. The torque was applied in the flex-joint local element system
and not in the skew system at the flex-joint nodes. The difference between the systems
is small and the correction gives insignificant changes to the results.

Corrected in `RIFLEX` 4.10.2.



#### Airfoil forces

A long-standing error (since version RIFLEX 4.4) has caused incorrect
results or uncontrolled error termination when computing airfoil
forces on cross-sections that were not part of a wind turbine. The
error has been corrected.

Corrected in `RIFLEX` 4.10.2.



#### Reporting of wind at wind turbine hub

For coupled analyses with `SIMO` wind type `IWITYP >= 10`:
- `=10`: Stationary uniform wind with shear
- `=11`: Fluctuating uniform 2-component wind
- `=12`: Fluctuating 3-component wind read from files (IECWind format)
- `=13`: Fluctuating 3-component wind read from files (TurbSim format)

The wind at the updated coordinates of the `RIFLEX` hub supernode is
now reported on the wind turbine result file. Previously, the wind at
the `SIMO` body `WIND_REF` was reported. The reported wind is also
sent into the external control system, but is otherwise not used in
the analyses. The incoming wind on the blades is found using the
updated nodal coordinates along the blades and has not been changed.

No changes for coupled analyses with `SIMO` wind type `IWITYP < 10`;
the wind at the `SIMO` body `WIND_REF` is reported. Note that this
wind is calculated at the wind force coefficient height `ZCOEFF`. This
wind is also used as the incoming wind along the wind turbine blades .

Possible change in response for wind turbines with external control
system and `SIMO` wind type `IWITYP >= 10`.

Corrected in `RIFLEX` 4.10.2.



#### Ball-joint release for systems with flex-joints

Corrected an error that could occur when releasing a ball-joint in a
nonlinear time domain simulation for a system that also contained one
or more flex-joints. The error occurred if
- a single, specified ball-joint was released and the system contained
  a flex-joint with the same reference number as the ball-joint
- all ball-joints were released and the system contained any flex-joints

The error caused `DYNMOD` to terminate with an error message when the
ball-joint connector was released. Error since flex-joints were
introduced in `RIFLEX 3.6.0`.

Corrected in `RIFLEX` 4.10.2.



#### Export of water depth for DeepC animation

The export of hydrodynamic water depth to the .vtf file for animation
in Xtract has been corrected.

Error in RIFLEX 4.10.0 and 4.10.1, corrected in RIFLEX 4.10.2.



#### Strain-dependent cross-sectional axial damping

The input of strain-dependent cross-sectional axial damping has been
corrected. The table is given as `IDMPAXI` pairs of strain and damping
coefficient values. All values are given on a single input line, as
described in the User Manual. The table has previously been
incorrectly read as two values on each input line.

This input may still be given as two values on each input line in
`RIFLEX 4.10.x`. This may be chenged in later versions.

Corrected in `RIFLEX` 4.10.2.



#### Empty pipe-in-pipe contact force file

The contact force file <pref>_cntfor.asc / <pref>_cntfor.bin was empty
if seafloor contact elements were present. The contents were instead
written to the Fortran file 80.

Error since `RIFLEX` 4.10.0. Also corrected in `RIFLEX` 4.10.4.



#### Allow several vessels without motion transfer functions

Several support vessels may now be specified without motion transfer
function, i..e with `IDWFTR = NONE`. Previously, only one vessel in a
system could be specified without motion transfer functions.



#### Avoid error for some cases of visualization with several vessels

Corrected errors that could cause a dynamic simulation to fail during
initialization of visualization. The error occurred if the simulation
included several vessels and either
- no vessel motions were included; CHMOT = NONE; or
- vessel motions read from file; CHMOT = FILE; and several vessels did not have transfer functions.



### RIFLEX 4.12.0 Input changes


#### Wind turbine response storage

Storage of wind turbine responses requires user input specification.



#### MacCamy-Fuchs wave loads

Since the input specification has been expanded to allow for
dimensional drag force coefficients, an input code
for hydrodynamic drag coefficients has to be specified. As a
consequence the input is not back-compatible for MacCamy-Fuchs wave loads.



#### Static wind loads

Static wind loads on RIFLEX elements will now only be applied in
static analysis if WIND is specified as a static load. Previously, the
static wind loads were activated together with specified forces. Add
the load type WIND to the static load group with SFOR, specified
forces, to get the same static loading as before.

See the section Wind force as separate load group in Stamod below for
more deals.



#### Require compatible wind type in coupled analysis with wind loads

The `SIMO` wind types that are not available in standalone `RIFLEX`;
`IWITYP < 10`, are now only allowed in coupled analysis if wind loads
are only applied to `SIMO` bodies and wind turbine blades. If the case
includes non-blade elements with wind force coefficients `IWITYP >=
10` is required.

Previously, the wind time series at the first `SIMO` body with wind
coefficients was used for all non-blade elements with wind
coefficients. The analysis stopped with an error if none of the
`SIMO` bodies had wind coefficients.




### RIFLEX 4.12.0 Known issues


#### Specified loads at nodes with skew boundary conditions

Specified nodal loads at nodes with user-defined skew boundary
conditions are not handled correctly. The loads in the global
directions are applied in the skew system. A warning is written to the
.res file.

Nodes connected to a flex-joint will have degrees of freedom in a skew
system. Specified loads at these nodes are not handled correctly. An
error message will be written to the .res file and the analysis
stopped.




### RIFLEX 4.12.0 Removed functionality


#### Generation of LF-motions from spectra

Generation of low frequency motions from spectra has been removed in
`RIFLEX 4.11.3`. The data groups `LFMOTION SPECTRUM SURGE`, `LFMOTION
SPECTRUM SWAY` and `LFMOTION SPECTRUM YAW` have been removed and the
options `CHLFM = GEN` and `CHLFM = NEW` are no longer allowed in
`IRREGULAR RESPONSE ANALYSIS`.

Time series of low frequency motions may be read from file.



### RIFLEX 4.12.0 Deprecated functionality

No functionality is deprecated in the 4.12.0 version.








## RIFLEX 4.10.0


### RIFLEX 4.10.0 Input changes

Most input files from version 4.8 can be used unchanged. The
exceptions are noted below. Input for new functionality is described
in the User Manual.



#### Bottom tangent option

The bottom tangent option for SB and AR systems, `IBTANG`, has been
changed. `IBTANG = 1` will now specify the 3D bottom formulation.

Note that the outer contact radius, `R_EXTCNT`, of the cross-section
is used in the 3D bottom formulation while it was not used in the flat
bottom formulation.

The 3D seafloor formulation gives contact on all nodes that are below
`Z < ZBOT + R_EXTCNT`; i.e. contact at the outer contact radius. The
original flat bottom formulation gives contact for nodes with `Z <
ZBOT`; i.e. contact at the centreline. Insignificant changes are
expected for cases in which `R_EXTCNT = 0` for the segments in contact
with the seafloor.

Results will change for cases where segments with `R_EXTCNT > 0` had
contact with the flat seafloor formulation. This may be handled in
four alternative ways:
- If the segments do not have other contact, set `R_EXTCNT = 0`
- If `R_EXTCNT` is the same for all segments with seafloor contact,
  lower the seafloor by `R_EXTCNT`.
- Raise the final static coordinates of the nodes with specified
  position on the seafloor by `R_EXTCNT`. The total line length may
  have to be modified to obtain the same configuration and tension.
- Continue using the original flat bottom formulation (see below), but
  note that this will not be available permanently.

The original flat bottom formulation may be chosen by specifying
`IBTANG = -9`. This option has been made available to allow
investigation of differences between the two formulations and will be
removed in a later version.




#### Seafloor friction contribution to torsional load

Previously, the seafloor friction contribution to torsional load was
activated in `STAMOD` by specifying the load type `FRIT`. This is now
specified though the seafloor contact parameter `ILTPR` given in
`INPMOD`. Specifying `FRIT` in `STAMOD` will now result in an error
message.




#### Modified input for Carisima seafloor contact

The Carisima `INPMOD` data group `NEW COMPonent SOIL` has been renamed
`NEW COMPONENT SEAFloorcontact` and will now be used for other
seafloor contact types as well. The first line of input has therefore
been split into two lines and a the parameter `CHSFCT` added to
specify the seafloor contact component type.

Example of old Carisima input:

~~~
NEW  COMP SOIL
' cmpty UFA1,UFA2,IPRSO,IPREL,IPRPO
  10     1 1
~~~

Example of new input:

~~~
NEW  COMP SEAF
' cmpty chsfct
  10     CARI
' UFA1,UFA2,IPRSO,IPREL,IPRPO
  1 1
~~~



### RIFLEX 4.10.0 Corrected errors



#### File storage of element forces for cases with pipe-in-pipe contact

An error has been corrected in the storage of element forces for cases
with pipe-in-pipe contact. The error could lead to specified element
curvatures not being stored as expected.

Storage of element forces is specified in the `DYNMOD` data group
`FORCE RESPONSE STORAGE`. If `IFORFM`, Format code for storage and /
or output of element forces, is not 0, the element forces for the
specified elements are output to the additional file;
<prefix>_elmfor.asc or <prefix>_elmfor.bin. If the model contains
pipe-in-pipe contact elements, the contact forces for all pipe-in-pipe
elements are written to the file <prefix>_cntfor.asc or
<prefix>_cntfor.bin.

No error if forces were not stored on additional Ascii or binary
files; i.e. if the data group `FORCE RESPONSE STORAGE` was not given
or if `IFILFM` = 0. No error if the number of elements for which force
storage was specified was at least 40% of the number of pipe-in-pipe
elements.

Error since `RIFLEX` 3.6.



#### Element-airfoil correspondence outside of wind turbines

An error in the selection of airfoil characteristics for elements
which are not part of a wind turbine blade has been corrected. In previous
versions, the airfoil characteristics for complex lines could be assigned out
of order in some cases.



#### Calculation of zero wind

The calculation of wind velocity could fail if all resulting wind
components at a point and time were exactly zero. Scaling of the
components resulted in a division by zero and an illegal number (NaN)
was returned. This has been corrected.




### RIFLEX 4.10.0 New / improved functionality


#### Visualization of seafloor contact

Contact forces from all non-Carisima seafloor contact may be exported
from `STAMOD` and `DYNMOD` for visualization in `SimVis`.



#### General cross-section

A new cross-section type CRS7 has been implemented which accounts for
eccentric shear center, mass center and area center.

The CRS7 cross-section also employs a new element geometric
stiffness matrix that accounts for the change of internal loads
due to element rigid body rotation. This is expected to improve the Newton
convergence properties and increase the maximum step size for simulations
with large rigid body rotations and low tension.


#### Coupled bending and torsion model

A coupled bending and torsion model has been implemented for CRS0, CRS1,
CRS2 and CRS7. The model employs a second order approximation of both the
cross-section rotation and the longitudinal Green strain, and may
therefore allow for increased element lengths in certain problems.



#### MacCamy-Fuchs loads on `RIFLEX` elements

MacCamy-Fuchs loads (with additional quadratic drag) may be applied
to vertical cross sections, which are assumed to be circular. The input
format for CRS0, CRS1, and CRS2 cross sections
is modified, existing files may be used without modification.



#### 3D Seafloor contact

The 3D seafloor contact formulation has been improved in order to
increase the numerical robustness. The modification will give minor
changes to the results for some cases.



#### Line tension measurements in DP system

A new option has been added that allows the `SIMO` DP system to
receive line tension measurements from `RIFLEX` lines in a coupled
simulation. Previously this has only been possible for `SIMO` catenary
lines. See the the `SIMO` userguide for more details.



#### Option to remove induction calculation for a wind turbine

An advanced aerodynamic option is included in order to remove the
induction calculation on a wind turbine. This option is useful for
a parked or idling wind turbine, where the aerodynamic loading is better
described by quasi-static airfoil loads.




#### Control of Prandtl factor calculation options

An aerodynamic option is included in order to user control of the Prandtl
correction options. This is done by introducing on/off switches for correction
at the blade tip, at the blade root, and a switch for how these correction
factors are modified in yawed inflow.




#### Seafloor contact specification

The data group Seafloor contact specification may be given to specify
which segments in an AR-system have contact with the
seafloor. Different segments can have different spring-friction
contact or have contact modelled using the new riser-soil contact
formulation.

A single-node contact element is generated at each end of each beam or
bar element in the specified segments.



#### 2nd order waves

The 2nd order wave calculations have been made more efficient.
Slight, but not significant, changes in the results are expected.



#### Short-crested sea

The restriction limiting the number of short-crested directions to a
maximum of 17 has been removed. This applies to both standalone
`RIFLEX` analyses and to coupled `RIFLEX` - `SIMO` analyses.



#### Maximum number of line types and components

The maximum number of line types is increased from 200 to 500 and the
maximum number of components from 200 to 500.




### RIFLEX 4.10.0 Removed functionality

No previously available functionality have been removed in version 4.10.0.




### RIFLEX 4.10.0 Deprecated functionality


#### Original flat bottom formulation

The original flat bottom formulation will be removed in a later
version. It may be specified with `IBTANG = -9` in `RIFLEX 4.10.x`.



#### LF-motion response spectrum

Generation of low frequency motions from spectra will be removed in a
later version of `RIFLEX`. This functionality is currently available
by setting `CHLFM = GEN` in `IRREGULAR RESPONSE ANALYSIS` and then
giving the date groups `LFMOTION SPECTRUM`.



#### Kill and choke lines

The simplified modelling of kill and choke lines attached to a
tensioned riser by including them in the riser elements will be
removed in a later version of `RIFLEX`.  This functionality is
currently available through the variable `NAKC` in `ARBITRARY SYSTEM
AR` and then giving the input described in Description of kill and
choke lines.




## RIFLEX 4.8


### RIFLEX 4.8 Input changes

Input files used in version 4.6 can be used unchanged in version 4.8
with the following exceptions:
- Local element axes must now be defined for all fish net elements (CRS6)


Input for new functionality is described in the User Manual.



### RIFLEX 4.8 Corrected errors


#### Aerodynamic pitching moment

The sign of the applied pitching moment on airfoils which are not a part of
a wind turbine was incorrect. This has been corrected.

Corrected in `RIFLEX` 4.8.4.



#### Linux binary files

The record length of the binary files was set to four times the
correct value. The .ffi, .sam, .raf, .bin and .ts files were therefore
four time their necessary size. The .bin and .ts files were not
comparable with their documentation and pre-existing tools for reading
them.

Error since 4.8.0.

Corrected in `RIFLEX` 4.8.3.



#### Flex-joint with free torsional rotation

An error in the dynamic implementation of flex-joint has been corrected.
The error concerned flex-joints where the torsional rotation was free
while the bending degrees of freedom were locked. This type of flex-joint
is typically used in wind turbine modelling.

The error led to incorrect results if the local x-axis of the flex-joint
did not coincide with the global x-axis. The error was negligible if
the deviation from global x-axis was small. For larger deviations,
the solution tended to diverge and the simulation stopped.

Consequences for wind turbine simulations where the flex-joint x-axis was
close to aligned with the global x-axis: Except torsional moment, this
error affects all reaction forces/moments in the first element in the shaft
(between the hub and the flex-joint). Responses in the rest of the system
are only slightly affected.

Corrected in `RIFLEX` 4.8.2.



#### Drag amplification input to STAMOD

The reading of the drag amplification factors from the specified
MatrixPlot file has assumed that there were five lines between the
line
~~~
MATRIX    Drag amplification factor
~~~
and the first line with drag amplification values. This will not
always be the case; the current version of `VIVANA`, for example, has
four lines here.

The decoding now follows the description of the MatrixPlot file format
in the MatrixPlot User Guide.

Corrected in `RIFLEX` 4.8.2.



#### 3D seafloor friction

An error in the 3D seafloor friction forces has been corrected. In the
transformation of relative displacements and velocities from the
global to local seafloor system the transformation matrix for the
first node of an element was used for both nodes of the element. No
error if the seafloor slope was the same at both ends of the
element. The consequences of the error are expected to be
insignificant for most cases.

Corrected in `RIFLEX` 4.8.1.



#### Correct wave kinematics node selection

A possible error in selection of kinematics nodes for lines that cross the
upper or lower limit for wave kinematics has been corrected. The error could
cause incorrect kinematics at nodes with interpolated kinematics near the
limit. Previously, the node with interpolated kinematics nearest a supernode
without kinematics was selected as a kinematics node. This is now only done if
there are no kinematics nodes between this node and the supernode. This
correction may lead to less accurate kinematics.  Please note that the selected
kinematics nodes are printed on the `*_dynmod.res` file, so any change in
behavior can be detected in this way.

Corrected in `RIFLEX` 4.8.0.


#### Error in vessel transfer functions and short-crested waves

A long-standing error could give extrapolation in direction of the vessel
motion transfer functions for short-crested wave components. The error occurred if
the average propagation direction, `WADR1` or `WADR2`, was less than

~~~
180/(IWADR+1) * (IWADR-1)/2
~~~

from the first or last direction that the transfer functions were given for. `IWADR` is
the number of directions used in the spreading function, `IWADR1` or `IWADR2` in data
group `NEW IRREgular SEAState`.

For `IWADR` = 5; the transfer function will be extrapolated if the
average wave direction is within 60 degrees of the first or last
direction the transfer function is given for.

For `IWADR` = 11; the transfer function will be extrapolated if the
average wave direction is within 75 degrees of the first or last
direction the transfer function is given for.

Corrected in `RIFLEX` 4.8.0.



#### Avoid extrapolation of vessel transfer function direction

Previously, the vessel motion transfer functions could be extrapolated
in direction if the first and last transfer function directions did
not cover a full circle; i.e. `HEAD(NDHFTR)` - `HEAD(1)` < 360 for
`ISYMHF` = 0 or `HEAD(1)` not 0 for for `ISYMHF` > 0.

To avoid extrapolation, the first direction will now be repeated for the
direction `HEAD(1) + 360` if the specified directions do not cover a
full circle.

Corrected in `RIFLEX` 4.8.0.


#### Irregular simulation without waves

Irregular simulation without waves may now be run. This previously led
to an error termination at the beginning of the analysis.

Corrected in `RIFLEX` 4.8.0.


#### Irregular simulation with only low frequency motions

Irregular simulation with low frequency motions and no wave frequency motions
may now be run. This previously led to an error termination during generation
of motion time series in `DYNMOD`.

Corrected in `RIFLEX` 4.8.0.


#### Visualization of regular waves for coupled analysis

`SIMA` and `SimVis` have always visualized regular waves with zero degrees
direction, regardless of the wave direction specified. This error has been
corrected. The error has no consequences for other results.

Corrected in `RIFLEX` 4.8.0.


#### Non-linear Buoyancy Correction (NBC) available for coupled analysis

The functionality Nonlinear Buoyancy Correction (NBC) has been made available
for coupled analysis. This was not the case in the RIFLEX version 4.6.

Corrected in `RIFLEX` 4.8.0.


#### Fish net load model, CRS6

The fish net load model requires that the net plane is defined. The plane
is defined by the local element X-axis and a reference vector specified in
the input group: LOCAL ELEMENT AXIS DEFINITION.

If the local reference vector was not given, an uncontrolled program
termination occurred in STAMOD. The program will now check whether a reference
vector is given for all fish net elements. In this case, the program terminates
in a controlled way giving an appropriate error message.

Corrected in `RIFLEX` 4.8.0.


#### Pipe-in-pipe sheltered closed option

Several errors regarding the sheltered closed option for pipe-in-pipe contact
have been corrected. This could cause errors in the calculation of the inner
fluid load effects. Error in version 4.6 only.

Corrected in `RIFLEX` 4.8.0.



#### Time domain VIV

The input value of the seed for the phase angles of the different
frequency components from `VIVANA` has previously not been used. This
has been corrected in `DYNMOD`.

Corrected in `RIFLEX` 4.8.0.



### RIFLEX 4.8 New / improved functionality



#### Second order wave kinematics for short-crested seas

Second order wave kinematics may now be used together with short-crested seas
(irregular waves with directional spreading).



#### Upwind tower shadow modifications

The tower shadow influence for upwind wind turbines is modified such
that the drag coefficient and Bak correction factor may be taken into
account. If these inputs are zero (default), the same tower shadow as
before is used.


#### Downwind wind turbine modelling

Downwind wind turbine modelling is enabled, including correct default blade
orientation and control system actions. A cosine-squared type tower shadow for
downwind wind turbines is implemented.


#### Morison-type aerodynamic drag forces

Morison-type aerodynamic drag forces may be applied to the dry part of CRS0,
CRS1, CRS2, CRS3, and CRS4 elements.


#### IEC turbulent wind for Linux

Wind files generated by WASP Engineering's IEC Turbulence Simulator can
now also be read by RIFLEX built for Linux.



#### New Linux release

The new Linux release of `SIMO`, `RIFLEX` and `VIVANA` is 64-bit and solves several
issues. Unfortunately, this means that 32-bit Linux operating systems are no
longer supported.

- Supports more than the 32-bit imposed limit of 2 GB of RAM
- No need to install 32-bit support libraries separately
- No special considerations are needed for writing output files larger than 2 GB
- The necessary runtime libraries are included in the installation package and
  no special consideration is needed for installation; the package is now
  fully relocatable
- Added man page for the `vrr` runner script

The package has been tested on the following Linux distributions:

- CentOS 7
- Ubuntu 14.04 LTS
- Linux Mint 17




### RIFLEX 4.8 Removed functionality

No previously available functionality have been removed in version 4.8.




### RIFLEX 4.8 Deprecated functionality

No functionality is deprecated in the 4.8 version.





## RIFLEX 4.6


### RIFLEX 4.6 Input changes

Most 4.4 input files may be used unchanged.

`INPMOD` now checks that the specified pipe-in-pipe identifiers are
unique. The maximum length of a pipe-in-pipe ID has been increased from
8 to 16.

Input for new functionality is described in the User Manual.

Alphanumeric identifiers may now be used for main riser lines
(MRL). Old inputs with numbered main riser lines may still be
used.

The alphanumeric identifiers for pipe-in-pipe specifications must mow
be unique. Note that they have a maximum length of eight characters.

Beam cross-sections with linear stiffness must now have positive,
nonzero axial, bending and torsional stiffness. Specifying zero
stiffness will result in an error in `INPMOD`.



### RIFLEX 4.6 Corrected errors


#### Pipe-in-pipe corrections

The friction stiffness along the pipe surface has been corrected. This
is expected to improve convergence in dynamic analysis.

The unit of STIFFR, spring stiffness associated with the static
friction coefficient, was incorrect in both the User Manual and the
echo on the `_inpmod.res` file. The correct unit is `F / L^2`.

Corrected in `RIFLEX` 4.6.2.


#### Main riser line as master in pipe-in-pipe pairs

An error that prevented the master pipe of a pipe-in-pipe pair to be a main
riser line has been corrected. The error resulted in an controlled error
termination before start of time integration when running dynamic analysis.

Corrected in `RIFLEX` 4.6.2.


#### Multiple main riser lines (MRL)

Corrected an error that prevented more than one main riser line being
defined. Error since 4.0.


#### Waves from multiple directions in coupled simulation

Corrected an error in wave loading on RIFLEX elements
from numerically defined (tabulated) spectra with multiple directions
in coupled `SIMO`-`RIFLEX` simulations.


#### Tubular contact

Corrected errors in calculation of tubular contact modelled using
`ELASTIC CONTACT SURFACE` and `NEW COMPONENT TUBULAR CONTACT`.
Changes in results are expected.

No chnage for pipe-in-pipe contact.



### RIFLEX 4.6 New / improved functionality


#### Pipe-in-pipe improvements

In both static and dynamic analysis, the stiffness terms along the
pipe surface have been modified to improve convergence. The applied
forces were not changed, so no significant change is expected in
results with good convergence. Included in `RIFLEX` 4.6.2.


#### Fluid loading on the inner pipe in a pipe in pipe pair

An option has been added to the pipe in pipe specification to allow
the user to specify whether the inner pipe is exposed to the external
environmental loads or is shielded by the outer pipe.

The default is that the inner pipe is exposed to the external
environmental loads; i.e. buoyancy based on the water density given
for the selected environment and wave loading based on the waves and
current. Old input files will therefore give unchanged behaviour.



#### Pipe in pipe contact with reference to main riser line

The pipes in a pipe-in-pipe pair may now be defined by main riser lines (MRL), lines or a combination of MRL and line.



#### Improved interface for external wind turbine controller

Wind velocity at hub height in global coordinates is added to
available measurements for the external wind turbine controller.
Existing external wind turbine controllers can be used unchanged.



#### Improved dynamic stall initialization options

The internal initialization of dynamic stall parameters may fail
for non-typical airfoils. The search methods have been made more
robust, and error messages have been improved. The user is also
given the option to specify the dynamic stall initialization
parameters.



#### Identifiers in modeling

Alphanumeric identifiers may now be used for main riser lines (MRL). Old inputs with numbered main riser lines may still be used.




### RIFLEX 4.6 Removed functionality

No `RIFLEX` 4.4 functionality has been removed in `RIFLEX` 4.6.




### RIFLEX 4.6 Deprecated functionality

The following functionality was also deprecated in `RIFLEX`4.2 and 4.4.



#### Kill and choke lines (INPMOD)

The simplified modelling of kill and choke lines attached to a tensioned riser by including
them in a riser elements will be removed in the next version of RIFLEX. In RIFLEX 4.0 this
functionality is available through the variable NAKC in ARBITRARY SYSTEM AR and
then giving the data in B6.9.



#### LF-motion response spectrum (DYNMOD)

Generation of low frequency motions from spectra will be removed in the next version of RIFLEX.
In RIFLEX 4.0 this functionality is available by setting CHLFM = GEN in IRREGULAR RESPONSE ANALYSIS
and then giving the date groups LFMOTION SPECTRUM.



#### Import of internal flow data from file (DYNMOD)

The restricted functionality to import internal flow data from file will be removed in the next
version of RIFLEX. In RIFLEX 4.4 this functionality is available for some users by setting INDINT=2
in data group E1.4 and then giving the data group IMPORT FLOW DATA.




## RIFLEX 4.4


### RIFLEX 4.4 Input changes

4.2 input files may be used unchanged, except for the case of regular
analysis with multiple vessels and no wave selected, see
[Specified regular motions for multiple vessels]
(@ref release_4_4_0_input_regmot).

Input for new functionality is described in the User Manual.



#### Specified regular motions for multiple vessels

The motion period must now be the same for all vessels.



### RIFLEX 4.4 Corrected errors


#### Specified regular motions for multiple vessels

If no regular wave is specified, regular motions must be given in a
regular analysis. If the system contained multiple vessels, the
motions were incorrect for vessels 2 - `NVES`. This is now corrected.
Note that the motion period must be the same for all vessels.

Corrected in `RIFLEX` 4.4.0.



#### Fatigue damage for stresses outside the S-N curve range (OUTMOD)

The `OUTMOD` data group TIMEDOMAIN FATIGUE DAMAGE has previously
reported zero fatigue damage if the stresses exceeded the stress level
corresponding to failure after a single cycle. This is now handled as
an error. The most probable cause of this occurring is that the units
of the S-N curve and the calculated stresses are not compatible.

Also corrected in RIFLEX 4.4.2.



#### Corrected radius of gyration for CRS0 cross section

The expression for radius of gyration that is used for the moment of inertia around the local X-axis
has been corrected. This concerns cross section type CRS0 and also cross sections created based on a
stress joint specification. Further, the coating contribution to moment of inertia was not previously included.
The radius of gyration has been calculated to be 71% of the correct value without coating. For cross sections
with coating, the difference is larger. For normal riser analysis, the error had minor or
insignificant influence on the results. However, this is system-dependent. The error has been corrected and
the updated expression also accounts for the coating contribution to the moment of inertia.

Corrected in RIFLEX 4.4.1.



#### Corrected an error in the storage of animation for DeepC

Corrected an error in the storage of dynamic analysis animation for DeepC. Error in 4.4.0 only.

Corrected in RIFLEX 4.4.1.



#### Corrected error in specification of detailed wave kinematics

Corrected an error in the specification of explicitly selected nodes
for undisturbed wave kinematics. This may be done by specifying `DIFF`
combined with `IVES = 0` in the `DYNMOD` data group IRREgular WAVE
PROCedure. Error in 4.4.0 only, where an error exit was caused.

Corrected in RIFLEX 4.4.1.



#### Corrected error with multiple support forces in OUTMOD

An error caused `OUTMOD` to fail if the `OUTMOD` data group SUPPf TIME
SERIes was given more than once. The error has been corrected.

Corrected in RIFLEX 4.4.2.




### RIFLEX 4.4 New / improved functionality


#### Improved wind turbine results

Blade pitch results are now presented for simulations
which include an external control system.

Improved in RIFLEX 4.4.1.



#### Friction stiffness for internal friction moment
The factor adjusting initial stiffness for the friction moment
functionality has been added as user input.  See
[Stiffness properties classification](@ref inpmod_c_crs1_stiffness_properties) in INPMOD.



#### Pre-curved line types
The line type definition may now include specification of a curved
stress-free configuration.
See [Transverse displacement specification](@ref inpmod_b_line_transverse) in INPMOD.



#### TurbSim 3D wind files
TurbSim 3D wind files may now be read by RIFLEX. See [Fluctuating 3-component wind field read from TurbSim file](@ref inpmod_d_wind_specification_turbsim).



#### Airfoil forces
Static airfoil forces may now be applied to CRS2 cross sections that are not blades in a
wind turbine.



#### Read wave kinematics from file
A new option to read in and use wave kinematics from file has been added, see  [Additional detailed specification of wave kinematics points (optional)](@ref dynmod_d_irregular_waves_procedure_additional).



#### Improved stability for coupled analysis with the old SIMO DP-system

The SIMO DP system is now called only at every SIMO time increment
(Sampling time interval). Previously, the old SIMO DP system was
called at each time step (Time integration step) while the new DP
system was correctly called at the sampling time interval.

The correction will possibly increase the computational robustness when the old DP-system (marked deprecated) is applied.



#### Improved wind turbine results

Improved selection and presentation of results for wind turbines. The results are now presented for all blades in the non-rotating shaft system.



#### Minor improvements

Blank space is added around some numbers printed on the .res
files. This has been done to increase readability and to facilitate
comparison of numerical results.

Minor improvements in error handling and layout.




### RIFLEX 4.4 Removed functionality

No `RIFLEX` 4.2 functionality has been removed in `RIFLEX` 4.4.




### RIFLEX 4.4 Miscellaneous


#### Run time environment

Windows versions 4.4 and higher are 64 bit executables and therefore
require different Fortran and Java DLLs than earlier version. The necessary
DLLs are included in the download package. The preformance is improved.




## RIFLEX 4.2


### RIFLEX 4.2 Input changes

4.0 input files may be used unchanged.

Input for new functionality is described in the User Manual.




#### Changed default values for irregular analysis (DYNMOD)

The default sampling step of the pre-generated time series, `DTGEN`, is
decreased to 0.5 s. The default length of the pre-generated time series,
`TIMGEN`, is increased to 4.6 hours. The default simulation length for
irregular analysis, `TIME`, is increased to 3.06 hours.




#### Changed default value for subdivision of time step (DYNMOD)

The default value of the `DYNMOD` parameter `IVARST`, Code for automatic
subdivision of time step, is changed from 2 to 0. If a simulation fails
to run, check if it previously used subdivision and if the default value
of `IVARST` was used.




### RIFLEX 4.2 Corrected errors

The following errors have been corrected in RIFLEX 4.2 versions.


#### Pipe-in-Pipe Contact Search Bug
Fixed a long-standing bug in pipe-in-pipe contact search that caused the search to fail
in the vicinity of flex joints and ball joints. Users with pipe in pipe models that
contains flex joints and/or ball joints should consider rerunning the simulations.

Corrected in `RIFLEX` 4.2.1.



#### Coupled analysis

Error in hydrodynamic drag forces on slender elements

If depth dependent current was applied and wind also was specified in the environmental condition, the
computed drag forces on slender elements were in error. This was due to an incorrect z-position being
used to interpolate the shear profile. The error has been present since version 4.2.0.
The consequence is incorrect drag forces on the slender elements. **Analysis done with this combination
by version 4.2.0 should be re-run!** The error has been corrected.

For other SIMO bugfixes, please refer to the SIMO Release Notes.

Corrected in `RIFLEX` 4.2.1.



#### Instability in prescribed displacements when vessel motions are imported from file Coupled analysis

Simulations occasionally failed when vessel motions were imported from
external file. The algorithm for prescribed (vessel) rotation induced
translation for nodes attached to the vessel has been modified to have
improved numerical robustness. No or insignificant changes to results.

Corrected in `RIFLEX` 4.2.0.



#### Exported vessel velocity and accelerations in coupled analyses (DYNMOD)

An error in the exported vessel velocity and accelerations for coupled
analysis with both `SIMO` bodies and `RIFLEX` support vessel was
corrected.  No error found in analysis results. No error for
standalone `RIFLEX` or for coupled analyses with only SIMO bodies,

Corrected in `RIFLEX` 4.2.0.



#### Winch modelling

A long-standing error in the winch formulation has been detected and
corrected. Analysis based on previous versions of RIFLEX should be
re-run.

Corrected in `RIFLEX` 4.2.0.



#### Linear drag coefficients not applied in linearized time domain analysis

Linear drag coefficients have not been applied in
linearized time domain analysis. Linear drag coefficients are seldom
used, so the consequences are assumed to be minimal. The error has
been corrected.

Corrected in `RIFLEX` 4.2.0.



#### Regular wave analysis with prescribed vessel motions

Error for combined regular wave loading with specified harmonic
displacements (`IMOTD` = 2).  The motions after the first wave period
were incorrect if a different period was specified for the motions
than the wave period (and the wave period was mot a multiple of the
motion period). . Error since `RIFLEX` 3.6.7.

No error if motions are calculated from vessel transfer functions (IMOTD = 1).

Corrected in `RIFLEX` 4.2.0.



### RIFLEX 4.2 New functionality


#### Geotechnical model

New modelling features have been added to model transverse contact
between a vertical pipe and the soil. The new `INPMOD` data group `GEO
SPRING SPECIFICATIONS` is used to give the input to the model.




#### Scaling of Froude-Kriloff term in Morison's equation

Extend the generalized Morison's equation by optionally scaling the term
associated with the Froude-Kriloff load. This to enhance the area of
application of Morison's equation, i.e. allow for larger structural
diameter versus wave length. Note that only loads normal to the
principal axis of an element are scaled. Additional, optional input is
added for cross section typed `CRS0`, `CRS1`, `CRS2`, `CRS3` and `CRS4`.




#### 2nd order wave kinematics

2nd order wave kinematics for long-crested waves have been added to
`RIFLEX`. 2nd order wave kinematics are obtained by setting the
`DYNMOD` input parameter `ICOSIM` to `5`.




#### Store wave kinematics on additional file

Generated wave kinematics may now be stored on additional binary file
from `DYNMOD`. Data group `IRREGULAR KINEMATICS STORAGE` to store wave kinematics on an
additional file `<prefix>_wavkin.bin`. The contents are described in
the text file `key_<prefix>_wavkin.txt`.




#### Wind turbine control system and results

The specified control interval for internal wind turbine control system
has been activated. In addition the value of the integrator gain are
kept within saturation limit. The reason for this implementation is to
improve the behaviour of the internal control system.

Wind turbine results may now be stored on additional text file or binary
file `<prefix>_witurb.asc` or `<prefix>_witurb.bin`. The contents are
described in the text file `key_<prefix>_witurb.txt`. There is no
special input for storing the wind turbine results. The results storage
is based on storage specification for element forces, i.e. time interval
for sampling and file format.




#### Detailed kinematic specification

Allow NODSTP = 0 i.e. no kinematics for this line in the detailed kinematic specification.

Available from `RIFLEX` 4.2.1.





### RIFLEX 4.2 Removed functionality

No `RIFLEX` 4.0 functionality has been removed in `RIFLEX` 4.2.




### RIFLEX 4.2 Miscellaneous


#### Java and HLALIB.jar

The included Java folder and the `HLALIB.jar` file have been updated in the Windows
installation `.zip` file.