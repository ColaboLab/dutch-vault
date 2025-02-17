from db import session
from db.models import Noun, NounArticle, Verb, Conjugation
import argparse

def store_new_noun(noun, article):

    existing_noun = session.query(Noun).filter(Noun.word == noun).first()
    if not existing_noun:
        existing_noun = Noun(word=noun)
        session.add(existing_noun)
        session.commit()
    
    new_article = NounArticle(article = article, noun_id = existing_noun.id)
    session.add(new_article)
    session.commit()

def het_of_de(noun):
    existing_noun = session.query(Noun).filter(Noun.word == noun).first()
    if not existing_noun:
        print("We have not registered that noun yet.")
    else:
        results = session.query(NounArticle.article).filter(NounArticle.noun_id == existing_noun.id).all()
        print([result.article for result in results])

def store_new_verb(verb):
    existing_verb = session.query(Verb).filter(Verb.infinitive == verb.lower()).first()
    if not existing_verb:
        existing_verb = Verb(infinitive = verb.lower())
        session.add(existing_verb)
        session.commit()
    else:
        print("Verb already exists, use FUNCTION to consult conjugation")

def main():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help="Available commands")

    add_noun_parser = subparsers.add_parser("add-noun", help="Add a new noun")
    add_noun_parser.add_argument("article", type=str, choices=["de","het"], help="The article ('de' or 'het')")
    add_noun_parser.add_argument("word", type=str, help="The noun word")
    add_noun_parser.set_defaults(func=lambda args: store_new_noun(args.word, args.article))

    add_het_of_de_parser = subparsers.add_parser("het-of-de", help="Retrieves article for noun")
    add_het_of_de_parser.add_argument("noun", type=str, help="The noun word")
    add_het_of_de_parser.set_defaults(func=lambda args: het_of_de(args.noun))

    add_verb_parser = subparsers.add_parser("add-verb", help = "Add a new verb")
    add_verb_parser.add_argument("verb", type=str, help="The verb in infinitive")
    add_verb_parser.set_defaults(func=lambda args: store_new_verb(args.verb))

    args = parser.parse_args()
    args.func(args)
    

if __name__ == "__main__":
    main()