# base64-encoder-decoder

Universiteti i Prishtinës
Fakulteti i Inxhinierisë Kompjuterike dhe Softuerike 

Implementimi i base64 enkoderit dhe dekoderit



Studentët: Dren Morina, Djellza Jasiqi, Dionis Sylejmani, Dituri Kodra
Mbikqyrës: ass. Mërgim Hoti


Mbi projektin:


Enkodimi dhe dekodimi base64 janë metoda reprezentimi për transmetim të sigurtë, që përdoren për konvertimin e të dhënave në një format të sigurtë për transferim mbi rrjete të cilat nuk procesojnë të dhëna binare.
Enkodimi:
Procesi i konvertimit të të dhënave binare sipas një formati 64 karakterësh, duke përfshirë shkronja të mëdha, shkronja të vogla, numra dhe simbole si "+" & "/".
Të dhënat hyrëse ndahen në blloqe 6-bitëshe duke e përshtatur secilin bllok me një nga 64 karakteret e tabelës base64.
Në qoftë se të dhënat hyrëse nuk janë shumëfish 3-bitësh, në fund të të dhënave të enkoduaratë shtojmë padding (mbushje).

Dekodimi:
Proces i kundërt i enkodimit, konverton të dhënat e enkoduara me base64 në formën fillestare binare.
Të dhënat e enkoduara ndahen në grupe katër karakterësh të cilat konvertohen në blloqe binare 6-bitëshe, më tej bashkohen për të krijuar të dhënat fillestare binare. Paddings (mbushjet) luajnë rol kyç për garantimin e rimarrjes së të dhënave origjinale.

