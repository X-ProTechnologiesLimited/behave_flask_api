FROM codenvy/python27
WORKDIR /app

COPY tests/ /app/tests
COPY lib/ /app/lib
COPY requirements.txt /app/
COPY utils /app/utils/
COPY initialise_db.py /app/

ENV CONTAINERISED true

USER root
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN if [ -d "lib/__pycache__/" ] ; then rm -rf lib/__pycache__ ; fi
RUN if [ -d "tests/__pycache__/" ] ; then rm -rf tests/__pycache__ ; fi
RUN if [ -d "tests/test_output" ] ; then rm -f tests/test_output/* ; fi

RUN chown -R user: /app
USER user

ENTRYPOINT ["/bin/bash"]
