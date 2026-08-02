import random
import time
import matplotlib.pyplot as plt


class Plant_Box:


    def __init__(self):
        self.temp = 20
        self.control_power = 0
        self.ambient_temp = 20
        self.heater_temp = 20

        self.plot = True  # default because plotting is useful

        # Internal plotting state
        self._plot_initialized = False
        self._times = []
        self._temps = []
        self._start_time = time.time()


    # Returns the temperature of the plant
    # that you are tasked with controlling
    # Units are in Celsius
    def get_temp(self):
        return self.temp


    # Sets if you want the temperature versus
    # time graph to be plotted for the plant box.
    # Usage of this function is not required,
    # but is suggested as it makes testing
    # much easier.  It is enabled by default
    def plot_temp(self, plot: bool):
        self.plot = plot

        # Close the plot if it was open
        if not plot and self._plot_initialized:
            plt.close(self._fig)
            self._plot_initialized = False
            self._times.clear()
            self._temps.clear()


    # Sets the control signal to the heat pump.
    def set_control_power(self, control_power):
        self.control_power = control_power


    # Updates the temperature of the plant
    # using the current temp, the control temp,
    # and some random noise from the enviroment
    def update_temp(self):

    # Simple first-order heat transfer model
        control_coeff = 0.20   # heater power
        heater_coeff = 0.08    # heater -> plant
        ambient_coeff = 0.02   # plant -> ambient
        heater_loss = 0.05     # heater -> ambient
        noise_std = 0.05       # environmental disturbances

        # Heater has thermal inertia
        heater_delta = (
            control_coeff * self.control_power
            - heater_loss * (self.heater_temp - self.ambient_temp)
        )
        self.heater_temp += heater_delta

        # Plant only responds to heater temperature
        delta = (
            heater_coeff * (self.heater_temp - self.temp)
            + ambient_coeff * (self.ambient_temp - self.temp)
            + random.gauss(0, noise_std)
        )

        # Prevent unrealistic jumps
        delta = max(min(delta, 2.0), -2.0)

        self.temp += delta

        # Update the live plot if enabled
        if self.plot:

            # Create the plot on first use
            if not self._plot_initialized:
                plt.ion()
                self._fig, self._ax = plt.subplots()
                self._line, = self._ax.plot([], [])
                self._ax.set_xlabel("Time (s)")
                self._ax.set_ylabel("Temperature")
                self._ax.set_title("Temperature vs Time")

                self._plot_initialized = True
                self._start_time = time.time()

            self._times.append(time.time() - self._start_time)
            self._temps.append(self.temp)

            self._line.set_data(self._times, self._temps)
            self._ax.relim()
            self._ax.autoscale_view()

            self._fig.canvas.draw_idle()
            self._fig.canvas.flush_events()
            plt.pause(0.001)

        return self.temp