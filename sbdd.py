# Coded by Cracker
# CRACKER911181
 

import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzCmZyb20gdGhyZWFkaW5nIGltcG9ydCBUaHJlYWQgYXMgcG9vbAppbXBvcnQgYmFzZTY0CmltcG9ydCBvcyx0aW1lCiNUZXh0IGNvbG91cgojY3JlYXRlZCBCeSBDcmFja2VyOTExMTgxCmNvbG91cm9mZj0iXHgxYlswMG0iICNjb2xvdXIgb2ZmCgpyZWQ9Ilx4MWJbOTFtIiAjcmVkCmdyZWVuPSJceDFiWzkybSIgI2dyZWVuCnllbGxvdz0iXHgxYls5M20iICN5ZWxsb3cKYmx1ZT0iXHgxYls5NG0iICNibHVlCnJvc3k9Ilx4MWJbOTVtIiAjcm9zeQpwZXN0PSJceDFiWzk2bSIgI3Blc3QKCgoKZG9tYWluPXN0cihpbnB1dChyb3N5KydcblxuRW50ZXIgVGFyZ2V0IERvbWFpbiAoZWc6ICJnb29nbGUuY29tIik6ICcrcmVkKSkKCm9vPW9wZW4oIi5zdWIudHh0IiwiciIpCm94PW9vLnJlYWQoKQoKY3g9YmFzZTY0LmI2NGRlY29kZShveCkKb3A9Y3guZGVjb2RlKCd1dGYtOCcpCgpzcD1vcC5zcGxpdCgnXG4nKQpwcmludChibHVlKyJcblxuICAgIFsrXVlvdXIgVGFyZ2V0IERvbWFpbidzIFN1YmRvbWFpbiBpczogXG5cbiIrZ3JlZW4pCgpkZWYgc3ViMCgpOgoJc3M9c3BbMDozNDJdCglmb3Igc3ViZG9tYWluIGluIHNzOgoJCQoJCXN1YmQ9c3RyKHN1YmRvbWFpbikKCQkjcHJpbnQoInRlc3Rpbmc6ICIrc3ViZCkKCQl1cmw9c3RyKCJodHRwOi8vIitzdWJkK2RvbWFpbikKCQkKCQl0cnk6CgkJCXJlcXVlc3RzLmdldCh1cmwpCgkJZXhjZXB0IHJlcXVlc3RzLkNvbm5lY3Rpb25FcnJvcjoKCQkJcGFzcwoJCWVsc2U6CgkJCXByaW50KCJcdCIrdXJsKQoKCmRlZiBzdWIxKCk6Cglzcz1zcFszNDI6Njg0XQoJZm9yIHN1YmRvbWFpbiBpbiBzczoKCQkKCQlzdWJkPXN0cihzdWJkb21haW4pCgkJI3ByaW50KCJ0ZXN0aW5nOiAiK3N1YmQpCgkJdXJsPXN0cigiaHR0cDovLyIrc3ViZCtkb21haW4pCgkJCgkJdHJ5OgoJCQlyZXF1ZXN0cy5nZXQodXJsKQoJCWV4Y2VwdCByZXF1ZXN0cy5Db25uZWN0aW9uRXJyb3I6CgkJCXBhc3MKCQllbHNlOgoJCQlwcmludCgiXHQiK3VybCkKCgpkZWYgc3ViMigpOgoJc3M9c3BbNjg0OjEwMjZdCglmb3Igc3ViZG9tYWluIGluIHNzOgoJCQoJCXN1YmQ9c3RyKHN1YmRvbWFpbikKCQkjcHJpbnQoInRlc3Rpbmc6ICIrc3ViZCkKCQl1cmw9c3RyKCJodHRwOi8vIitzdWJkK2RvbWFpbikKCQkKCQl0cnk6CgkJCXJlcXVlc3RzLmdldCh1cmwpCgkJZXhjZXB0IHJlcXVlc3RzLkNvbm5lY3Rpb25FcnJvcjoKCQkJcGFzcwoJCWVsc2U6CgkJCXByaW50KCJcdCIrdXJsKQoKCmRlZiBzdWIzKCk6Cglzcz1zcFsxMDI2OjEzNjhdCglmb3Igc3ViZG9tYWluIGluIHNzOgoJCQoJCXN1YmQ9c3RyKHN1YmRvbWFpbikKCQkjcHJpbnQoInRlc3Rpbmc6ICIrc3ViZCkKCQl1cmw9c3RyKCJodHRwOi8vIitzdWJkK2RvbWFpbikKCQkKCQl0cnk6CgkJCXJlcXVlc3RzLmdldCh1cmwpCgkJZXhjZXB0IHJlcXVlc3RzLkNvbm5lY3Rpb25FcnJvcjoKCQkJcGFzcwoJCWVsc2U6CgkJCXByaW50KCJcdCIrdXJsKQoKCmRlZiBzdWI0KCk6Cglzcz1zcFsxMzY4OjE3MTBdCglmb3Igc3ViZG9tYWluIGluIHNzOgoJCQoJCXN1YmQ9c3RyKHN1YmRvbWFpbikKCQkjcHJpbnQoInRlc3Rpbmc6ICIrc3ViZCkKCQl1cmw9c3RyKCJodHRwOi8vIitzdWJkK2RvbWFpbikKCQkKCQl0cnk6CgkJCXJlcXVlc3RzLmdldCh1cmwpCgkJZXhjZXB0IHJlcXVlc3RzLkNvbm5lY3Rpb25FcnJvcjoKCQkJcGFzcwoJCWVsc2U6CgkJCXByaW50KCJcdCIrdXJsKQoKCmRlZiBzdWI1KCk6Cglzcz1zcFsxNzEwOjIwNTJdCglmb3Igc3ViZG9tYWluIGluIHNzOgoJCQoJCXN1YmQ9c3RyKHN1YmRvbWFpbikKCQkjcHJpbnQoInRlc3Rpbmc6ICIrc3ViZCkKCQl1cmw9c3RyKCJodHRwOi8vIitzdWJkK2RvbWFpbikKC'
love = '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'
god = 'VzdGluZzogIitzdWJkKQoJCXVybD1zdHIoImh0dHA6Ly8iK3N1YmQrZG9tYWluKQoJCQoJCXRyeToKCQkJcmVxdWVzdHMuZ2V0KHVybCkKCQlleGNlcHQgcmVxdWVzdHMuQ29ubmVjdGlvbkVycm9yOgoJCQlwYXNzCgkJZWxzZToKCQkJcHJpbnQoIlx0Iit1cmwpCgoKZGVmIHN1YjE0KCk6Cglzcz1zcFs0Nzg4OjUxMzBdCglmb3Igc3ViZG9tYWluIGluIHNzOgoJCQoJCXN1YmQ9c3RyKHN1YmRvbWFpbikKCQkjcHJpbnQoInRlc3Rpbmc6ICIrc3ViZCkKCQl1cmw9c3RyKCJodHRwOi8vIitzdWJkK2RvbWFpbikKCQkKCQl0cnk6CgkJCXJlcXVlc3RzLmdldCh1cmwpCgkJZXhjZXB0IHJlcXVlc3RzLkNvbm5lY3Rpb25FcnJvcjoKCQkJcGFzcwoJCWVsc2U6CgkJCXByaW50KCJcdCIrdXJsKQoKCmRlZiBzdWIxNSgpOgoJc3M9c3BbNTEzMDo1NDcyXQoJZm9yIHN1YmRvbWFpbiBpbiBzczoKCQkKCQlzdWJkPXN0cihzdWJkb21haW4pCgkJI3ByaW50KCJ0ZXN0aW5nOiAiK3N1YmQpCgkJdXJsPXN0cigiaHR0cDovLyIrc3ViZCtkb21haW4pCgkJCgkJdHJ5OgoJCQlyZXF1ZXN0cy5nZXQodXJsKQoJCWV4Y2VwdCByZXF1ZXN0cy5Db25uZWN0aW9uRXJyb3I6CgkJCXBhc3MKCQllbHNlOgoJCQlwcmludCgiXHQiK3VybCkKCgpkZWYgc3ViMTYoKToKCXNzPXNwWzU0NzI6NTgxNF0KCWZvciBzdWJkb21haW4gaW4gc3M6CgkJCgkJc3ViZD1zdHIoc3ViZG9tYWluKQoJCSNwcmludCgidGVzdGluZzogIitzdWJkKQoJCXVybD1zdHIoImh0dHA6Ly8iK3N1YmQrZG9tYWluKQoJCQoJCXRyeToKCQkJcmVxdWVzdHMuZ2V0KHVybCkKCQlleGNlcHQgcmVxdWVzdHMuQ29ubmVjdGlvbkVycm9yOgoJCQlwYXNzCgkJZWxzZToKCQkJcHJpbnQoIlx0Iit1cmwpCgoKZGVmIHN1YjE3KCk6Cglzcz1zcFs1ODE0OjYxNTZdCglmb3Igc3ViZG9tYWluIGluIHNzOgoJCQoJCXN1YmQ9c3RyKHN1YmRvbWFpbikKCQkjcHJpbnQoInRlc3Rpbmc6ICIrc3ViZCkKCQl1cmw9c3RyKCJodHRwOi8vIitzdWJkK2RvbWFpbikKCQkKCQl0cnk6CgkJCXJlcXVlc3RzLmdldCh1cmwpCgkJZXhjZXB0IHJlcXVlc3RzLkNvbm5lY3Rpb25FcnJvcjoKCQkJcGFzcwoJCWVsc2U6CgkJCXByaW50KCJcdCIrdXJsKQoKCmRlZiBzdWIxOCgpOgoJc3M9c3BbNjE1Njo2NDk4XQoJZm9yIHN1YmRvbWFpbiBpbiBzczoKCQkKCQlzdWJkPXN0cihzdWJkb21haW4pCgkJI3ByaW50KCJ0ZXN0aW5nOiAiK3N1YmQpCgkJdXJsPXN0cigiaHR0cDovLyIrc3ViZCtkb21haW4pCgkJCgkJdHJ5OgoJCQlyZXF1ZXN0cy5nZXQodXJsKQoJCWV4Y2VwdCByZXF1ZXN0cy5Db25uZWN0aW9uRXJyb3I6CgkJCXBhc3MKCQllbHNlOgoJCQlwcmludCgiXHQiK3VybCkKCgpkZWYgc3ViMTkoKToKCXNzPXNwWzY0OTg6Njg0MF0KCWZvciBzdWJkb21haW4gaW4gc3M6CgkJCgkJc3ViZD1zdHIoc3ViZG9tYWluKQoJCSNwcmludCgidGVzdGluZzogIitzdWJkKQoJCXVybD1zdHIoImh0dHA6Ly8iK3N1YmQrZG9tYWluKQoJCQoJCXRyeToKCQkJcmVxdWVzdHMuZ2V0KHVybCkKCQlleGNlcHQgcmVxdWVzdHMuQ29ubmVjdGlvbkVycm9yOgoJCQlwYXNzCgkJZWxzZToKCQkJcHJpbnQoIlx0Iit1cmwpCgoKZGVmIHN1YjIwKCk6Cglzcz1zcFs2ODQwOjcxODJdCglmb3Igc3ViZG9tYWluIGluIHNzOgoJCQoJCXN1YmQ9c3RyKHN1YmRvbWFpbikKCQkjcHJpbnQoInRlc3Rpbmc6ICIrc3ViZCkKCQl1cmw9c3RyKCJodHRwOi8vIitzdWJkK2RvbWFpbikKCQkKCQl0cnk6CgkJCXJlcXVlc3RzLmdldCh1cmwpCgkJZXhjZXB0IHJlcXVlc3RzLkNvbm5lY3Rpb25FcnJvcjoKCQkJcGFzcwoJCWVsc2U6CgkJCXByaW50KCJcdCIrdXJsKQoKCmRlZiBzdWIyMSgpOgoJc3M9c3BbNzE4Mjo3NTI0XQoJZm9yIHN'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))