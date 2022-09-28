# MLFY

*Because RIDL can't flee from death forever*

## Background

* [Raptor wiki](https://wiki.raptorcs.com/wiki/Speculative_Execution_Vulnerabilities_of_2018#Attack_surface_reduction)
* [Kicksecure forum](http://forums.w5j6stm77zs6652pgsij4awcjeel3eco7kvipheu6mtr623eyyehj4yd.onion/t/disabling-smt-in-security-misc-may-make-security-worse-on-some-power9-systems/100)

## To disable CPU's

~~~
lstopo --of xml | ./paired-caches.py | sudo ./disable-cpus.sh
~~~

## To re-enable CPU's

~~~
sudo ./enable-all-cpus.sh
~~~

## Credits

RobbieAB and cyrozap for pointing me in a useful direction.

## Etymology

It's a Harry Potter wand-lore reference.

## License

Copyright 2022 Jeremy Rand.  GPLv3+.
