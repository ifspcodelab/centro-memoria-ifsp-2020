--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

-- Started on 2020-09-21 16:45:57

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 2 (class 3079 OID 60367)
-- Name: unaccent; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS unaccent WITH SCHEMA public;


--
-- TOC entry 3190 (class 0 OID 0)
-- Dependencies: 2
-- Name: EXTENSION unaccent; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION unaccent IS 'text search dictionary that removes accents';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 204 (class 1259 OID 59974)
-- Name: acervo_categoriaacervo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.acervo_categoriaacervo (
    id integer NOT NULL,
    nome character varying(100) NOT NULL,
    descricao text NOT NULL,
    imagem character varying(100) NOT NULL,
    categoria_pai_id integer,
    ativo boolean NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL
);


ALTER TABLE public.acervo_categoriaacervo OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 59972)
-- Name: acervo_categoriaacervo_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.acervo_categoriaacervo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.acervo_categoriaacervo_id_seq OWNER TO postgres;

--
-- TOC entry 3191 (class 0 OID 0)
-- Dependencies: 203
-- Name: acervo_categoriaacervo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.acervo_categoriaacervo_id_seq OWNED BY public.acervo_categoriaacervo.id;


--
-- TOC entry 210 (class 1259 OID 60004)
-- Name: acervo_fotoitemacervo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.acervo_fotoitemacervo (
    id integer NOT NULL,
    destaque boolean NOT NULL,
    imagem character varying(100) NOT NULL,
    item_acervo_id integer NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL
);


ALTER TABLE public.acervo_fotoitemacervo OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 60002)
-- Name: acervo_fotoitemacervo_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.acervo_fotoitemacervo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.acervo_fotoitemacervo_id_seq OWNER TO postgres;

--
-- TOC entry 3192 (class 0 OID 0)
-- Dependencies: 209
-- Name: acervo_fotoitemacervo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.acervo_fotoitemacervo_id_seq OWNED BY public.acervo_fotoitemacervo.id;


--
-- TOC entry 206 (class 1259 OID 59985)
-- Name: acervo_itemacervo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.acervo_itemacervo (
    id integer NOT NULL,
    nome character varying(100) NOT NULL,
    descricao text NOT NULL,
    data date,
    fundo character varying(100),
    id_acervo integer,
    ativo boolean NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL
);


ALTER TABLE public.acervo_itemacervo OWNER TO postgres;

--
-- TOC entry 208 (class 1259 OID 59996)
-- Name: acervo_itemacervo_categorias; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.acervo_itemacervo_categorias (
    id integer NOT NULL,
    itemacervo_id integer NOT NULL,
    categoriaacervo_id integer NOT NULL
);


ALTER TABLE public.acervo_itemacervo_categorias OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 59994)
-- Name: acervo_itemacervo_categorias_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.acervo_itemacervo_categorias_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.acervo_itemacervo_categorias_id_seq OWNER TO postgres;

--
-- TOC entry 3193 (class 0 OID 0)
-- Dependencies: 207
-- Name: acervo_itemacervo_categorias_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.acervo_itemacervo_categorias_id_seq OWNED BY public.acervo_itemacervo_categorias.id;


--
-- TOC entry 205 (class 1259 OID 59983)
-- Name: acervo_itemacervo_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.acervo_itemacervo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.acervo_itemacervo_id_seq OWNER TO postgres;

--
-- TOC entry 3194 (class 0 OID 0)
-- Dependencies: 205
-- Name: acervo_itemacervo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.acervo_itemacervo_id_seq OWNED BY public.acervo_itemacervo.id;


--
-- TOC entry 240 (class 1259 OID 60229)
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- TOC entry 239 (class 1259 OID 60227)
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- TOC entry 3195 (class 0 OID 0)
-- Dependencies: 239
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- TOC entry 242 (class 1259 OID 60239)
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- TOC entry 241 (class 1259 OID 60237)
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- TOC entry 3196 (class 0 OID 0)
-- Dependencies: 241
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- TOC entry 238 (class 1259 OID 60221)
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- TOC entry 237 (class 1259 OID 60219)
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- TOC entry 3197 (class 0 OID 0)
-- Dependencies: 237
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- TOC entry 244 (class 1259 OID 60247)
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- TOC entry 246 (class 1259 OID 60257)
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- TOC entry 245 (class 1259 OID 60255)
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO postgres;

--
-- TOC entry 3198 (class 0 OID 0)
-- Dependencies: 245
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- TOC entry 243 (class 1259 OID 60245)
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO postgres;

--
-- TOC entry 3199 (class 0 OID 0)
-- Dependencies: 243
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- TOC entry 248 (class 1259 OID 60265)
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- TOC entry 247 (class 1259 OID 60263)
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- TOC entry 3200 (class 0 OID 0)
-- Dependencies: 247
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- TOC entry 250 (class 1259 OID 60325)
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- TOC entry 249 (class 1259 OID 60323)
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- TOC entry 3201 (class 0 OID 0)
-- Dependencies: 249
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- TOC entry 236 (class 1259 OID 60211)
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- TOC entry 235 (class 1259 OID 60209)
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- TOC entry 3202 (class 0 OID 0)
-- Dependencies: 235
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- TOC entry 234 (class 1259 OID 60200)
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- TOC entry 233 (class 1259 OID 60198)
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- TOC entry 3203 (class 0 OID 0)
-- Dependencies: 233
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- TOC entry 251 (class 1259 OID 60356)
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- TOC entry 257 (class 1259 OID 76780)
-- Name: eventos_evento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eventos_evento (
    id integer NOT NULL,
    nome character varying(100) NOT NULL,
    descricao text NOT NULL,
    destaque boolean NOT NULL,
    ativo boolean NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL,
    texto text NOT NULL
);


ALTER TABLE public.eventos_evento OWNER TO postgres;

--
-- TOC entry 256 (class 1259 OID 76778)
-- Name: eventos_evento_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.eventos_evento_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.eventos_evento_id_seq OWNER TO postgres;

--
-- TOC entry 3204 (class 0 OID 0)
-- Dependencies: 256
-- Name: eventos_evento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.eventos_evento_id_seq OWNED BY public.eventos_evento.id;


--
-- TOC entry 259 (class 1259 OID 76791)
-- Name: eventos_fotoevento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eventos_fotoevento (
    id integer NOT NULL,
    destaque boolean NOT NULL,
    imagem character varying(100) NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL,
    evento_id integer NOT NULL
);


ALTER TABLE public.eventos_fotoevento OWNER TO postgres;

--
-- TOC entry 258 (class 1259 OID 76789)
-- Name: eventos_fotoevento_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.eventos_fotoevento_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.eventos_fotoevento_id_seq OWNER TO postgres;

--
-- TOC entry 3205 (class 0 OID 0)
-- Dependencies: 258
-- Name: eventos_fotoevento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.eventos_fotoevento_id_seq OWNED BY public.eventos_fotoevento.id;


--
-- TOC entry 222 (class 1259 OID 60061)
-- Name: galeria_diretores_fotopersonalidade; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.galeria_diretores_fotopersonalidade (
    id integer NOT NULL,
    destaque boolean NOT NULL,
    imagem character varying(100) NOT NULL,
    personalidade_id integer NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL
);


ALTER TABLE public.galeria_diretores_fotopersonalidade OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 60059)
-- Name: galeria_diretores_fotopersonalidade_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.galeria_diretores_fotopersonalidade_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.galeria_diretores_fotopersonalidade_id_seq OWNER TO postgres;

--
-- TOC entry 3206 (class 0 OID 0)
-- Dependencies: 221
-- Name: galeria_diretores_fotopersonalidade_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.galeria_diretores_fotopersonalidade_id_seq OWNED BY public.galeria_diretores_fotopersonalidade.id;


--
-- TOC entry 216 (class 1259 OID 60031)
-- Name: galeria_diretores_galeria; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.galeria_diretores_galeria (
    id integer NOT NULL,
    nome character varying(100) NOT NULL,
    descricao text NOT NULL,
    imagem character varying(100) NOT NULL,
    ativo boolean NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL
);


ALTER TABLE public.galeria_diretores_galeria OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 60029)
-- Name: galeria_diretores_galeria_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.galeria_diretores_galeria_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.galeria_diretores_galeria_id_seq OWNER TO postgres;

--
-- TOC entry 3207 (class 0 OID 0)
-- Dependencies: 215
-- Name: galeria_diretores_galeria_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.galeria_diretores_galeria_id_seq OWNED BY public.galeria_diretores_galeria.id;


--
-- TOC entry 218 (class 1259 OID 60042)
-- Name: galeria_diretores_personalidade; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.galeria_diretores_personalidade (
    id integer NOT NULL,
    nome character varying(100) NOT NULL,
    funcao character varying(100),
    sobre text NOT NULL,
    inicio_servico date NOT NULL,
    fim_servico date NOT NULL,
    ativo boolean NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL
);


ALTER TABLE public.galeria_diretores_personalidade OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 60053)
-- Name: galeria_diretores_personalidade_galerias; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.galeria_diretores_personalidade_galerias (
    id integer NOT NULL,
    personalidade_id integer NOT NULL,
    galeria_id integer NOT NULL
);


ALTER TABLE public.galeria_diretores_personalidade_galerias OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 60051)
-- Name: galeria_diretores_personalidade_galerias_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.galeria_diretores_personalidade_galerias_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.galeria_diretores_personalidade_galerias_id_seq OWNER TO postgres;

--
-- TOC entry 3208 (class 0 OID 0)
-- Dependencies: 219
-- Name: galeria_diretores_personalidade_galerias_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.galeria_diretores_personalidade_galerias_id_seq OWNED BY public.galeria_diretores_personalidade_galerias.id;


--
-- TOC entry 217 (class 1259 OID 60040)
-- Name: galeria_diretores_personalidade_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.galeria_diretores_personalidade_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.galeria_diretores_personalidade_id_seq OWNER TO postgres;

--
-- TOC entry 3209 (class 0 OID 0)
-- Dependencies: 217
-- Name: galeria_diretores_personalidade_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.galeria_diretores_personalidade_id_seq OWNED BY public.galeria_diretores_personalidade.id;


--
-- TOC entry 263 (class 1259 OID 84941)
-- Name: instituicao_fotoinstituicao; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.instituicao_fotoinstituicao (
    id integer NOT NULL,
    imagem character varying(100) NOT NULL,
    instituicao_id integer NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL
);


ALTER TABLE public.instituicao_fotoinstituicao OWNER TO postgres;

--
-- TOC entry 262 (class 1259 OID 84939)
-- Name: instituicao_fotoinstituicao_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.instituicao_fotoinstituicao_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.instituicao_fotoinstituicao_id_seq OWNER TO postgres;

--
-- TOC entry 3210 (class 0 OID 0)
-- Dependencies: 262
-- Name: instituicao_fotoinstituicao_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.instituicao_fotoinstituicao_id_seq OWNED BY public.instituicao_fotoinstituicao.id;


--
-- TOC entry 261 (class 1259 OID 84930)
-- Name: instituicao_instituicao; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.instituicao_instituicao (
    id integer NOT NULL,
    nome character varying(100) NOT NULL,
    sobre text NOT NULL,
    missao text NOT NULL,
    visao text NOT NULL,
    endereco character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    facebook character varying(255),
    instagram character varying(255),
    email_agendamento character varying(100) NOT NULL,
    email_faleconosco character varying(100) NOT NULL,
    telefone character varying(100) NOT NULL,
    patrono text NOT NULL,
    atividade text NOT NULL,
    policia_acervo text NOT NULL,
    periodos_visita character varying(255) NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL
);


ALTER TABLE public.instituicao_instituicao OWNER TO postgres;

--
-- TOC entry 260 (class 1259 OID 84928)
-- Name: instituicao_instituicao_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.instituicao_instituicao_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.instituicao_instituicao_id_seq OWNER TO postgres;

--
-- TOC entry 3211 (class 0 OID 0)
-- Dependencies: 260
-- Name: instituicao_instituicao_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.instituicao_instituicao_id_seq OWNED BY public.instituicao_instituicao.id;


--
-- TOC entry 265 (class 1259 OID 84949)
-- Name: instituicao_membro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.instituicao_membro (
    id integer NOT NULL,
    nome character varying(100) NOT NULL,
    funcao character varying(100) NOT NULL,
    imagem character varying(100) NOT NULL,
    instituicao_id integer NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL
);


ALTER TABLE public.instituicao_membro OWNER TO postgres;

--
-- TOC entry 264 (class 1259 OID 84947)
-- Name: instituicao_membro_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.instituicao_membro_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.instituicao_membro_id_seq OWNER TO postgres;

--
-- TOC entry 3212 (class 0 OID 0)
-- Dependencies: 264
-- Name: instituicao_membro_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.instituicao_membro_id_seq OWNED BY public.instituicao_membro.id;


--
-- TOC entry 253 (class 1259 OID 76751)
-- Name: linha_tempo_acontecimento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.linha_tempo_acontecimento (
    id integer NOT NULL,
    titulo character varying(255) NOT NULL,
    descricao text NOT NULL,
    data date NOT NULL,
    ativo boolean NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL
);


ALTER TABLE public.linha_tempo_acontecimento OWNER TO postgres;

--
-- TOC entry 252 (class 1259 OID 76749)
-- Name: linha_tempo_acontecimento_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.linha_tempo_acontecimento_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.linha_tempo_acontecimento_id_seq OWNER TO postgres;

--
-- TOC entry 3213 (class 0 OID 0)
-- Dependencies: 252
-- Name: linha_tempo_acontecimento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.linha_tempo_acontecimento_id_seq OWNED BY public.linha_tempo_acontecimento.id;


--
-- TOC entry 212 (class 1259 OID 60012)
-- Name: linha_tempo_evento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.linha_tempo_evento (
    id integer NOT NULL,
    titulo character varying(255) NOT NULL,
    descricao text NOT NULL,
    data date NOT NULL,
    ativo boolean NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL
);


ALTER TABLE public.linha_tempo_evento OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 60010)
-- Name: linha_tempo_evento_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.linha_tempo_evento_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.linha_tempo_evento_id_seq OWNER TO postgres;

--
-- TOC entry 3214 (class 0 OID 0)
-- Dependencies: 211
-- Name: linha_tempo_evento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.linha_tempo_evento_id_seq OWNED BY public.linha_tempo_evento.id;


--
-- TOC entry 255 (class 1259 OID 76762)
-- Name: linha_tempo_fotoacontecimento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.linha_tempo_fotoacontecimento (
    id integer NOT NULL,
    destaque boolean NOT NULL,
    imagem character varying(100) NOT NULL,
    acontecimento_id integer NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL
);


ALTER TABLE public.linha_tempo_fotoacontecimento OWNER TO postgres;

--
-- TOC entry 254 (class 1259 OID 76760)
-- Name: linha_tempo_fotoacontecimento_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.linha_tempo_fotoacontecimento_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.linha_tempo_fotoacontecimento_id_seq OWNER TO postgres;

--
-- TOC entry 3215 (class 0 OID 0)
-- Dependencies: 254
-- Name: linha_tempo_fotoacontecimento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.linha_tempo_fotoacontecimento_id_seq OWNED BY public.linha_tempo_fotoacontecimento.id;


--
-- TOC entry 214 (class 1259 OID 60023)
-- Name: linha_tempo_fotoevento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.linha_tempo_fotoevento (
    id integer NOT NULL,
    destaque boolean NOT NULL,
    imagem character varying(100) NOT NULL,
    evento_id integer NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL
);


ALTER TABLE public.linha_tempo_fotoevento OWNER TO postgres;

--
-- TOC entry 213 (class 1259 OID 60021)
-- Name: linha_tempo_fotoevento_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.linha_tempo_fotoevento_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.linha_tempo_fotoevento_id_seq OWNER TO postgres;

--
-- TOC entry 3216 (class 0 OID 0)
-- Dependencies: 213
-- Name: linha_tempo_fotoevento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.linha_tempo_fotoevento_id_seq OWNED BY public.linha_tempo_fotoevento.id;


--
-- TOC entry 226 (class 1259 OID 60080)
-- Name: noticias_fotonoticia; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.noticias_fotonoticia (
    id integer NOT NULL,
    destaque boolean NOT NULL,
    imagem character varying(100) NOT NULL,
    noticia_id integer NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL
);


ALTER TABLE public.noticias_fotonoticia OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 60078)
-- Name: noticias_fotonoticia_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.noticias_fotonoticia_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.noticias_fotonoticia_id_seq OWNER TO postgres;

--
-- TOC entry 3217 (class 0 OID 0)
-- Dependencies: 225
-- Name: noticias_fotonoticia_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.noticias_fotonoticia_id_seq OWNED BY public.noticias_fotonoticia.id;


--
-- TOC entry 224 (class 1259 OID 60069)
-- Name: noticias_noticia; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.noticias_noticia (
    id integer NOT NULL,
    titulo character varying(100) NOT NULL,
    descricao text NOT NULL,
    corpo text NOT NULL,
    destaque boolean NOT NULL,
    periodo_destaque integer,
    ativo boolean NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL
);


ALTER TABLE public.noticias_noticia OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 60067)
-- Name: noticias_noticia_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.noticias_noticia_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.noticias_noticia_id_seq OWNER TO postgres;

--
-- TOC entry 3218 (class 0 OID 0)
-- Dependencies: 223
-- Name: noticias_noticia_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.noticias_noticia_id_seq OWNED BY public.noticias_noticia.id;


--
-- TOC entry 230 (class 1259 OID 60099)
-- Name: pesquisas_fotogrupopesquisa; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pesquisas_fotogrupopesquisa (
    id integer NOT NULL,
    destaque boolean NOT NULL,
    imagem character varying(100) NOT NULL,
    grupo_pesquisa_id integer NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL
);


ALTER TABLE public.pesquisas_fotogrupopesquisa OWNER TO postgres;

--
-- TOC entry 229 (class 1259 OID 60097)
-- Name: pesquisas_fotogrupopesquisa_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pesquisas_fotogrupopesquisa_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pesquisas_fotogrupopesquisa_id_seq OWNER TO postgres;

--
-- TOC entry 3219 (class 0 OID 0)
-- Dependencies: 229
-- Name: pesquisas_fotogrupopesquisa_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pesquisas_fotogrupopesquisa_id_seq OWNED BY public.pesquisas_fotogrupopesquisa.id;


--
-- TOC entry 228 (class 1259 OID 60088)
-- Name: pesquisas_grupopesquisa; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pesquisas_grupopesquisa (
    id integer NOT NULL,
    nome character varying(100) NOT NULL,
    descricao character varying(255) NOT NULL,
    texto_livre text NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL
);


ALTER TABLE public.pesquisas_grupopesquisa OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 60086)
-- Name: pesquisas_grupopesquisa_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pesquisas_grupopesquisa_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pesquisas_grupopesquisa_id_seq OWNER TO postgres;

--
-- TOC entry 3220 (class 0 OID 0)
-- Dependencies: 227
-- Name: pesquisas_grupopesquisa_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pesquisas_grupopesquisa_id_seq OWNED BY public.pesquisas_grupopesquisa.id;


--
-- TOC entry 232 (class 1259 OID 60107)
-- Name: pesquisas_membro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pesquisas_membro (
    id integer NOT NULL,
    nome character varying(100) NOT NULL,
    funcao character varying(100),
    descricao character varying(255),
    imagem character varying(100),
    grupo_pesquisa_id integer NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL
);


ALTER TABLE public.pesquisas_membro OWNER TO postgres;

--
-- TOC entry 231 (class 1259 OID 60105)
-- Name: pesquisas_membro_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pesquisas_membro_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pesquisas_membro_id_seq OWNER TO postgres;

--
-- TOC entry 3221 (class 0 OID 0)
-- Dependencies: 231
-- Name: pesquisas_membro_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pesquisas_membro_id_seq OWNED BY public.pesquisas_membro.id;


--
-- TOC entry 2893 (class 2604 OID 59977)
-- Name: acervo_categoriaacervo id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.acervo_categoriaacervo ALTER COLUMN id SET DEFAULT nextval('public.acervo_categoriaacervo_id_seq'::regclass);


--
-- TOC entry 2896 (class 2604 OID 60007)
-- Name: acervo_fotoitemacervo id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.acervo_fotoitemacervo ALTER COLUMN id SET DEFAULT nextval('public.acervo_fotoitemacervo_id_seq'::regclass);


--
-- TOC entry 2894 (class 2604 OID 59988)
-- Name: acervo_itemacervo id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.acervo_itemacervo ALTER COLUMN id SET DEFAULT nextval('public.acervo_itemacervo_id_seq'::regclass);


--
-- TOC entry 2895 (class 2604 OID 59999)
-- Name: acervo_itemacervo_categorias id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.acervo_itemacervo_categorias ALTER COLUMN id SET DEFAULT nextval('public.acervo_itemacervo_categorias_id_seq'::regclass);


--
-- TOC entry 2911 (class 2604 OID 60232)
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- TOC entry 2912 (class 2604 OID 60242)
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- TOC entry 2910 (class 2604 OID 60224)
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- TOC entry 2913 (class 2604 OID 60250)
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- TOC entry 2914 (class 2604 OID 60260)
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- TOC entry 2915 (class 2604 OID 60268)
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- TOC entry 2916 (class 2604 OID 60328)
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- TOC entry 2909 (class 2604 OID 60214)
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- TOC entry 2908 (class 2604 OID 60203)
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- TOC entry 2920 (class 2604 OID 76783)
-- Name: eventos_evento id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eventos_evento ALTER COLUMN id SET DEFAULT nextval('public.eventos_evento_id_seq'::regclass);


--
-- TOC entry 2921 (class 2604 OID 76794)
-- Name: eventos_fotoevento id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eventos_fotoevento ALTER COLUMN id SET DEFAULT nextval('public.eventos_fotoevento_id_seq'::regclass);


--
-- TOC entry 2902 (class 2604 OID 60064)
-- Name: galeria_diretores_fotopersonalidade id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.galeria_diretores_fotopersonalidade ALTER COLUMN id SET DEFAULT nextval('public.galeria_diretores_fotopersonalidade_id_seq'::regclass);


--
-- TOC entry 2899 (class 2604 OID 60034)
-- Name: galeria_diretores_galeria id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.galeria_diretores_galeria ALTER COLUMN id SET DEFAULT nextval('public.galeria_diretores_galeria_id_seq'::regclass);


--
-- TOC entry 2900 (class 2604 OID 60045)
-- Name: galeria_diretores_personalidade id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.galeria_diretores_personalidade ALTER COLUMN id SET DEFAULT nextval('public.galeria_diretores_personalidade_id_seq'::regclass);


--
-- TOC entry 2901 (class 2604 OID 60056)
-- Name: galeria_diretores_personalidade_galerias id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.galeria_diretores_personalidade_galerias ALTER COLUMN id SET DEFAULT nextval('public.galeria_diretores_personalidade_galerias_id_seq'::regclass);


--
-- TOC entry 2923 (class 2604 OID 84944)
-- Name: instituicao_fotoinstituicao id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.instituicao_fotoinstituicao ALTER COLUMN id SET DEFAULT nextval('public.instituicao_fotoinstituicao_id_seq'::regclass);


--
-- TOC entry 2922 (class 2604 OID 84933)
-- Name: instituicao_instituicao id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.instituicao_instituicao ALTER COLUMN id SET DEFAULT nextval('public.instituicao_instituicao_id_seq'::regclass);


--
-- TOC entry 2924 (class 2604 OID 84952)
-- Name: instituicao_membro id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.instituicao_membro ALTER COLUMN id SET DEFAULT nextval('public.instituicao_membro_id_seq'::regclass);


--
-- TOC entry 2918 (class 2604 OID 76754)
-- Name: linha_tempo_acontecimento id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.linha_tempo_acontecimento ALTER COLUMN id SET DEFAULT nextval('public.linha_tempo_acontecimento_id_seq'::regclass);


--
-- TOC entry 2897 (class 2604 OID 60015)
-- Name: linha_tempo_evento id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.linha_tempo_evento ALTER COLUMN id SET DEFAULT nextval('public.linha_tempo_evento_id_seq'::regclass);


--
-- TOC entry 2919 (class 2604 OID 76765)
-- Name: linha_tempo_fotoacontecimento id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.linha_tempo_fotoacontecimento ALTER COLUMN id SET DEFAULT nextval('public.linha_tempo_fotoacontecimento_id_seq'::regclass);


--
-- TOC entry 2898 (class 2604 OID 60026)
-- Name: linha_tempo_fotoevento id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.linha_tempo_fotoevento ALTER COLUMN id SET DEFAULT nextval('public.linha_tempo_fotoevento_id_seq'::regclass);


--
-- TOC entry 2904 (class 2604 OID 60083)
-- Name: noticias_fotonoticia id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.noticias_fotonoticia ALTER COLUMN id SET DEFAULT nextval('public.noticias_fotonoticia_id_seq'::regclass);


--
-- TOC entry 2903 (class 2604 OID 60072)
-- Name: noticias_noticia id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.noticias_noticia ALTER COLUMN id SET DEFAULT nextval('public.noticias_noticia_id_seq'::regclass);


--
-- TOC entry 2906 (class 2604 OID 60102)
-- Name: pesquisas_fotogrupopesquisa id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pesquisas_fotogrupopesquisa ALTER COLUMN id SET DEFAULT nextval('public.pesquisas_fotogrupopesquisa_id_seq'::regclass);


--
-- TOC entry 2905 (class 2604 OID 60091)
-- Name: pesquisas_grupopesquisa id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pesquisas_grupopesquisa ALTER COLUMN id SET DEFAULT nextval('public.pesquisas_grupopesquisa_id_seq'::regclass);


--
-- TOC entry 2907 (class 2604 OID 60110)
-- Name: pesquisas_membro id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pesquisas_membro ALTER COLUMN id SET DEFAULT nextval('public.pesquisas_membro_id_seq'::regclass);


--
-- TOC entry 2927 (class 2606 OID 59982)
-- Name: acervo_categoriaacervo acervo_categoriaacervo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.acervo_categoriaacervo
    ADD CONSTRAINT acervo_categoriaacervo_pkey PRIMARY KEY (id);


--
-- TOC entry 2938 (class 2606 OID 60009)
-- Name: acervo_fotoitemacervo acervo_fotoitemacervo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.acervo_fotoitemacervo
    ADD CONSTRAINT acervo_fotoitemacervo_pkey PRIMARY KEY (id);


--
-- TOC entry 2931 (class 2606 OID 60135)
-- Name: acervo_itemacervo_categorias acervo_itemacervo_catego_itemacervo_id_categoriaa_7ed4b74b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.acervo_itemacervo_categorias
    ADD CONSTRAINT acervo_itemacervo_catego_itemacervo_id_categoriaa_7ed4b74b_uniq UNIQUE (itemacervo_id, categoriaacervo_id);


--
-- TOC entry 2935 (class 2606 OID 60001)
-- Name: acervo_itemacervo_categorias acervo_itemacervo_categorias_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.acervo_itemacervo_categorias
    ADD CONSTRAINT acervo_itemacervo_categorias_pkey PRIMARY KEY (id);


--
-- TOC entry 2929 (class 2606 OID 59993)
-- Name: acervo_itemacervo acervo_itemacervo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.acervo_itemacervo
    ADD CONSTRAINT acervo_itemacervo_pkey PRIMARY KEY (id);


--
-- TOC entry 2983 (class 2606 OID 60354)
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- TOC entry 2988 (class 2606 OID 60281)
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- TOC entry 2991 (class 2606 OID 60244)
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 2985 (class 2606 OID 60234)
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- TOC entry 2978 (class 2606 OID 60272)
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- TOC entry 2980 (class 2606 OID 60226)
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- TOC entry 2999 (class 2606 OID 60262)
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- TOC entry 3002 (class 2606 OID 60296)
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- TOC entry 2993 (class 2606 OID 60252)
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- TOC entry 3005 (class 2606 OID 60270)
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 3008 (class 2606 OID 60310)
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- TOC entry 2996 (class 2606 OID 60348)
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- TOC entry 3011 (class 2606 OID 60334)
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- TOC entry 2973 (class 2606 OID 60218)
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- TOC entry 2975 (class 2606 OID 60216)
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- TOC entry 2971 (class 2606 OID 60208)
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- TOC entry 3015 (class 2606 OID 60363)
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- TOC entry 3023 (class 2606 OID 76788)
-- Name: eventos_evento eventos_evento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eventos_evento
    ADD CONSTRAINT eventos_evento_pkey PRIMARY KEY (id);


--
-- TOC entry 3026 (class 2606 OID 76796)
-- Name: eventos_fotoevento eventos_fotoevento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eventos_fotoevento
    ADD CONSTRAINT eventos_fotoevento_pkey PRIMARY KEY (id);


--
-- TOC entry 2956 (class 2606 OID 60066)
-- Name: galeria_diretores_fotopersonalidade galeria_diretores_fotopersonalidade_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.galeria_diretores_fotopersonalidade
    ADD CONSTRAINT galeria_diretores_fotopersonalidade_pkey PRIMARY KEY (id);


--
-- TOC entry 2945 (class 2606 OID 60039)
-- Name: galeria_diretores_galeria galeria_diretores_galeria_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.galeria_diretores_galeria
    ADD CONSTRAINT galeria_diretores_galeria_pkey PRIMARY KEY (id);


--
-- TOC entry 2949 (class 2606 OID 60161)
-- Name: galeria_diretores_personalidade_galerias galeria_diretores_person_personalidade_id_galeria_b62e12d0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.galeria_diretores_personalidade_galerias
    ADD CONSTRAINT galeria_diretores_person_personalidade_id_galeria_b62e12d0_uniq UNIQUE (personalidade_id, galeria_id);


--
-- TOC entry 2953 (class 2606 OID 60058)
-- Name: galeria_diretores_personalidade_galerias galeria_diretores_personalidade_galerias_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.galeria_diretores_personalidade_galerias
    ADD CONSTRAINT galeria_diretores_personalidade_galerias_pkey PRIMARY KEY (id);


--
-- TOC entry 2947 (class 2606 OID 60050)
-- Name: galeria_diretores_personalidade galeria_diretores_personalidade_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.galeria_diretores_personalidade
    ADD CONSTRAINT galeria_diretores_personalidade_pkey PRIMARY KEY (id);


--
-- TOC entry 3031 (class 2606 OID 84946)
-- Name: instituicao_fotoinstituicao instituicao_fotoinstituicao_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.instituicao_fotoinstituicao
    ADD CONSTRAINT instituicao_fotoinstituicao_pkey PRIMARY KEY (id);


--
-- TOC entry 3028 (class 2606 OID 84938)
-- Name: instituicao_instituicao instituicao_instituicao_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.instituicao_instituicao
    ADD CONSTRAINT instituicao_instituicao_pkey PRIMARY KEY (id);


--
-- TOC entry 3034 (class 2606 OID 84954)
-- Name: instituicao_membro instituicao_membro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.instituicao_membro
    ADD CONSTRAINT instituicao_membro_pkey PRIMARY KEY (id);


--
-- TOC entry 3018 (class 2606 OID 76759)
-- Name: linha_tempo_acontecimento linha_tempo_acontecimento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.linha_tempo_acontecimento
    ADD CONSTRAINT linha_tempo_acontecimento_pkey PRIMARY KEY (id);


--
-- TOC entry 2940 (class 2606 OID 60020)
-- Name: linha_tempo_evento linha_tempo_evento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.linha_tempo_evento
    ADD CONSTRAINT linha_tempo_evento_pkey PRIMARY KEY (id);


--
-- TOC entry 3021 (class 2606 OID 76767)
-- Name: linha_tempo_fotoacontecimento linha_tempo_fotoacontecimento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.linha_tempo_fotoacontecimento
    ADD CONSTRAINT linha_tempo_fotoacontecimento_pkey PRIMARY KEY (id);


--
-- TOC entry 2943 (class 2606 OID 60028)
-- Name: linha_tempo_fotoevento linha_tempo_fotoevento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.linha_tempo_fotoevento
    ADD CONSTRAINT linha_tempo_fotoevento_pkey PRIMARY KEY (id);


--
-- TOC entry 2961 (class 2606 OID 60085)
-- Name: noticias_fotonoticia noticias_fotonoticia_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.noticias_fotonoticia
    ADD CONSTRAINT noticias_fotonoticia_pkey PRIMARY KEY (id);


--
-- TOC entry 2958 (class 2606 OID 60077)
-- Name: noticias_noticia noticias_noticia_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.noticias_noticia
    ADD CONSTRAINT noticias_noticia_pkey PRIMARY KEY (id);


--
-- TOC entry 2966 (class 2606 OID 60104)
-- Name: pesquisas_fotogrupopesquisa pesquisas_fotogrupopesquisa_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pesquisas_fotogrupopesquisa
    ADD CONSTRAINT pesquisas_fotogrupopesquisa_pkey PRIMARY KEY (id);


--
-- TOC entry 2963 (class 2606 OID 60096)
-- Name: pesquisas_grupopesquisa pesquisas_grupopesquisa_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pesquisas_grupopesquisa
    ADD CONSTRAINT pesquisas_grupopesquisa_pkey PRIMARY KEY (id);


--
-- TOC entry 2969 (class 2606 OID 60115)
-- Name: pesquisas_membro pesquisas_membro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pesquisas_membro
    ADD CONSTRAINT pesquisas_membro_pkey PRIMARY KEY (id);


--
-- TOC entry 2925 (class 1259 OID 60133)
-- Name: acervo_categoriaacervo_categoria_pai_id_d00053c9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX acervo_categoriaacervo_categoria_pai_id_d00053c9 ON public.acervo_categoriaacervo USING btree (categoria_pai_id);


--
-- TOC entry 2936 (class 1259 OID 60153)
-- Name: acervo_fotoitemacervo_item_acervo_id_2efbe40c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX acervo_fotoitemacervo_item_acervo_id_2efbe40c ON public.acervo_fotoitemacervo USING btree (item_acervo_id);


--
-- TOC entry 2932 (class 1259 OID 60147)
-- Name: acervo_itemacervo_categorias_categoriaacervo_id_abc8fabd; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX acervo_itemacervo_categorias_categoriaacervo_id_abc8fabd ON public.acervo_itemacervo_categorias USING btree (categoriaacervo_id);


--
-- TOC entry 2933 (class 1259 OID 60146)
-- Name: acervo_itemacervo_categorias_itemacervo_id_c5effdaa; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX acervo_itemacervo_categorias_itemacervo_id_c5effdaa ON public.acervo_itemacervo_categorias USING btree (itemacervo_id);


--
-- TOC entry 2981 (class 1259 OID 60355)
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- TOC entry 2986 (class 1259 OID 60292)
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- TOC entry 2989 (class 1259 OID 60293)
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- TOC entry 2976 (class 1259 OID 60278)
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- TOC entry 2997 (class 1259 OID 60308)
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- TOC entry 3000 (class 1259 OID 60307)
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- TOC entry 3003 (class 1259 OID 60322)
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- TOC entry 3006 (class 1259 OID 60321)
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- TOC entry 2994 (class 1259 OID 60349)
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- TOC entry 3009 (class 1259 OID 60345)
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- TOC entry 3012 (class 1259 OID 60346)
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- TOC entry 3013 (class 1259 OID 60365)
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- TOC entry 3016 (class 1259 OID 60364)
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- TOC entry 3024 (class 1259 OID 76802)
-- Name: eventos_fotoevento_evento_id_c411b814; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX eventos_fotoevento_evento_id_c411b814 ON public.eventos_fotoevento USING btree (evento_id);


--
-- TOC entry 2954 (class 1259 OID 60179)
-- Name: galeria_diretores_fotopersonalidade_personalidade_id_14c4838e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX galeria_diretores_fotopersonalidade_personalidade_id_14c4838e ON public.galeria_diretores_fotopersonalidade USING btree (personalidade_id);


--
-- TOC entry 2950 (class 1259 OID 60172)
-- Name: galeria_diretores_personal_personalidade_id_30de8388; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX galeria_diretores_personal_personalidade_id_30de8388 ON public.galeria_diretores_personalidade_galerias USING btree (personalidade_id);


--
-- TOC entry 2951 (class 1259 OID 60173)
-- Name: galeria_diretores_personalidade_galerias_galeria_id_fce4b2e8; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX galeria_diretores_personalidade_galerias_galeria_id_fce4b2e8 ON public.galeria_diretores_personalidade_galerias USING btree (galeria_id);


--
-- TOC entry 3029 (class 1259 OID 84960)
-- Name: instituicao_fotoinstituicao_instituicao_id_f9ba77d0; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX instituicao_fotoinstituicao_instituicao_id_f9ba77d0 ON public.instituicao_fotoinstituicao USING btree (instituicao_id);


--
-- TOC entry 3032 (class 1259 OID 84966)
-- Name: instituicao_membro_instituicao_id_39229cec; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX instituicao_membro_instituicao_id_39229cec ON public.instituicao_membro USING btree (instituicao_id);


--
-- TOC entry 3019 (class 1259 OID 76773)
-- Name: linha_tempo_fotoacontecimento_acontecimento_id_27cfb46f; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX linha_tempo_fotoacontecimento_acontecimento_id_27cfb46f ON public.linha_tempo_fotoacontecimento USING btree (acontecimento_id);


--
-- TOC entry 2941 (class 1259 OID 60159)
-- Name: linha_tempo_fotoevento_evento_id_7f50e698; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX linha_tempo_fotoevento_evento_id_7f50e698 ON public.linha_tempo_fotoevento USING btree (evento_id);


--
-- TOC entry 2959 (class 1259 OID 60185)
-- Name: noticias_fotonoticia_noticia_id_ece26d4e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX noticias_fotonoticia_noticia_id_ece26d4e ON public.noticias_fotonoticia USING btree (noticia_id);


--
-- TOC entry 2964 (class 1259 OID 60191)
-- Name: pesquisas_fotogrupopesquisa_grupo_pesquisa_id_efcbfb30; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX pesquisas_fotogrupopesquisa_grupo_pesquisa_id_efcbfb30 ON public.pesquisas_fotogrupopesquisa USING btree (grupo_pesquisa_id);


--
-- TOC entry 2967 (class 1259 OID 60197)
-- Name: pesquisas_membro_grupo_pesquisa_id_bbc94ddc; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX pesquisas_membro_grupo_pesquisa_id_bbc94ddc ON public.pesquisas_membro USING btree (grupo_pesquisa_id);


--
-- TOC entry 3035 (class 2606 OID 60128)
-- Name: acervo_categoriaacervo acervo_categoriaacer_categoria_pai_id_d00053c9_fk_acervo_ca; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.acervo_categoriaacervo
    ADD CONSTRAINT acervo_categoriaacer_categoria_pai_id_d00053c9_fk_acervo_ca FOREIGN KEY (categoria_pai_id) REFERENCES public.acervo_categoriaacervo(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3038 (class 2606 OID 60148)
-- Name: acervo_fotoitemacervo acervo_fotoitemacerv_item_acervo_id_2efbe40c_fk_acervo_it; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.acervo_fotoitemacervo
    ADD CONSTRAINT acervo_fotoitemacerv_item_acervo_id_2efbe40c_fk_acervo_it FOREIGN KEY (item_acervo_id) REFERENCES public.acervo_itemacervo(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3037 (class 2606 OID 60141)
-- Name: acervo_itemacervo_categorias acervo_itemacervo_ca_categoriaacervo_id_abc8fabd_fk_acervo_ca; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.acervo_itemacervo_categorias
    ADD CONSTRAINT acervo_itemacervo_ca_categoriaacervo_id_abc8fabd_fk_acervo_ca FOREIGN KEY (categoriaacervo_id) REFERENCES public.acervo_categoriaacervo(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3036 (class 2606 OID 60136)
-- Name: acervo_itemacervo_categorias acervo_itemacervo_ca_itemacervo_id_c5effdaa_fk_acervo_it; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.acervo_itemacervo_categorias
    ADD CONSTRAINT acervo_itemacervo_ca_itemacervo_id_c5effdaa_fk_acervo_it FOREIGN KEY (itemacervo_id) REFERENCES public.acervo_itemacervo(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3048 (class 2606 OID 60287)
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3047 (class 2606 OID 60282)
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3046 (class 2606 OID 60273)
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3050 (class 2606 OID 60302)
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3049 (class 2606 OID 60297)
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3052 (class 2606 OID 60316)
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3051 (class 2606 OID 60311)
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3053 (class 2606 OID 60335)
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3054 (class 2606 OID 60340)
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3056 (class 2606 OID 76797)
-- Name: eventos_fotoevento eventos_fotoevento_evento_id_c411b814_fk_eventos_evento_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eventos_fotoevento
    ADD CONSTRAINT eventos_fotoevento_evento_id_c411b814_fk_eventos_evento_id FOREIGN KEY (evento_id) REFERENCES public.eventos_evento(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3042 (class 2606 OID 60174)
-- Name: galeria_diretores_fotopersonalidade galeria_diretores_fo_personalidade_id_14c4838e_fk_galeria_d; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.galeria_diretores_fotopersonalidade
    ADD CONSTRAINT galeria_diretores_fo_personalidade_id_14c4838e_fk_galeria_d FOREIGN KEY (personalidade_id) REFERENCES public.galeria_diretores_personalidade(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3041 (class 2606 OID 60167)
-- Name: galeria_diretores_personalidade_galerias galeria_diretores_pe_galeria_id_fce4b2e8_fk_galeria_d; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.galeria_diretores_personalidade_galerias
    ADD CONSTRAINT galeria_diretores_pe_galeria_id_fce4b2e8_fk_galeria_d FOREIGN KEY (galeria_id) REFERENCES public.galeria_diretores_galeria(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3040 (class 2606 OID 60162)
-- Name: galeria_diretores_personalidade_galerias galeria_diretores_pe_personalidade_id_30de8388_fk_galeria_d; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.galeria_diretores_personalidade_galerias
    ADD CONSTRAINT galeria_diretores_pe_personalidade_id_30de8388_fk_galeria_d FOREIGN KEY (personalidade_id) REFERENCES public.galeria_diretores_personalidade(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3057 (class 2606 OID 84955)
-- Name: instituicao_fotoinstituicao instituicao_fotoinst_instituicao_id_f9ba77d0_fk_instituic; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.instituicao_fotoinstituicao
    ADD CONSTRAINT instituicao_fotoinst_instituicao_id_f9ba77d0_fk_instituic FOREIGN KEY (instituicao_id) REFERENCES public.instituicao_instituicao(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3058 (class 2606 OID 84961)
-- Name: instituicao_membro instituicao_membro_instituicao_id_39229cec_fk_instituic; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.instituicao_membro
    ADD CONSTRAINT instituicao_membro_instituicao_id_39229cec_fk_instituic FOREIGN KEY (instituicao_id) REFERENCES public.instituicao_instituicao(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3055 (class 2606 OID 76768)
-- Name: linha_tempo_fotoacontecimento linha_tempo_fotoacon_acontecimento_id_27cfb46f_fk_linha_tem; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.linha_tempo_fotoacontecimento
    ADD CONSTRAINT linha_tempo_fotoacon_acontecimento_id_27cfb46f_fk_linha_tem FOREIGN KEY (acontecimento_id) REFERENCES public.linha_tempo_acontecimento(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3039 (class 2606 OID 60154)
-- Name: linha_tempo_fotoevento linha_tempo_fotoeven_evento_id_7f50e698_fk_linha_tem; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.linha_tempo_fotoevento
    ADD CONSTRAINT linha_tempo_fotoeven_evento_id_7f50e698_fk_linha_tem FOREIGN KEY (evento_id) REFERENCES public.linha_tempo_evento(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3043 (class 2606 OID 60180)
-- Name: noticias_fotonoticia noticias_fotonoticia_noticia_id_ece26d4e_fk_noticias_noticia_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.noticias_fotonoticia
    ADD CONSTRAINT noticias_fotonoticia_noticia_id_ece26d4e_fk_noticias_noticia_id FOREIGN KEY (noticia_id) REFERENCES public.noticias_noticia(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3044 (class 2606 OID 60186)
-- Name: pesquisas_fotogrupopesquisa pesquisas_fotogrupop_grupo_pesquisa_id_efcbfb30_fk_pesquisas; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pesquisas_fotogrupopesquisa
    ADD CONSTRAINT pesquisas_fotogrupop_grupo_pesquisa_id_efcbfb30_fk_pesquisas FOREIGN KEY (grupo_pesquisa_id) REFERENCES public.pesquisas_grupopesquisa(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3045 (class 2606 OID 60192)
-- Name: pesquisas_membro pesquisas_membro_grupo_pesquisa_id_bbc94ddc_fk_pesquisas; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pesquisas_membro
    ADD CONSTRAINT pesquisas_membro_grupo_pesquisa_id_bbc94ddc_fk_pesquisas FOREIGN KEY (grupo_pesquisa_id) REFERENCES public.pesquisas_grupopesquisa(id) DEFERRABLE INITIALLY DEFERRED;


-- Completed on 2020-09-21 16:45:57

--
-- PostgreSQL database dump complete
--

