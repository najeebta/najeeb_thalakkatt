import pdfkit

__author__ = 'NajeebT'


class ReportGen(object):
    """
    Class to be inherited if report generation is needed
    """
    @staticmethod
    def generate_report(movies):
        """
        This method is for generating raw report
        """
        fname = 'output.txt'
        f = open(fname, 'w')
        s = "MOVIE NAME, RUN TIME, LANGUAGE, LEAD ACTOR, GENRE \n"
        f.write(s)
        lines = "________________________________________________________ \n"
        f.write(lines)
        for movie in movies:
            f.write(movie.name + ", " + movie.run_time + ", " +
                    movie.language + ", " + movie.lead_actor + ", " + movie.genre + "\n")
        f.close()


class MovieGen(ReportGen):
    """
    This Class is for generating reports
    """

    @staticmethod
    def text(movies):
        """
        This method will generate text file
        :param movies:
        :return:
        """
        ReportGen.generate_report(movies)

    @staticmethod
    def pdf(movies):
        """
        This method will use pdfkit to create pdf files
        :param movies:
        :return:
        """
        ReportGen.generate_report(movies)
        pdfkit.from_file('output.txt', 'output.pdf')


def get_report(movie, export_method):
    """
    Method with Reflection
    :return:
    """
    class_name = "MovieGen"
    method = export_method
    obj = globals()[class_name]()
    getattr(obj, method)([movie])
