"""
Experiment script title: 	<Test stand testing>
Author: 		<Dia>
E-mail address: 			<primary_experimenter_address>
Date: 						<2019/06/06>
Notes: 						<first time we are running the experiment>
							...
							...
							...
"""

import laboratory_devices as lab
import time

### ------- Experiment protocol: insert script between brackets. ------- ###
if __name__ == "__main__":

    master = lab.locate_master_pump()

    # leave a comment here that describes how syringe a is going to be used.
    syringe_a = lab.Syringe(make="HSW Norm-Ject", volume=1)

    ### ---------------- Associate pumps with syringes ----------------  ###
    pump_0 = lab.Pump(port=master, address=0, syringe=syringe_a)

    # Sample preparation

    lab.check_in("""Add the following components to a tube: 10 ul plasma""")
    lab.check_in(""" Add 65ul beads/lysis mix to the plasma""")
    lab.check_in("""Place the tube on vortex for 10 min""")
    lab.check_in("""Place the tube to the tubing inlet""")
    lab.check_in(
        """Make sure the syringe is already installed in the correct possition""")

    # PHASE 1 - Pull the plasma/beads/lysis buffer mix trough the device
    # channel

    lab.announce(
        """PHASE 1 is coming, when our sample mix is going throug the device channel""")
    pump_0.pull(volume=250, volume_units="ul", rate=250, rate_units="ul/min")

    # PHASE 2 - First wash step

    lab.check_in("""Fill up a 1.5 mls tube with 100 ul Wash Solution""")
    lab.check_in("""Place the tube to the tubing inlet""")

    lab.announce(
        """PHASE 2 is coming, which is the first washing step during the process""")
    pump_0.pull(volume=150, volume_units="ul", rate=250, rate_units="ul/min")

    # PHASE 3 - Second wash step

    lab.check_in("""Fill up a 1.5 mls tube with 100 ul 80 % EtOH""")
    lab.check_in("""Place the tube to the tubing inlet""")

    lab.announce(
        """PHASE 3 is coming, which is the second washing step during the process""")
    pump_0.pull(volume=500, volume_units="ul", rate=150, rate_units="ul/min")

    lab.check_in(
        """Prepare the nex sample: add 10 ul plasma and 65ul beads/lysis mix in a tube""")
    lab.check_in("""Place on vortex for 10 min""")

    # PHASE 4 - Elution step

    lab.check_in("""Fill up a new 1.5 mls tube with 20 ul Elution buffer""")
    lab.check_in("Place the tube to the tubing inlet")

    lab.announce(
        """PHASE 4 is coming, which is the Elution step, the process is almost done""")
    pump_0.pull(volume=45, volume_units="ul", rate=500, rate_units="ul/min")

    lab.check_in("Wait 5 minutes")
    time.sleep(5 * 60)

    pump_0.push(volume=75, volume_units="ul", rate=500, rate_units="ul/min")
    lab.announce(
        """Good job, you are done with the extraction, store the sample""")
