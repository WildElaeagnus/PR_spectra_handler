---


---

<h1 id="photoreflection-spectra-handler">Photoreflection spectra handler</h1>
<p>Эта программа предназначена для обработки спектров фотоотражения, в частности для подгонки формы интерференционного сигнала в спектр.<br>
Фильтрация сигнала интерференции в спектре может помочь обнаружить более сложный сигнал который был искажен наложением помех.</p>
<h2 id="установка">Установка</h2>
<ol>
<li>Убедитесь что python3 установлен.</li>
<li>Используйте <code>pip install -r requirements.txt</code> для установки<br>
необходимых библиотек для python.</li>
<li>Настройте поля в фйале <code>auth_info.txt</code></li>
</ol>
<h2 id="как-использовать">Как использовать</h2>
<ol>
<li>Запустите <code>main_plot.py</code></li>
<li>Откройте спектр (файл формата <code>.CSV</code> или  <code>.DPT</code>, пример файла: <code>test_file.DPT</code> первый столбец: k[1/cm], второй столбец: I[r. u.])<pre><code>12991.92168	0.00267
12984.20676	0.00306
12976.49185	0.00313
...			...
</code></pre>
</li>
<li>При помощи слайдеров измените форму красной синусоиды на левом графике так, чтобы она максимально соответствовала спектру<br>
<img src="https://user-images.githubusercontent.com/54314123/132597127-004c90c9-5080-45d7-8e2e-89e17f23e002.png" alt="initial plot"></li>
<li>Полученный резутьлат бует представленн ввиде зеленой линии на правом графике</li>
</ol>
<p><img src="https://user-images.githubusercontent.com/54314123/132597592-83d7ec4f-9680-4052-a4bc-f707a41caa02.png" alt="configured plot"></p>
<h3 id="описание-элементов">Описание элементов</h3>
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
This button returns all sliders to their default         positions witch is marcked red on each slider.</p>
</li>
</ul>
<h2 id="лицензия">Лицензия</h2>
<p>Photoreflection spectra handler бесплатное программное обеспечение с открытым исходным кодом под лицензией <a href="https://github.com/create-go-app/cli/blob/master/LICENSE">Apache 2.0 License</a>.</p>

