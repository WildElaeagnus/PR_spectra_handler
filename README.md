---


---

<h1 id="photoreflection-spectra-handler">Photoreflection spectra handler</h1>
<p>This program is designed for the processing of photoreflection spectra, specifically for fitting the shape of the interference signal into the<br>
spectrum.<br>
Filtering out the interference signal in the spectrum can help to detect a more complex signal that has been distorted by the interference overlay.</p>
<h2 id="installation">Installation</h2>
<ol>
<li>Make sure python3 is installed.</li>
<li>Use <code>pip install -r requirements.txt</code> to install<br>
required libraries for python.</li>
<li>Configure the fields in the <code>auth_info.txt</code> file</li>
</ol>
<h2 id="how-to-use">How to use</h2>
<ol>
<li>Run <code>main_plot.py</code>.</li>
<li>Open spectrum (file format <code>.CSV</code> or <code>.DPT</code>, example file: <code>test_file.DPT</code> first column: k[1/cm], second column: I[r. u.])<pre><code>12991.92168 0.00267
12984.20676 0.00306
12976.49185 0.00313
...			...
</code></pre>
</li>
<li>Use the sliders to change the shape of the red sine wave in the left graph so that it matches the spectrum as closely as possible<br>
<img src="https://user-images.githubusercontent.com/54314123/132597127-004c90c9-5080-45d7-8e2e-89e17f23e002.png" alt="initial plot"></li>
<li>The result will be shown as a green line on the right graph</li>
</ol>
<p><img src="https://user-images.githubusercontent.com/54314123/132597592-83d7ec4f-9680-4052-a4bc-f707a41caa02.png" alt="configured plot"></p>
<h3 id="description-of-elements">Description of elements</h3>
<ul>
<li>
<p><strong>Cd</strong> left and right sliders:<br>
These sliders represents amount of attenuation by gauss function from right         and left side accordingly.</p>
</li>
<li>
<p><strong>Wd</strong> left and right sliders:<br>
These sliders represents intensity of         attenuation by gauss function from         right and left side accordingly.</p>
</li>
<li>
<p><strong>Amp</strong> slider:<br>
This slider represents amplitude of sine signal.</p>
</li>
<li>
<p><strong>Freq</strong> slider:<br>
This slider represents frequency of sine signal.</p>
</li>
<li>
<p><strong>Phase</strong> slider:<br>
This slider represents phase of sine signal from 0 to 2*Pi in         rads.</p>
</li>
<li>
<p><strong>Offset</strong> slider:<br>
This slider represents offset of sine signal along the x-axis.</p>
</li>
<li>
<p><strong>Reset</strong> button:<br>
This button returns all sliders to their default         positions witch is marked red on each slider.</p>
</li>
</ul>
<h2 id="license">License</h2>
<p>Photoreflection spectra handler is free and open source software under the <a href="https://github.com/create-go-app/cli/blob/master/LICENSE">Apache 2.0 License</a>.</p>

