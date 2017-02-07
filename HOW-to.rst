Recordar activar el viartualenv (Si funciona veremos el entorno virtual)

.. code::
 nercof:~/workspace/KameLabs (master) $ source ./vkame_labs/bin/activate
 (vkame_labs)nercof:~/workspace/KameLabs (master) $
 
Al intentar actualizar github por primera vez:

.. code::
 nercof:~/workspace/KameLabs (master) $ git push -u origin master
 Username for 'https://github.com': gheize@gmail.com
 Password for 'https://gheize@gmail.com@github.com': 
 To https://github.com/nercof/kame-labs.git
  ! [rejected]        master -> master (non-fast-forward)
 error: failed to push some refs to 'https://github.com/nercof/kame-labs.git'
 hint: Updates were rejected because the tip of your current branch is behind
 hint: its remote counterpart. Integrate the remote changes (e.g.
 hint: 'git pull ...') before pushing again.
 hint: See the 'Note about fast-forwards' in 'git push --help' for details.
 nercof:~/workspace/KameLabs (master) $
 
Para realizar el push emplee un --force
.. code::
 (vkame_labs)nercof:~/workspace/KameLabs (master) $ git push --force
