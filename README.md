<p>This library will be used for making charts easier for Network Performance Engineers</p>

<p>This package was creating following this tutorial:<br />
https://packaging.python.org/tutorials/packaging-projects/</p>

<p>To update the package on PyPI:</p>
<ol>
    <li>Update version number in setup.cfg</li>
    <li>In terminal, build the new version: "python3 -m build"</li>
    <li>Upload to PyPI: "twine upload dist/*"<br />
        OR just upload to alt private repo manually (see hallred.com/py_repo as example)</li>
    <li>Enter username and password for PyPI. Done!</li>
</ol>


<p>To install the package. Do this from the terminal:<br />
pip install "hallred-chart"
</p>

<p>Or to install it from a NON PyPI repository (like hallred.com/py_repo), do this:<br />
pip install --index-url https://hallred.com/py_repo/ hallred-chart
</p>