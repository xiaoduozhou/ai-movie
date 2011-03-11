import logging
from nlg import nlg
from nlu import NLUnderstanding
from dm import DialogManager

logging.basicConfig(level=logging.DEBUG,
                    filename='session.log',
                    format='%(message)s',
                    filemode='a')
nlu = NLUnderstanding()
dialogManager = DialogManager()

#TODO test MORE PREF

try:
    greeting="Hi, there"#nlg.greet()
    logging.info('Bot: '+greeting)
#    print('Bot: '+greeting)
    input = raw_input(greeting+'\n')
    while input is not None:
        # NLU processing
        logging.info('User: '+input)
        nlu_out = nlu.process(input)
        logging.debug('nlu_out: '+str(nlu_out))
        # Dialog manager processing
        dm_out=dialogManager.input(nlu_out)
        logging.debug('dm_out: '+str(dm_out))
        # Dialog manager gives feed back to NLU
        nlu.expect = dialogManager.pending_question
        # Generate response to user
        output=nlg.process(nlu_out,dm_out)
        # Print and log response  
        logging.info('Bot: '+str(output))
#        print('Bot: '+str(output))
        # Decide whether to continue
        for dict in nlu_out:
            if dict.get("command")=="EXIT":
                exit()
        #Get user input
        input = raw_input(output+'\n')
except EOFError:
    exit()