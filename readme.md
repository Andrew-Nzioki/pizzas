# RUNNING FLASK APP

FROM SCRATCH 

`flask db init`
`flask db revision --autogenerate -m'message'`
`flask db upgrade`